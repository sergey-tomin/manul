"""
Sergey Tomin. XFEL/DESY, 2017.
"""
#QT imports
from PyQt4.QtGui import QApplication, QFrame, QPixmap, QMessageBox
from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
#normal imports
import numpy as np
#import epics
import sys
import os


path = os.path.realpath(__file__)
indx = path.find("manul")
print("PATH", os.path.realpath(__file__), path[:indx])
sys.path.append(path[:indx])
if sys.version_info[0] == 2:
    from imp import reload
else:
    from importlib import reload
import time
import pyqtgraph as pg
from gui_main import *
from orbit import OrbitInterface
from lattices.xfel_i1_890 import *
from lattices.xfel_l1_890 import *
from lattices.xfel_l2_890 import *
from lattices.xfel_l3_890 import *
from ocelot import *
from ocelot.gui.accelerator import *
from ocelot.optimizer.mint.xfel_interface import *

from ocelot.optimizer.mint.opt_objects import Device
from ocelot.optimizer.mint.xfel_interface import *
import copy
from scipy import optimize
#GUI layout file



#import taperThread

class DeviceUI:
    def __init__(self, ui=None):
        self.tableWidget = None
        self.row = 0
        self.col = 0

    def get_value(self):
        return self.tableWidget.cellWidget(self.row, self.col).value()

    def set_value(self, val):
        self.tableWidget.cellWidget(self.row, self.col).setValue(val)

    def set_init_value(self, val):
        val = "{:1.4e}".format(val)
        self.tableWidget.item(self.row, 1).setText(str(val))

    def get_init_value(self):
        return float(self.tableWidget.item(self.row, 1).text())

    def uncheck(self):
        item = self.tableWidget.item(self.row, 3)
        item.setCheckState(False)

    def check(self):
        item = self.tableWidget.item(self.row, 3)
        item.setCheckState(True)

    def state(self):
        item = self.tableWidget.item(self.row, 3)
        state = item.checkState()
        return state

class MDevice(Device):
    def __init__(self, eid=None):
        super(MDevice, self).__init__(eid=eid)





class ManulInterfaceWindow(QFrame):
    """ Main class for the GUI application """
    def __init__(self):
        """
        Initialize the GUI and QT UI aspects of the application.
        Initialize the scan parameters.
        Connect start and logbook buttons on the scan panel.
        Initialize the plotting.
        Make the timer object that updates GUI on clock cycle during a scan.
        """
        # PATHS
        path = os.path.realpath(__file__)
        indx = path.find("ocelot" + os.sep + "optimizer")
        self.path2ocelot = path[:indx]
        self.optimizer_path = self.path2ocelot + "ocelot" + os.sep + "optimizer" + os.sep
        self.config_dir = self.path2ocelot + "config_optim" +os.sep
        self.set_file = self.config_dir + "default.json" # ./parameters/default.json"
        self.obj_func_path = self.optimizer_path + "mint" + os.sep + "obj_function.py"
        self.obj_save_path = self.config_dir +  "obj_funcs" + os.sep
        # initialize
        QFrame.__init__(self)

        self.logbook = "xfellog"
        self.dev_mode = True

        self.ui = MainWindow(self)
        self.orbit = OrbitInterface(parent=self)

        self.cell_back_track = (cell_i1 + cell_l1 + cell_l2)
        self.copy_cells = copy.deepcopy((cell_i1 , cell_l1, cell_l2))
        self.online_calc = True
        self.mi = XFELMachineInterface()
        #self.mi = TestMachineInterface()
        #QFrame.__init__(self)
        #self.ui = Ui_Form()
        #self.ui.setupUi(self)


        #load in the dark theme style sheet
        self.loadStyleSheet()

        #timer for plots, starts when scan starts
        self.multiPvTimer = QtCore.QTimer()
        #self.multiPvTimer.timeout.connect(self.getPlotData)
        self.pvs = ["sdf","asdf"]
        #self.initTable()
        #print("quads", self.quads)
        self.add_plot()

        self.lat = self.return_lat()
        #self.tws0 = self.return_tws()
        #self.load_lattice()
        #taperThread.Taper(initPVs = True, mi=self.mi) #update taper PVs with initial taper parameters


        self.ui.pb_write.clicked.connect(self.calc_twiss)
        self.ui.pb_read.clicked.connect(self.read_quads)
        self.ui.pb_reset.clicked.connect(self.reset_quads)

        #self.ui.cb_select_alg.addItem(self.name_gauss)
        self.ui.cb_lattice.addItem("Injector")
        self.ui.cb_lattice.addItem("I1 + L1")
        self.ui.cb_lattice.addItem("I1 + L1 + L2")
        self.ui.cb_lattice.addItem("L1")
        self.ui.cb_lattice.addItem("L2")
        self.ui.cb_lattice.currentIndexChanged.connect(self.return_lat)
        self.ui.cb_otr55.setChecked(True)
        self.ui.cb_coupler_kick.stateChanged.connect(self.apply_coupler_kick)
        self.ui.cb_sec_order.stateChanged.connect(self.apply_second_order)
        #self.ui.pb_write.clicked.connect(self.match)
        self.ui.pb_reload.clicked.connect(self.reload_lat)

    def reload_lat(self):
        cell_i1 = copy.deepcopy(self.copy_cells[0])
        cell_l1 = copy.deepcopy(self.copy_cells[1])
        cell_l2 = copy.deepcopy(self.copy_cells[2])
        try:
            pass
        except:
            print("ERROR in RELOAD")



    def update_table(self):
        for quad in self.quads:
            quad.ui.set_init_value(quad.kick_mrad)
            quad.ui.set_value(quad.kick_mrad)


    def reset_quads(self):
        for quad in self.quads:
            #print(quad.i_kick)
            quad.ui.set_value(quad.i_kick)
        #self.calc()

    def read_cavs(self):
        "XFEL.RF/LLRF.ENERGYGAIN.ML/M2.A4.L2/ENERGYGAIN.SA1"

    def read_quads(self):
        self.online_calc = False
        for elem in self.quads:
            elem.kick_mrad = elem.mi.get_value()
            k1 = elem.kick_mrad/elem.l*1e-3
            elem.k1 = k1
            elem.i_kick = elem.kick_mrad
            #print(elem.i_kick)
            elem.ui.set_init_value(elem.kick_mrad)
            elem.ui.set_value(elem.kick_mrad)
        self.online_calc = True
        self.lat.update_transfer_maps()

        self.tws0 = self.back_tracking()
        #print("back_tracking = ", self.tws0)
        tws = twiss(self.lat, self.tws0)
        beta_x = [tw.beta_x for tw in tws]
        beta_y = [tw.beta_y for tw in tws]
        dx = [tw.Dx for tw in tws]
        dy = [tw.Dy for tw in tws]
        s = [tw.s for tw in tws]

        self.update_plot(s, beta_x, beta_y, dx, dy)

        #self.update_table()

    def back_tracking(self):
        tws0 = self.read_twiss()
        if self.ui.cb_otr218.isChecked():
            stop = otrb_218_b1

        elif self.ui.cb_otr450.isChecked():
            stop = otrb_450_b2

        else:
            stop = otrc_55_i1


        lat_tmp = MagneticLattice(self.cell_back_track, stop=stop)
        lat_tmp = MagneticLattice(lat_tmp.sequence[::-1])
        for elem in lat_tmp.sequence:
            if elem.__class__  == Cavity:
                elem.phi -= 180
                #print(elem.v, elem.phi)
        lat_tmp.update_transfer_maps()

        tws0.alpha_x = -tws0.alpha_x
        tws0.alpha_y = -tws0.alpha_y
        #print("start", tws0)
        tws = twiss(lat_tmp, tws0)
        #plot_opt_func(lat_tmp, tws)
        #plt.show()
        self.tws0 = Twiss()
        self.tws0.beta_x = tws[-1].beta_x
        self.tws0.beta_y = tws[-1].beta_y
        self.tws0.alpha_x = -tws[-1].alpha_x
        self.tws0.alpha_y = -tws[-1].alpha_y
        self.tws0.s = 0
        self.tws0.E = tws[-1].E
        for elem in lat_tmp.sequence:
            if elem.__class__  == Cavity:
                elem.phi += 180
        lat_tmp.update_transfer_maps()
        return self.tws0


    def read_twiss(self):
        tws = Twiss()
        if self.ui.cb_otr218.isChecked():
            section = "B1"
            tws.E = 0.7
        elif self.ui.cb_otr450.isChecked():
            section = "B2"
            tws.E = 2.4
        else:
            self.ui.cb_otr55.setChecked(True)
            section = "I1"
            tws.E = 0.130

        ch_beta_x = "XFEL.UTIL/BEAM_PARAMETER/" + section + "/PROJECTED_X.BETA.SA1"
        ch_alpha_x = "XFEL.UTIL/BEAM_PARAMETER/" + section + "/PROJECTED_X.ALPHA.SA1"
        ch_beta_y = "XFEL.UTIL/BEAM_PARAMETER/" + section + "/PROJECTED_Y.BETA.SA1"
        ch_alpha_y = "XFEL.UTIL/BEAM_PARAMETER/" + section + "/PROJECTED_Y.ALPHA.SA1"
        ch_energy = "XFEL.UTIL/BEAM_PARAMETER/" + section + "/PROJECTED_X.ENERGY.SA1"

        tws.beta_x = self.mi.get_value(ch_beta_x)
        tws.beta_y = self.mi.get_value(ch_beta_y)
        tws.alpha_x = self.mi.get_value(ch_alpha_x)
        tws.alpha_y = self.mi.get_value(ch_alpha_y)
        #tws.E = self.mi.get_value(ch_energy)*0.001
        print(tws)
        return tws

    def match(self):
        quads = [qi_46_i1, qi_47_i1, qi_50_i1, qi_52_i1, qi_53_i1, qi_54_i1]
        x = np.array([q.kick_mrad for q in quads])
        def error_func(x):
            #print(x)
            for i, quad in enumerate(quads):
                quad.kick_mrad = x[i]
                quad.k1 = x[i]/quad.l/1000.
            self.lat.update_transfer_maps()
            tws = twiss(self.lat, self.tws0)
            err = np.sqrt((tws[-1].beta_x - self.tws_end.beta_x)**2 +
            (tws[-1].beta_y - self.tws_end.beta_y)**2 +
            (tws[-1].alpha_x - self.tws_end.alpha_x)**2 +
            (tws[-1].alpha_y - self.tws_end.alpha_y)**2 )
            print(err)
            return err


        res = optimize.fmin(error_func, x, xtol=0.1)
        print(res)
        for i, quad in enumerate(quads):
            quad.kick_mrad = res[i]
            quad.k1 = res[i]/quad.l/1000.
            quad.ui.set_value(quad.kick_mrad)



    def apply_coupler_kick(self):
        print(self.ui.cb_coupler_kick.isChecked())
        if self.ui.cb_coupler_kick.isChecked():
            for elem in self.lat.sequence:
                if elem.__class__ == Cavity and not(".AH1." in elem.id):# and not(".A1." in elem.id):
                    elem.coupler_kick = True
                    elem.vx_up = -56.813 + 10.751j
                    elem.vy_up = -41.091 + 0.5739j
                    elem.vxx_up = 0.99943 - 0.81401j
                    elem.vxy_up = 3.4065 - 0.4146j
                    elem.vx_down = -24.014 + 12.492j
                    elem.vy_down = 36.481 +  7.9888j
                    elem.vxx_down = -4.057 - 0.1369j
                    elem.vxy_down = 2.9243 - 0.012891j
        else:
            for elem in self.lat.sequence:
                if elem.__class__ == Cavity and not(".AH1." in elem.id):# and not(".A1." in elem.id):
                    elem.coupler_kick = False
        self.lat.update_transfer_maps()
        self.calc_twiss()

        # calc orbit
        self.orbit.calc_orbit()

    def apply_second_order(self):
        print(self.ui.cb_sec_order.isChecked())
        method = MethodTM()
        if self.ui.cb_sec_order.isChecked():
            method.global_method = SecondTM
        else:
            method.global_method = TransferMap
        self.lat = MagneticLattice(self.lat.sequence, method=method)
        #self.lat.update_transfer_maps()
        #self.calc_twiss()
        #print("second")
        # calc orbit
        self.orbit.calc_orbit()

    def return_lat(self):
        #self.lat = MagneticLattice(cell_i1+cell_l1)
        current_lat = self.ui.cb_lattice.currentText()
        method = MethodTM()
        method.global_method = TransferMap
        if current_lat == "I1 + L1":
            self.lat = MagneticLattice(cell_i1 + cell_l1, method=method)
            self.tws_des = tws_i1

            tmp_lat = MagneticLattice(self.copy_cells[0] + self.copy_cells[1] )
            tws = twiss(tmp_lat, self.tws_des)
            self.b_x_des = [tw.beta_x for tw in tws]
            self.b_y_des = [tw.beta_y for tw in tws]
            self.tws_end = tws[-1]
            print(len(self.lat.sequence))
        elif current_lat == "L1":
            self.lat = MagneticLattice(cell_l1, method=method)
            self.tws_des = tws_l1

            tmp_lat = MagneticLattice(self.copy_cells[1] )
            tws = twiss(tmp_lat, self.tws_des)
            self.b_x_des = [tw.beta_x for tw in tws]
            self.b_y_des = [tw.beta_y for tw in tws]
            self.tws_end = tws[-1]

        elif current_lat == "I1 + L1 + L2":
            self.lat = MagneticLattice(cell_i1 + cell_l1 + cell_l2, method=method)
            self.tws_des = tws_i1
            tmp_lat = MagneticLattice(self.copy_cells[0] + self.copy_cells[1]  + self.copy_cells[2])
            tws = twiss(tmp_lat, self.tws_des)
            self.b_x_des = [tw.beta_x for tw in tws]
            self.b_y_des = [tw.beta_y for tw in tws]
            self.tws_end = tws[-1]

        elif current_lat == "L2":
            self.lat = MagneticLattice(cell_l2 , method=method)
            self.tws_des = tws_l2
            tmp_lat = MagneticLattice( self.copy_cells[2])
            tws = twiss(tmp_lat, self.tws_des)
            self.b_x_des = [tw.beta_x for tw in tws]
            self.b_y_des = [tw.beta_y for tw in tws]
            self.tws_end = tws[-1]

        else:
            self.lat = MagneticLattice(cell_i1 , method=method)
            self.tws_des = tws_i1
            tmp_lat = MagneticLattice(self.copy_cells[0])
            tws = twiss(tmp_lat, self.tws_des)
            self.b_x_des = [tw.beta_x for tw in tws]
            self.b_y_des = [tw.beta_y for tw in tws]
            self.tws_end = tws[-1]
            print(len(self.lat.sequence))
        self.tws0 = copy.deepcopy(self.tws_des)
        self.load_lattice()

        self.calc_twiss()

        # for orbit
        #self.orbit.load_orbit_devs()
        self.orbit.calc_orbit()
        #self.ui.tableWidget.repaint()
        #self.ui.tableWidget.resizeColumnsToContents()
        #self.repaint()
        return self.lat

    def return_tws(self):
        tws0 = Twiss()
        tws0.E = 0.005
        tws0.beta_x = 55.7887190242
        tws0.beta_y = 55.7887190242
        tws0.alpha_x = 18.185436973
        tws0.alpha_y = 18.185436973
        return tws0

    def load_devices(self, types):
        devices = []
        mi_devs = {}
        #cell_i1_copy = copy.deepcopy(cell_i1_copy)
        #lat_tmp = MagneticLattice(cell_i1_copy)

        L = 0
        for elem in self.lat.sequence:
            L += elem.l
            if elem.__class__ in types:
                elem.s_pos = L - elem.l/2.
                elem.k1_th = elem.k1
                elem.kick_mrad = elem.k1 * elem.l * 1000.
                elem.i_kick = elem.kick_mrad
                devices.append(elem)
                #elem.mi = Device(eid="XFEL.MAGNETS/MAGNET.ML/" + elem.id + "/KICK_MRAD.SP")
                if "ps_id" in elem.__dict__:
                    if elem.ps_id not in mi_devs.keys():
                        mi_dev = Device(eid="XFEL.MAGNETS/MAGNET.ML/" + elem.id + "/KICK_MRAD.SP")
                        mi_dev.mi = self.mi
                        elem.mi = mi_dev
                        mi_devs[elem.ps_id] = mi_dev
                    else:
                        elem.mi = mi_devs[elem.ps_id]
                else:
                    mi_dev = Device(eid="XFEL.MAGNETS/MAGNET.ML/" + elem.id + "/KICK_MRAD.SP")
                    mi_dev.mi = self.mi
                    elem.mi = mi_dev
        return devices


    def load_lattice(self):
        self.quads = self.load_devices(types=[Quadrupole])
        self.add_devs2table(self.quads, w_table=self.ui.tableWidget, calc_obj=self.calc_twiss)

        #self.init_kick_mrad = np.array([q.kick_mrad for q in self.quads])
        self.quad_ampl = np.max(np.abs(np.array([q.kick_mrad for q in self.quads])))
        # for orbit
        self.orbit.load_orbit_devs()

        tws = twiss(self.lat, self.tws_des)
        #plot_opt_func(lat, tws, top_plot=["Dx", "Dy"])
        #plt.show()
        #beta_x_des = [tw.beta_x for tw in tws]
        #beta_y_des = [tw.beta_y for tw in tws]
        #dx_des = [tw.Dx for tw in tws]
        #dy_des = [tw.Dy for tw in tws]
        s = [tw.s for tw in tws]
        self.beta_x_des.setData(x=s, y=self.b_x_des)
        self.beta_y_des.setData(x=s, y=self.b_y_des)
        self.r_items = self.plot_lat(plot_wdg=self.plot2, types=[Quadrupole])

    def calc_twiss(self, calc=True):
        #lat = MagneticLattice(cell)
        if self.online_calc == False:
            return

        # L = 0
        for elem in self.lat.sequence:
            if elem.__class__ in [Quadrupole]:
                #print(elem.id, elem.row)
                elem.kick_mrad = elem.ui.get_value()
                elem.k1 = elem.kick_mrad/elem.l/1000.
                if np.abs(np.abs(elem.kick_mrad) - np.abs(elem.i_kick))> 1:
                    self.r_items[elem.ui.row].setBrush(pg.mkBrush("r"))
                    self.ui.tableWidget.item(elem.row, 1).setForeground(QtGui.QColor(255, 101, 101))  # red
                else:
                    self.ui.tableWidget.item(elem.row, 1).setForeground(QtGui.QColor(255, 255, 255))  # white
                    self.r_items[elem.ui.row].setBrush(pg.mkBrush("g"))
                r = self.r_items[elem.ui.row]
                sizes = r.init_params
                #sizes = list(r.boundingRect().getRect())
                sizes[3] = 10*elem.kick_mrad/self.quad_ampl
                r.setRect(sizes[0], sizes[1], sizes[2], sizes[3])

        self.lat.update_transfer_maps()
        #print("test")
        # exit(0)
        tws = twiss(self.lat, self.tws0)
        #print(tws[-1], self.tws0)
        #plot_opt_func(lat, tws, top_plot=["Dx", "Dy"])
        #plt.show()
        beta_x = [tw.beta_x for tw in tws]
        beta_y = [tw.beta_y for tw in tws]
        dx = [tw.Dx for tw in tws]
        dy = [tw.Dy for tw in tws]
        s = [tw.s for tw in tws]

        self.update_plot(s, beta_x, beta_y, dx, dy)

    def add_devs2table(self, devs, w_table, calc_obj, spin_params=[-5000, 5000, 5], check_box=False):
        """ Initialize the UI table object """
        #spin_boxes = [QtGui.QDoubleSpinBox()]*
        self.spin_boxes = []
        w_table.setRowCount(0)
        for row in range(len(devs)):
            eng = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)
            w_table.setRowCount(row + 1)
            pv = devs[row].id
            # put PV in the table
            w_table.setItem(row, 0, QtGui.QTableWidgetItem(str(pv)))
            # put start val in
            w_table.setItem(row, 1, QtGui.QTableWidgetItem(str(devs[row].kick_mrad)))
            spin_box = QtGui.QDoubleSpinBox()
            spin_box.setStyleSheet("color: #b1b1b1; font-size: 16px; background-color:#595959; border: 2px solid #b1b1b1")
            spin_box.setLocale(eng)
            spin_box.setDecimals(4)
            spin_box.setMaximum(spin_params[1])
            spin_box.setMinimum(spin_params[0])
            spin_box.setSingleStep(spin_params[2])
            spin_box.setValue(devs[row].kick_mrad)
            spin_box.setAccelerated(True)
            spin_box.valueChanged.connect(calc_obj)
            # spin_box.setFixedWidth(50)
            w_table.setCellWidget(row, 2, spin_box)
            #w_table.resizeColumnsToContents()
            self.spin_boxes.append(spin_box)

            if check_box:
                checkBoxItem = QtGui.QTableWidgetItem()
                # checkBoxItem.setBackgroundColor(QtGui.QColor(100,100,150))
                checkBoxItem.setCheckState(QtCore.Qt.Checked)
                flags = checkBoxItem.flags()
                # print("FLAG", flags)
                # flags != flags
                checkBoxItem.setFlags(flags)
                w_table.setItem(row, 3, checkBoxItem)

            devs[row].row = row

            ui = DeviceUI()
            ui.tableWidget = w_table
            ui.row = row
            ui.col = 2
            devs[row].ui = ui
        #w_table.repaint()

    def add_plot_matplotlib(self):

        #fig = plt.figure()#(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)
        #self.axes = plt.plot([1,2,3,4])
        ##self.compute_initial_figure()
        #
        #FigureCanvas.__init__(self, fig)
        ##self.setParent(parent)
        #
        #FigureCanvas.setSizePolicy(self,
        #                           QtGui.QSizePolicy.Expanding,
        #                           QtGui.QSizePolicy.Expanding)
        #FigureCanvas.updateGeometry(self)
        # a figure instance to plot on
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)
        self.axes.plot([1,2,3])
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)
        # set the layout
        layout = QtGui.QVBoxLayout()

        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        self.ui.widget_2.setLayout(layout)

    def plot_lat(self, plot_wdg, types):
        self.plot2.clear()
        r_items = []
        L = 0.
        for elem in self.lat.sequence:
            a = 1
            L += elem.l
            if elem.__class__ in types:
                s = L - elem.l
                r1 = pg.QtGui.QGraphicsRectItem(s, 0, elem.l, 1)#10*elem.k1/self.quad_ampl)
                #print()
                #color = QtGui.QColor(164, 230, 10)
                #pen = pg.mkPen(color, width=1)
                r1.setPen(pg.mkPen(None))
                r1.setBrush(pg.mkBrush("g"))
                r1.init_params = [s, 0, elem.l, 1] #*elem.k1/self.quad_ampl]
                r_items.append(r1)
                plot_wdg.addItem(r1)
        plot_wdg.update()
        return r_items
        #print(self.plot2.items())

    def zoom_signal(self):
        s = self.plot1.viewRange()[0][0]
        s_pos = np.array([q.s_pos for q in self.quads])
        indx = np.argwhere(s_pos>s)[0][0]
        row = self.quads[indx].ui.row
        #self.ui.tableWidget.scrollTo(row)
        item = self.ui.tableWidget.item(row, 2)
        self.ui.tableWidget.scrollToItem(item, QtGui.QAbstractItemView.PositionAtBottom)
        self.ui.tableWidget.selectRow(row)


    def add_plot(self):
        #self.plot1 = pg.PlotWidget(title="Objective Function Monitor",
        #                           labels={'left': str("adsfasf"), 'bottom': "Time (seconds)"})
        #self.ui.verticalLayout_5.setSpacing(0)
        #self.ui.verticalLayout_5.setMargin(0)
        #self.ui.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        #self.ui.verticalLayout_5.setVerticalSpacing(0)
        #self.ui.verticalLayout_5.insertStretch(-1, 1)


        #win = pg.GraphicsWindow()
        win = pg.GraphicsLayoutWidget()
        #win = pg.GraphicsView()
        #gl = pg.GraphicsLayout(border=(100,100,100))
        #w.ci.layout.setRowMaximumHeight(1, 200)
        #gl.setLayout()
        #win.setCentralItem(gl)

        #win.setWindowTitle('pyqtgraph example: crosshair')
        #print(win.size())
        #label = pg.LabelItem(justify='right')
        #win.addItem(label)
        #l2 = gl.addLayout(rowspan=3, border=(50, 0, 0))
        self.plot3 = win.addPlot(row=0, col=0)
        win.ci.layout.setRowMaximumHeight(0, 200)

        self.plot3.showGrid(1, 1, 1)


        self.plot1 = win.addPlot(row=1, col=0)
        self.plot3.setXLink(self.plot1)
        # gl.nextRow()

        #l3 = gl.addLayout(rowspan=1, border=(10, 0, 0))
        #self.plot2 = gl.addPlot(row=5, col=0, rowspan=1)
        #print(self.plot1.resize(800, 400))
        #self.plot2 = win.addPlot(row=2, col=0, rowspan=2)
        self.plot1.showGrid(1, 1, 1)

        self.plot1.getAxis('left').enableAutoSIPrefix(enable=False)  # stop the auto unit scaling on y axes
        layout = QtGui.QGridLayout()
        self.ui.widget_2.setLayout(layout)
        layout.addWidget(win, 0, 0)
        #layout.addWidget(win, 0, 0)

        #region = pg.LinearRegionItem()
        #region.setZValue(10)
        # Add the LinearRegionItem to the ViewBox, but tell the ViewBox to exclude this
        # item when doing auto-range calculations.
        #self.plot2.addItem(region, ignoreBounds=True)

        # pg.dbg()
        self.plot1.setAutoVisible(y=True)

        #self.plot1.showGrid(1, 1, 1)
        #self.plot1.getAxis('left').enableAutoSIPrefix(enable=False)  # stop the auto unit scaling on y axes
        #layout = QtGui.QGridLayout()
        #self.ui.widget_2.setLayout(layout)
        #layout.addWidget(self.plot1, 0, 0)

        self.plot1.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.beta_x = pg.PlotCurveItem(x=[], y=[], pen=pen, name='beta_x', antialias=True)
        self.plot1.addItem(self.beta_x)

        pen = pg.mkPen(color, width=1)
        self.beta_x_des = pg.PlotCurveItem(x=[], y=[], pen=pen, name='beta_x', antialias=True)
        self.plot1.addItem(self.beta_x_des)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=3)
        self.beta_y = pg.PlotCurveItem(x=[], y=[], pen=pen, name='beta_y', antialias=True)
        self.plot1.addItem(self.beta_y)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=1)
        self.beta_y_des = pg.PlotCurveItem(x=[], y=[], pen=pen, name='beta_y', antialias=True)
        self.plot1.addItem(self.beta_y_des)

        self.plot2 = win.addPlot(row=2, col=0)
        win.ci.layout.setRowMaximumHeight(2, 150)

        #self.plot2.showAxis('left', False)
        #self.plot2.showAxis('bottom', False)
        self.plot2.setXLink(self.plot1)
        self.plot2.showGrid(1, 1, 1)

        self.plot3.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.Dx = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Dx', antialias=True)
        self.plot3.addItem(self.Dx)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=3)
        self.Dy = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Dy', antialias=True)
        self.plot3.addItem(self.Dy)
        self.plot2.sigRangeChanged.connect(self.zoom_signal)




    def update_plot(self, s, bx, by, dx, dy):
        # Line
        self.beta_x.setData(x=s, y=bx)
        self.beta_y.setData(x=s, y=by)
        self.plot1.update()
        self.plot2.update()
        self.Dx.setData(x=s, y=dx)
        self.Dy.setData(x=s, y=dy)
        self.plot3.update()


    def loadStyleSheet(self):
        """ Sets the dark GUI theme from a css file."""
        try:
            self.cssfile = "style.css"
            with open(self.cssfile, "r") as f:
                self.setStyleSheet(f.read())
        except IOError:
            print ('No style sheet found!')







def main():


    #make pyqt threadsafe
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_X11InitThreads)
    #create the application
    app    = QApplication(sys.argv)


    window = ManulInterfaceWindow()


    #show app
    window.setWindowIcon(QtGui.QIcon('manul.png'))
    window.show()

    #Build documentaiton if source files have changed
    # TODO: make more universal
    #os.system("cd ./docs && xterm -T 'Ocelot Doc Builder' -e 'bash checkDocBuild.sh' &")
    #exit script
    sys.exit(app.exec_())

if __name__ == "__main__":

    main()
"""
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np

win = pg.plot()
win.setWindowTitle('pyqtgraph example: FillBetweenItem')
win.setXRange(-10, 10)
win.setYRange(-10, 10)

N = 200
x = np.linspace(-10, 10, N)
gauss = np.exp(-x ** 2 / 20.)
mn = mx = np.zeros(len(x))
curves = [win.plot(x=x, y=np.zeros(len(x)), pen='k') for i in range(4)]
brushes = [0.5, (100, 100, 255), 0.5]
fills = [pg.FillBetweenItem(curves[i], curves[i + 1], brushes[i]) for i in range(3)]
for f in fills:
    win.addItem(f)


def update():
    global mx, mn, curves, gauss, x
    a = 5 / abs(np.random.normal(loc=1, scale=0.2))
    y1 = -np.abs(a * gauss + np.random.normal(size=len(x)))
    y2 = np.abs(a * gauss + np.random.normal(size=len(x)))

    s = 0.01
    mn = np.where(y1 < mn, y1, mn) * (1 - s) + y1 * s
    mx = np.where(y2 > mx, y2, mx) * (1 - s) + y2 * s
    curves[0].setData(x, mn)
    curves[1].setData(x, y1)
    curves[2].setData(x, y2)
    curves[3].setData(x, mx)


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(30)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
"""
