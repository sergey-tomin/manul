"""
Sergey Tomin, XFEL/DESY, 2017
"""

import numpy as np
import json
import pyqtgraph as pg
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets
from scipy import io
from mint.devices import *
import copy
from ocelot.cpbd.elements import Marker, Monitor

def save_json(filename, py_dict):
    with open(filename, 'w') as f:
        json.dump(py_dict, f)


def mat2json(mat_file, json_file):
    a = io.loadmat(mat_file, variable_names=None, mat_dtype=True)
    y = a["data"]["y"][0, 0][0]
    x = a["data"]["x"][0, 0][0]
    names = a["data"]["names"][0, 0]
    names = [str(name.replace(" ", "")) for name in names]
    orbit = {}
    for i in range(len(x)):
        orbit[names[i]] = [float(x[i] / 1000.), float(y[i] / 1000.)]
    save_json(json_file, orbit)


class GoldenOrbit:
    def __init__(self, parent):
        self.ui = parent.ui
        self.parent = parent
        self.master = parent.parent
        self.golden_orbit = {}
        self.bpms = []
        self.add_orbit_plot()
        self.online_calc = True
        self.ui.pb_golden_orbit.clicked.connect(self.start_stop_golden_orbit)
        self.ui.pb_set_golden.clicked.connect(self.set_golden_orbit)
        self.ui.pb_zero_gold.clicked.connect(self.set_zero_golden_orbit)
        self.ui.actionLoad_Golden_Orbit.triggered.connect(self.load_golden_from)
        self.ui.actionSave_Golden_Orbit.triggered.connect(self.save_golden_as)
        self.ui.actionLoad_GO_from_Orbit_Display.triggered.connect(self.load_golden_from_OD)
        self.ui.actionTake_Ref_Orbit_from_Server.triggered.connect(self.load_ref_from_doocs)
        self.ui.actionTake_GO_from_Server.triggered.connect(self.load_gold_from_doocs)
        self.ui.pb_doocs_ref2go.clicked.connect(self.load_ref_from_doocs)
        self.ui.pb_doocs_go2go.clicked.connect(self.load_gold_from_doocs)
        self.ui.pb_uncheck_bpms.clicked.connect(lambda: self.parent.getRows(0, self.ui.table_golden_bpm))
        self.ui.pb_check_bpms.clicked.connect(lambda: self.parent.getRows(2, self.ui.table_golden_bpm))
        self.ui.pb_use_go.clicked.connect(self.editor2dict)

    def set_go_warning(self, warn):
        if warn:
            self.ui.groupBox_go.setStyleSheet("QGroupBox{ border: 1px solid red;}")
        else:
            self.ui.groupBox_go.setStyleSheet("QGroupBox { border: 1px solid #76797C;}")

    def load_ref_from_doocs(self):
        self.set_go_warning(warn=True)
        self.parent.read_orbit()
        self.golden_orbit = {}
        ref_orbit = self.parent.mi_orbit.read_doocs_ref_orbit()
        for valid, x, y, z_pos, bpm_id in ref_orbit:
            if valid == 0:
                self.golden_orbit[bpm_id] = [x*1e-3, y*1e-3] # mm -> m

        for elem in self.parent.bpms:
            if elem.id in self.golden_orbit.keys():
                x_gold = self.golden_orbit[elem.id][0]
                y_gold = self.golden_orbit[elem.id][1]
                elem.x_ref = x_gold
                elem.y_ref = y_gold
            else:
                elem.x_ref = 0.
                elem.y_ref = 0.
        self.dict2editor()

    def load_gold_from_doocs(self):
        self.set_go_warning(warn=True)
        self.parent.read_orbit()
        self.golden_orbit = {}
        gold_orbit = self.parent.mi_orbit.read_doocs_gold_orbit()
        for valid, x, y, z_pos, bpm_id in gold_orbit:
            if valid == 0:
                self.golden_orbit[bpm_id] = [x*1e-3, y*1e-3] # mm -> m

        for elem in self.parent.bpms:
            if elem.id in self.golden_orbit.keys():
                x_gold = self.golden_orbit[elem.id][0]
                y_gold = self.golden_orbit[elem.id][1]
                elem.x_ref = x_gold
                elem.y_ref = y_gold
                #print(elem.id, elem.x_ref, elem.y_ref)
            else:
                elem.x_ref = 0.
                elem.y_ref = 0.
        self.dict2editor()

    def set_golden_orbit(self):
        """
        reads orbit and set BPM.x_ref and BPM.y_ref from actual readings.
        Writes these refs to dictionary: self.golden_orbit

        :return:
        """
        self.set_go_warning(warn=True)
        self.parent.read_orbit()
        self.golden_orbit = {}
        for elem in self.parent.bpms:
            elem.x_ref = elem.x
            elem.y_ref = elem.y
            self.golden_orbit[elem.id] = [elem.x, elem.y]
        self.dict2editor()

    def set_zero_golden_orbit(self):
        """
        Set BPM.x_ref and BPM.y_ref to zeros.
        Writes these refs to dictionary: self.golden_orbit

        :return:
        """
        self.set_go_warning(warn=False)
        self.golden_orbit = {}
        for elem in self.parent.bpms:
            elem.x_ref = 0.
            elem.y_ref = 0.
            self.golden_orbit[elem.id] = [0., 0.]
        self.dict2editor()

    def dict2golden_orbit(self):
        """
        Method sets BPM.x_ref and BPM.y_ref from dictionary: self.golden_orbit

        :return:
        """
        #for elem in self.parent.orbit.bpms:
        for elem in self.parent.bpms:
            if elem.id in self.golden_orbit.keys():
                x_gold = self.golden_orbit[elem.id][0]
                y_gold = self.golden_orbit[elem.id][1]
                elem.x_ref = x_gold
                elem.y_ref = y_gold
            else:
                elem.x_ref = 0.
                elem.y_ref = 0.

    def update_golden_orbit(self, new_dict):
        for name in self.golden_orbit.keys():
            if name in new_dict.keys():
                self.golden_orbit[name] = new_dict[name]

    def start_stop_golden_orbit(self):
        if self.ui.pb_golden_orbit.text() == "Show GO":
            self.ui.pb_golden_orbit.setText("Hide GO")
            self.ui.pb_golden_orbit.setStyleSheet("color: rgb(255, 255, 0);")
            s_bpm = np.array([])
            x_bpm = np.array([])
            y_bpm = np.array([])
            bpms = self.parent.get_dev_from_cb_state(self.parent.bpms)
            for elem in bpms:
                #print(elem.id)
                try:
                    #print(elem.id, elem.id in self.golden_orbit.keys(), self.golden_orbit.keys())
                    if elem.id in self.golden_orbit.keys():
                        x_gold = self.golden_orbit[elem.id][0]
                        y_gold = self.golden_orbit[elem.id][1]
                        elem.x_ref = x_gold
                        elem.y_ref = y_gold
                        s_bpm = np.append(s_bpm, elem.s)
                        x_bpm = np.append(x_bpm, x_gold*1000)
                        y_bpm = np.append(y_bpm, y_gold*1000)
                except:
                    print("could not read BPM golden", elem.id)

            s_bpm += self.parent.parent.lat_zi
            self.parent.plot_x.addItem(self.parent.orb_x_golden)
            self.parent.plot_y.addItem(self.parent.orb_y_golden)
            self.parent.orb_x_golden.setData(x=s_bpm, y=x_bpm)
            self.parent.orb_y_golden.setData(x=s_bpm, y=y_bpm)
            self.parent.orb_y.update()
            self.parent.orb_x.update()

        else:
            self.parent.plot_x.removeItem(self.parent.orb_x_golden)
            self.parent.plot_y.removeItem(self.parent.orb_y_golden)
            self.parent.plot_x.legend.removeItem(self.parent.orb_x_golden.name())
            self.parent.plot_y.legend.removeItem(self.parent.orb_y_golden.name())
            self.ui.pb_golden_orbit.setStyleSheet("color: rgb(85, 255, 255);")
            self.ui.pb_golden_orbit.setText("Show GO")
            #self.orb_x_golden.setData(x=[], y=[])
            #self.orb_y_golden.setData(x=[], y=[])
            #self.orb_y.update()
            #self.orb_x.update()

    def save_golden_orbit(self, filename):
        orbit = {}
        for bpm in self.master.orbit.bpms:
            orbit[bpm.id] = [bpm.x, bpm.y]
        with open(filename, 'w') as f:
            json.dump(orbit, f)
        print("SAVE Ref Orbit")

    def restore_golden_orbit(self, filename):
        with open(filename, 'r') as f:
            orbit = json.load(f)
        self.golden_orbit = orbit

    def mat2orbit(self, mat_file):
        a = io.loadmat(mat_file, variable_names=None, mat_dtype=True)
        y = a["data"]["y"][0, 0][0]
        x = a["data"]["x"][0, 0][0]
        names = a["data"]["names"][0, 0]
        names = [str(name.replace(" ", "")) for name in names]
        orbit = {}
        for i in range(len(x)):
            orbit[names[i]] = [float(x[i] / 1000.), float(y[i] / 1000.)]
        return orbit

    def restore_golden_orbit_from_mat(self, filename):
        orbit = self.mat2orbit(filename)
        self.golden_orbit = orbit

    def save_golden_as(self):
        filename = QFileDialog.getSaveFileName(self.master, 'Save Golden Orbit',
                                               self.master.gold_orbits_dir, "txt (*.json)", None, QFileDialog.DontUseNativeDialog)[0]
        if filename:
            name = filename.split("/")[-1]
            parts = name.split(".")
            body_name = parts[0]

            if len(parts)<2 or parts[1] !="json":
                part = filename.split(".")[0]
                filename = part + ".json"
            self.save_golden_orbit(filename)

    def load_golden_from(self):
        filename = QFileDialog.getOpenFileName(self.master, 'Load Golden Orbit',
                                               self.master.gold_orbits_dir, "txt (*.json *.mat)", None, QFileDialog.DontUseNativeDialog)[0]
        if filename:
            (body_name, extension) = filename.split("/")[-1].split(".")
            if extension == "mat":
                self.restore_golden_orbit_from_mat(filename=filename)
            else:
                self.restore_golden_orbit(filename)

    def load_golden_from_OD(self):
        filename = QFileDialog.getOpenFileName(self.master, 'Load Golden Orbit',
                                               self.master.gold_orbits_from_OD_dir, "txt (*.mat)", None, QFileDialog.DontUseNativeDialog)[0]
        print(filename)
        if filename:
            #print(filename)
            self.restore_golden_orbit_from_mat(filename=filename)


    def dict2editor(self):
        #print(self.bpms)

        if len(self.bpms) == 0:
            return 0

        for elem in self.bpms:

            if elem.id in self.golden_orbit.keys():
                x_gold = self.golden_orbit[elem.id][0]
                y_gold = self.golden_orbit[elem.id][1]
                elem.x_ref = x_gold
                elem.y_ref = y_gold
                elem.ui.set_spin_values((elem.x_ref*1000, elem.y_ref*1000))

            else:

                elem.x_ref = 0.
                elem.y_ref = 0.
            elem.x_init = elem.x_ref
            elem.y_init = elem.y_ref

    def editor2dict(self):
        if len(self.bpms) == 0:
            return 0
        for elem in self.bpms:
            if elem.id in self.golden_orbit.keys():
                self.golden_orbit[elem.id] = [elem.x_ref, elem.y_ref]
                #print(elem.id, self.golden_orbit[elem.id])
        self.dict2golden_orbit()

    def copy_bpms(self, bpms):
        self.bpms = []
        for bpm in bpms:
            bpm_copy = Monitor()
            for atrb in bpm.__dict__.keys():
                if atrb not in ["mi", "ui"]:
                    bpm_copy.__dict__[atrb] = bpm.__dict__[atrb]
            for atrb in bpm.element.__dict__.keys():
                if atrb not in ["mi", "ui"]:
                    bpm_copy.element.__dict__[atrb] = bpm.element.__dict__[atrb]
            bpm_copy.x_init = 0
            bpm_copy.y_init = 0
            self.bpms.append(bpm_copy)
        self.online_calc = False
        self.add_bpms2table(self.bpms, self.ui.table_golden_bpm, calc_obj=self.update_plot, sp_box1=True, sp_box2=True,
                                spin_params=[-30, 30, 0.1], check_box=True)
        self.online_calc = True
        self.dict2editor()
        self.update_plot()


    def add_orbit_plot(self):
        win = pg.GraphicsLayoutWidget()
        self.plot_x = win.addPlot(row=0, col=0)
        self.plot_x.showGrid(1, 1, 1)
        self.plot_y = win.addPlot(row=1, col=0)
        self.plot_x.setXLink(self.plot_y)
        self.plot_y.showGrid(1, 1, 1)
        self.plot_y.getAxis('left').enableAutoSIPrefix(enable=False)  # stop the auto unit scaling on y axes
        layout = QtWidgets.QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.ui.widget_6.setLayout(layout)
        layout.addWidget(win, 0, 0)
        self.plot_y.setAutoVisible(y=True)

        self.plot_y.addLegend()
        self.plot_x.addLegend()

        pen = pg.mkPen((255, 140, 0), width=3)
        self.orb_y_golden = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', symbolBrush=(255, 140, 0), name='Y golden', antialias=True)
        self.plot_y.addItem(self.orb_y_golden)


        self.orb_x_golden = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', symbolBrush=(255, 140, 0), name='X golden', antialias=True)
        self.plot_x.addItem(self.orb_x_golden)
        self.plot_x.sigRangeChanged.connect(self.zoom_signal)
        self.plot_x.setYRange(-2, 2)
        self.plot_y.setYRange(-2, 2)


    def zoom_signal(self):

        if len(self.bpms) == 0:
            return
        s_up = self.plot_y.viewRange()[0][0]
        s_down = self.plot_y.viewRange()[0][1]
        s_bpm_pos = np.array([q.s for q in self.bpms]) + self.master.lat_zi
        s_bpm_up = s_up if s_up <= s_bpm_pos[-1] else s_bpm_pos[-1]
        s_bpm_down = s_down if s_down >= s_bpm_pos[0] else s_bpm_pos[0]
        s_bpm_pos = np.array([q.s for q in self.bpms]) + self.master.lat_zi
        s_bpm_up = s_bpm_up if s_bpm_up <= s_bpm_pos[-1] else s_bpm_pos[-1]
        s_bpm_down = s_bpm_down if s_bpm_down >= s_bpm_pos[0] else s_bpm_pos[0]
        indexes_bpm = np.arange(np.argwhere(s_bpm_pos >= s_bpm_up)[0][0], np.argwhere(s_bpm_pos <= s_bpm_down)[-1][0] + 1)
        mask_bpm = np.ones(len(self.bpms), bool)
        mask_bpm[indexes_bpm] = 0
        self.bpms = np.array(self.bpms)
        [q.ui.set_hide(hide=False) for q in self.bpms[indexes_bpm]]
        [q.ui.set_hide(hide=True) for q in self.bpms[mask_bpm]]

    def update_plot(self):
        if not self.online_calc:
            return

        bpms = self.bpms
        s_bpm = np.array([bpm.s for bpm in bpms]) + self.master.lat_zi
        for bpm in bpms:
            x, y = bpm.ui.get_spin_values()
            bpm.x_ref = x/1000
            bpm.y_ref = y/1000
            bpm.ui.is_touched((np.abs(bpm.x_init - bpm.x_ref) > 1e-5 or np.abs(bpm.y_init - bpm.y_ref) > 1e-5))

        x_bpm = np.array([bpm.x_ref*1000 for bpm in bpms])
        y_bpm = np.array([bpm.y_ref*1000 for bpm in bpms])
        self.orb_x_golden.setData(x=s_bpm, y=x_bpm)
        self.orb_y_golden.setData(x=s_bpm, y=y_bpm)
        self.orb_y_golden.update()
        self.orb_x_golden.update()

    def add_bpms2table(self, devs, w_table, calc_obj=None, sp_box1=False, sp_box2=False, spin_params=[-30, 30, 0.1], check_box=False):
        """ Initialize the UI table object """
        
        def create_spin_box(dev, atrb, spin_params, calc_obj):
            eng = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)
            spin_box = QtWidgets.QDoubleSpinBox()
            spin_box.setStyleSheet("color: #b1b1b1; font-size: 16px; background-color:#595959; border: 2px solid #b1b1b1")
            spin_box.setLocale(eng)
            spin_box.setDecimals(3)
            spin_box.setMaximum(spin_params[1])
            spin_box.setMinimum(spin_params[0])
            spin_box.setSingleStep(spin_params[2])
            spin_box.setValue(dev.__getattr__(atrb))
            spin_box.setAccelerated(True)
            spin_box.valueChanged.connect(calc_obj)
            return spin_box

        self.spin_boxes = []

        w_table.setRowCount(0)

        for row in range(len(devs)):
            #eng = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)
            w_table.setRowCount(row + 1)
            pv = devs[row].id
            # put PV in the table
            w_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(pv)))
            # put start val in

            if sp_box1:
                spin_box = create_spin_box(devs[row], "x_ref", spin_params, calc_obj)
                w_table.setCellWidget(row, 1, spin_box)
            else:
                w_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(devs[row].x)))
            if sp_box2:
                spin_box = create_spin_box(devs[row], "y_ref", spin_params, calc_obj)
                w_table.setCellWidget(row, 2, spin_box)
            else:
                w_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(devs[row].y)))


            if check_box:
                checkBoxItem = QtWidgets.QTableWidgetItem()
                checkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                flags = checkBoxItem.flags()
                checkBoxItem.setFlags(flags)
                w_table.setItem(row, 3, checkBoxItem)
            devs[row].row = row
            ui = BPMUI()
            ui.tableWidget = w_table
            ui.row = row
            ui.col = 2
            #ui.set_spin_values((devs[row].x_ref*1000, devs[row].y_ref*1000))
            devs[row].ui = ui
        w_table.resizeColumnsToContents()