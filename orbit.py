"""
Sergey Tomin. XFEL/DESY, 2017.
"""

import pyqtgraph as pg
from PyQt4 import QtGui, QtCore
import numpy as np
from ocelot import *
from ocelot.optimizer.mint.opt_objects import Device
from ocelot.cpbd.track import *

from ocelot.cpbd.orbit_correction import *

class BPMUI:
    def __init__(self, ui=None):
        self.tableWidget = None
        self.row = 0
        self.col = 0

    def get_value(self):
        x = float(self.tableWidget.item(self.row, 1).text())
        y = float(self.tableWidget.item(self.row, 2).text())
        return (x, y)

    def set_value(self, val):
        x = val[0]
        y = val[1]
        self.tableWidget.item(self.row, 1).setText(str(x))
        self.tableWidget.item(self.row, 2).setText(str(y))
        self.check_values(val)

    def check_values(self, val):
        if np.max(np.abs(val)) > 15.:
            self.tableWidget.item(self.row, 1).setBackground(QtGui.QColor(255, 0, 0))  # red
            self.tableWidget.item(self.row, 2).setBackground(QtGui.QColor(255, 0, 0))  # red

        else:
            self.tableWidget.item(self.row, 1).setBackground(QtGui.QColor(89, 89, 89))  # grey
            self.tableWidget.item(self.row, 2).setBackground(QtGui.QColor(89, 89, 89))  # grey

    def set_init_value(self, val):
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


class BPM(Device):

    def get_pos(self):
        ch_x = "XFEL.DIAG/BPM/" + self.eid + "/X.SA1"
        ch_y = "XFEL.DIAG/BPM/" + self.eid + "/Y.SA1"
        print(ch_x, ch_y)
        x = self.mi.get_value(ch_x)
        y = self.mi.get_value(ch_y)
        print(x, y)
        return x, y


class OrbitInterface:
    def __init__(self, parent):
        self.parent = parent
        self.ui = parent.ui
        self.online_calc = True
        #self.corrs = self.parent.load_devices(types=[Vcor, Hcor])
        #self.parent.add_devs2table(devs=self.corrs, w_table=self.ui.table_cor )
        #self.add_orbit_plot()
        self.corrs = []
        self.hcors = []
        self.vcors = []
        self.s_bpm = []
        self.x_bpm = []
        self.y_bpm = []
        self.p_init = None
        self.add_orbit_plot()
        self.ui.pb_check.clicked.connect(lambda: self.getRows(2))
        self.ui.pb_uncheck.clicked.connect(lambda: self.getRows(0))
        self.ui.pb_read_orbit.clicked.connect(self.read_orbit)

        self.ui.pb_apply_kicks.clicked.connect(self.apply_kicks)

        self.ui.pb_calc_misal.clicked.connect(self.calc_misalignment_rm)
        self.ui.pb_calc_RM.clicked.connect(self.response_matrix)
        self.ui.pb_correct_orbit.clicked.connect(self.correct)
        self.ui.pb_reset_all.clicked.connect(self.reset_all)
        #self.ui.table_bpm.itemChanged.connect(self.update_plot)

        #self.ui.cb_coupler_kick.stateChanged.connect(self.calc_orbit)
        #self.loadStyleSheet()

    #def loadStyleSheet(self):
    #    """ Load in the dark theme style sheet. """
    #    try:
    #        self.cssfile = "style.css"
    #        with open(self.cssfile, "r") as f:
    #            self.setStyleSheet(f.read())
    #    except IOError:
    #        print('No style sheet found!')
    #def return_lattice(self):
    #    self.load_lattice()
    #    self.calc_twiss()
    def reset_all(self):
        corrs = self.get_dev_from_cb_state(self.corrs)
        for cor in corrs:
            kick_mrad = cor.ui.get_init_value()
            cor.ui.set_value(kick_mrad)

    def apply_kicks(self):
        corrs = self.get_dev_from_cb_state(self.corrs)
        for cor in corrs:

            kick_mrad = cor.ui.get_value()
            print( cor.id," set: ", cor.ui.get_init_value(), "-->", kick_mrad)
            if -2.5 <= kick_mrad <=2.5:
                cor.mi.set_value(kick_mrad)

    def intro_misal(self):
        #lat = MagneticLattice(cell)

        for elem in self.parent.lat.sequence:
            if elem.id == 'CKX.23.I1':
                elem.angle = 0.1*0.001
            if elem.id == 'CKX.24.I1':
                elem.angle = -0.2 * 0.001
            #if elem.__class__ == Quadrupole:
            #    elem.dx = np.random.normal(0, 200e-6)
            #    elem.dx = np.random.normal(0, 200e-6)
        self.parent.lat.update_transfer_maps()

    def read_traj(self):
        self.orbit = Orbit(self.parent.lat)
        X0, Y0 = self.orbit.read_virtual_orbit(p_init=Particle(x=0.00, y=-0.00, px=0.000, E=self.parent.tws0.E))
        #for elem in self.bpms:
        #    elem.x_mm = elem.x * 1000
        #    elem.y_mm = elem.y * 1000

    def read_orbit_sim(self):
        self.intro_misal()
        self.read_traj()
        self.online_calc = False
        for elem in self.corrs:
            elem.kick_mrad = elem.angle*1000.
            #angle = elem.kick_mrad*1e-3
            elem.angle = 0.
            elem.angle_read = elem.kick_mrad*1e-3
            elem.i_kick = elem.kick_mrad
            #print(elem.id, elem.angle)
            elem.ui.set_init_value(elem.kick_mrad)
            elem.ui.set_value(elem.kick_mrad)
        self.online_calc = True
        self.parent.lat.update_transfer_maps()
        for elem in self.bpms:
            try:
                x_mm, y_mm = elem.x*1000, elem.y*1000
                print(elem.id, x_mm, y_mm)
                elem.x = x_mm/1000.
                elem.y = y_mm/1000.
                elem.ui.set_value((x_mm, y_mm))
            except:
                print("deleted BPM", elem.id)
                self.bpms.remove(elem)
        #self.update_plot(self.s_bpm = np.array([bpm.s for bpm in self.bpms])
        #self.x_bpm = np.array([bpm.x_mm for bpm in self.bpms])
        #self.y_bpm = np.array([bpm.y_mm for bpm in self.bpms])
        #self.update_plot(s=[], x=[], y=[], s_bpm=self.s_bpm, x_ref=self.x_bpm, y_ref=self.y_bpm)

        self.update_plot()


    def read_orbit(self):
        self.online_calc = False
        for elem in self.corrs:
            elem.kick_mrad = elem.mi.get_value()
            #angle = elem.kick_mrad*1e-3
            #elem.angle = elem.kick_mrad*1e-3
            elem.angle_read = elem.kick_mrad*1e-3
            elem.i_kick = elem.kick_mrad
            #print(elem.id, elem.angle)
            elem.ui.set_init_value(elem.kick_mrad)
            elem.ui.set_value(elem.kick_mrad)
        self.online_calc = True
        self.parent.lat.update_transfer_maps()
        for elem in self.bpms:
            try:
                x_mm, y_mm = elem.mi.get_pos()
                elem.x = x_mm/1000.
                elem.y = y_mm/1000.
                elem.ui.set_value((x_mm, y_mm))
            except:
                print("deleted BPM", elem.id)
                self.bpms.remove(elem)

        self.update_plot()

    def calc_orbit(self):
        #lat = MagneticLattice(cell)
        if self.online_calc == False:
            return

        # L = 0
        start = time()
        for elem in self.parent.lat.sequence:
            if elem.__class__ in [Hcor, Vcor]:
                #print(elem.id, elem.row)
                elem.kick_mrad = elem.ui.get_value()
                kick_mrad_i = elem.ui.get_init_value()
                angle = (elem.kick_mrad - kick_mrad_i)/1000.
                elem.angle = angle # elem.kick_mrad/1000.
                if np.abs(np.abs(elem.kick_mrad) - np.abs(elem.i_kick))> 0.001:
                    self.r_items[elem.ui.row].setBrush(pg.mkBrush("r"))
                    self.ui.table_cor.item(elem.row, 1).setForeground(QtGui.QColor(255, 101, 101))  # red
                else:
                    self.ui.table_cor.item(elem.row, 1).setForeground(QtGui.QColor(255, 255, 255))  # white
                    self.r_items[elem.ui.row].setBrush(pg.mkBrush("g"))
                r = self.r_items[elem.ui.row]
                sizes = r.init_params
                #sizes = list(r.boundingRect().getRect())
                sizes[3] = elem.kick_mrad/self.cor_ampl
                r.setRect(sizes[0]-0.1, sizes[1], sizes[2]+0.1, sizes[3])
        print("1 = ", start - time())
        start = time()
        self.parent.lat.update_transfer_maps()
        print("2 = ", start - time())
        #print("test")
        # exit(0)
        #if self.p_init == None:


        self.update_plot()
        #self.update_plot(s, x, y, s_bpm=self.s_bpm, x_ref=self.x_bpm, y_ref=self.y_bpm)

    def correct(self):
        #for bpm in self.bpms:
        #    bpm.x = bpm.x_mm/1000
        #    bpm.y = bpm.y_mm/1000
        p0 = Particle(E=self.parent.tws0.E)
        for cor in self.corrs:
            cor.angle = 0.
        self.orbit.correction(p_init=p0)
        self.online_calc = False
        for cor in self.corrs:
           print("fin = ",  cor.angle, cor.id, cor)
           kick_mrad_old = cor.ui.get_value()
           delta_kick_mrad = cor.angle*1000
           new_kick_mrad = kick_mrad_old + delta_kick_mrad
           cor.kick_mrad =  new_kick_mrad # cor.angle*1000
           cor.ui.set_value(cor.kick_mrad)
        self.online_calc = True

        self.calc_orbit()

    #def get_correctors(self):
    #    pvs = self.getPvsFromCbState()
    #    corrs = self.get_devices(pvs)
    #    return corrs

    #def get_devices(self, pvs):
    #    d_pvs = [dev.id for dev in self.corrs]
    #    inxs = [d_pvs.index(pv) for pv in pvs]
    #    return [self.corrs[inx] for inx in inxs]

    def get_dev_from_cb_state(self, devs):

        """
        Gets list of all pvs that have checked boxes.

        Returns:
                List of PV strings
        """
        checked_devs = []
        for dev in devs:
            state = dev.ui.state()
            #print(dev.id, state)
            if state == 2:
                checked_devs.append(dev)
        return checked_devs

    def response_matrix(self):
        for elem in self.corrs:
            print("angle = ", elem.angle)
        #print("response")
        self.orbit = Orbit(self.parent.lat, empty=True)

        #corrs = self.get_correctors()
        corrs = self.get_dev_from_cb_state(self.corrs)
        print("correctors" , corrs)
        s_pos = np.min([cor.s for cor in corrs])
        self.bpms = np.array(self.bpms)
        print([bpm.id for bpm in self.bpms])
        bpms = self.bpms[np.array([bpm.s for bpm in self.bpms])>=s_pos]
        bpms = self.get_dev_from_cb_state(bpms)
        print([bpm.id for bpm in bpms])
        #self.orbit.bpms = copy.deepcopy(bpms)
        self.orbit.bpms = bpms
        self.hcors = []
        self.vcors = []
        for cor in corrs:
            #cor = copy.deepcopy(cor)
            if cor.__class__ == Hcor:
                self.hcors.append(cor)
            else:
                self.vcors.append(cor)

        self.orbit.hcors = self.hcors
        self.orbit.vcors = self.vcors
        #print(self.hcors, self.vcors)
        #self.read_orbit()
        print(self.parent.tws0)
        self.rmatrix = self.orbit.linac_response_matrix(tw_init=self.parent.tws0)
        #self.rmatrix = self.orbit.linac_response_matrix_meas(tw_init=self.parent.tws0)
        self.orbit.resp = self.rmatrix.matrix
        return self.rmatrix

    def calc_misalignment_rm(self):
        for elem in self.corrs:
            print("angle = ", elem.angle)
        #self.orbit = Orbit(self.parent.lat, empty=True)

        self.misal_resp_mat = self.orbit.misalignment_rm(p_init=Particle(E=self.parent.tws0.E),
                                   elem_types=[Quadrupole, Bend, SBend,RBend], remove_elem=[])
        #for bpm in self.bpms:
        #    bpm.x = bpm.x_mm/1000
        #    bpm.y = bpm.y_mm/1000
        p = self.orbit.elem_correction(self.misal_resp_mat, elem_types=[Quadrupole, Bend, SBend, RBend], remove_elems=[])
        p.E=self.parent.tws0.E
        self.p_init = p
        self.calc_orbit()

    def create_orbit(self):
        self.orbit = Orbit(self.parent.lat)

        resp_m = self.orbit.misalignment_rm(p_init=Particle(E=self.parent.tws0.E),
                                   elem_types=[Quadrupole, Bend, SBend,RBend], remove_elem=[])
        self.orbit.elem_correction(resp_m, elem_types=[Quadrupole, Bend, SBend,RBend], remove_elems=[])
        self.calc_orbit()

    def func(self):
        pass


    def load_correctors(self):

        self.corrs = self.load_devices(types=[Hcor, Vcor])

        self.parent.add_devs2table(self.corrs, w_table=self.ui.table_cor, calc_obj=self.calc_orbit,
                                   spin_params=[-100, 100, 0.1], check_box=True)
        self.cor_ampl = np.max(np.append(1, np.abs(np.array([q.kick_mrad for q in self.corrs]))))

    def load_bpms(self, lat):
        devices = []
        L = 0
        for i, elem in enumerate(lat.sequence):
            L += elem.l
            if elem.__class__ in [Monitor]:
                elem.s = L - elem.l/2.
                devices.append(elem)

                mi_dev = BPM(eid=elem.id)
                mi_dev.mi = self.parent.mi
                elem.mi = mi_dev
                elem.lat_inx = i
                elem.x = 0
                elem.y = 0
                elem.weight = 1

        return devices

    def add_bpms2table(self, devs, w_table, check_box=False):
        """ Initialize the UI table object """
        #spin_boxes = [QtGui.QDoubleSpinBox()]*
        self.spin_boxes = []
        w_table.setRowCount(0)
        for row in range(len(devs)):
            #eng = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)
            w_table.setRowCount(row + 1)
            pv = devs[row].id
            # put PV in the table
            w_table.setItem(row, 0, QtGui.QTableWidgetItem(str(pv)))
            # put start val in
            w_table.setItem(row, 1, QtGui.QTableWidgetItem(str(devs[row].x)))
            w_table.setItem(row, 2, QtGui.QTableWidgetItem(str(devs[row].y)))

            w_table.resizeColumnsToContents()


            if check_box:
                checkBoxItem = QtGui.QTableWidgetItem()
                # checkBoxItem.setBackgroundColor(QtGui.QColor(100,100,150))
                checkBoxItem.setCheckState(QtCore.Qt.Checked)
                flags = checkBoxItem.flags()
                checkBoxItem.setFlags(flags)
                w_table.setItem(row, 3, checkBoxItem)
                #checkBoxItem.itemChanged.connect(self.calc_orbit)

            devs[row].row = row

            ui = BPMUI()
            ui.tableWidget = w_table
            ui.row = row
            ui.col = 2
            devs[row].ui = ui

    def load_orbit_devs(self):
        self.bpms = self.load_bpms(lat=self.parent.lat)
        self.add_bpms2table(self.bpms, w_table=self.ui.table_bpm, check_box=True)
        self.load_correctors()

        self.r_items = self.parent.plot_lat(plot_wdg=self.plot_cor, types=[Hcor, Vcor])

    def load_devices(self, types):
        devices = []
        mi_devs = {}
        #cell_i1_copy = copy.deepcopy(cell_i1_copy)
        #lat_tmp = MagneticLattice(cell_i1_copy)

        L = 0
        for i, elem in enumerate(self.parent.lat.sequence):
            L += elem.l
            if elem.__class__ in types:
                elem.s = L - elem.l / 2.
                elem.kick_mrad = elem.angle* 1000.
                elem.i_kick = elem.kick_mrad

                elem.lat_inx = i
                #elem.mi = Device(eid="XFEL.MAGNETS/MAGNET.ML/" + elem.id + "/KICK_MRAD.SP")
                if "ps_id" in elem.__dict__:
                    if elem.ps_id not in mi_devs.keys():
                        mi_dev = Device(eid="XFEL.MAGNETS/MAGNET.ML/" + elem.id + "/KICK_MRAD.SP")
                        mi_dev.mi = self.parent.mi
                        elem.mi = mi_dev
                        mi_devs[elem.ps_id] = mi_dev
                    else:
                        elem.mi = mi_devs[elem.ps_id]
                else:
                    mi_dev = Device(eid="XFEL.MAGNETS/MAGNET.ML/" + elem.id + "/KICK_MRAD.SP")
                    mi_dev.mi = self.parent.mi
                    elem.mi = mi_dev
                #print("load ", elem.id)
                if elem.__class__ == Hcor:
                    self.hcors.append(elem)
                elif elem.__class__ == Vcor:
                    self.vcors.append(elem)
                else:
                    print("wrong type")
                devices.append(elem)
        #print(devices)
        #print(self.hcors)
        #print(self.vcors)
        return devices


    def add_orbit_plot(self):
        win = pg.GraphicsLayoutWidget()
        self.plot_x = win.addPlot(row=0, col=0)

        win.ci.layout.setRowMaximumHeight(0, 200)

        self.plot_x.showGrid(1, 1, 1)
        self.plot_y = win.addPlot(row=1, col=0)
        self.plot_x.setXLink(self.plot_y)

        self.plot_y.showGrid(1, 1, 1)

        self.plot_y.getAxis('left').enableAutoSIPrefix(enable=False)  # stop the auto unit scaling on y axes
        layout = QtGui.QGridLayout()
        self.ui.w_orbit.setLayout(layout)
        layout.addWidget(win, 0, 0)

        self.plot_y.setAutoVisible(y=True)

        self.plot_y.addLegend()
        #color = QtGui.QColor(0, 255, 255)
        #pen = pg.mkPen(color, width=3)
        #self.orb_x = pg.PlotCurveItem(x=[], y=[], pen=pen, name='beta_x', antialias=True)
        #self.plot_y.addItem(self.orb_x)

        #pen = pg.mkPen(color, width=1)
        #self.orb_x_ref = pg.PlotCurveItem(x=[], y=[], pen=pen, name='beta_x', antialias=True)
        #self.plot_y.addItem(self.orb_x_ref)

        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.orb_y = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Y', antialias=True)
        self.plot_y.addItem(self.orb_y)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=3)
        #self.orb_y_ref = pg.PlotCurveItem(x=[], y=[], pen=pen, symbol='o', name='Y ref', antialias=True)
        self.orb_y_ref = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='X ref', antialias=True)

        self.plot_y.addItem(self.orb_y_ref)

        self.plot_cor = win.addPlot(row=2, col=0)
        win.ci.layout.setRowMaximumHeight(2, 150)

        self.plot_cor.setXLink(self.plot_y)
        self.plot_cor.showGrid(1, 1, 1)

        self.plot_x.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.orb_x = pg.PlotCurveItem(x=[], y=[], pen=pen,  name='X', antialias=True)
        #self.orb_x = pg.ScatterPlotItem(x=[], y=[], pen=pen, symbol='o', name='X ref', antialias=True)

        self.plot_x.addItem(self.orb_x)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=3, symbolPen='o')
        #self.orb_x_ref = pg.PlotCurveItem(x=[], y=[], pen=pen, symbolPen='w', name='X ref', antialias=True)
        self.orb_x_ref = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='X ref', antialias=True)

        self.plot_x.addItem(self.orb_x_ref)
        self.plot_cor.sigRangeChanged.connect(self.zoom_signal)
        self.plot_cor.setYRange(-3, 3)
        self.plot_x.setYRange(-5, 5)
        self.plot_y.setYRange(-5, 5)

    def zoom_signal(self):
        if len(self.corrs) == 0:
            return
        s = self.plot_y.viewRange()[0][0]
        s_pos = np.array([q.s for q in self.corrs])
        indx = np.argwhere(s_pos>s)[0][0]
        row = self.corrs[indx].ui.row
        #self.ui.tableWidget.scrollTo(row)
        item = self.ui.tableWidget.item(row, 2)
        self.ui.tableWidget.scrollToItem(item, QtGui.QAbstractItemView.PositionAtBottom)
        self.ui.tableWidget.selectRow(row)

    def update_plot(self):

        start = time()
        p_list = lattice_track(self.parent.lat, Particle(E=self.parent.tws0.E))
        print("3 = ", start - time())
        #else:
        #    p_list = lattice_track(self.parent.lat, copy.deepcopy(self.p_init))
        #tws = twiss(self.lat, self.tws0)
        #print(tws[-1], self.tws0)
        #plot_opt_func(lat, tws, top_plot=["Dx", "Dy"])
        #plt.show()
        x = np.array([p.x for p in p_list])*1000
        y = np.array([p.y for p in p_list])*1000
        s = [p.s for p in p_list]

        bpms = self.get_dev_from_cb_state(self.bpms)

        s_bpm = np.array([bpm.s for bpm in bpms])
        x_bpm = np.array([bpm.x for bpm in bpms])*1000
        y_bpm = np.array([bpm.y for bpm in bpms])*1000

        # Line
        self.orb_x_ref.setData(x=s_bpm, y=x_bpm)
        self.orb_x.setData(x=s, y=x)
        self.orb_y_ref.setData(x=s_bpm, y=y_bpm)
        self.orb_y.setData(x=s, y=y)

        self.plot_cor.update()
        self.orb_y.update()
        self.orb_x.update()

    def uncheckBoxes(self):
        """ Method to unchecked all active boxes """
        for cor in self.corrs:
            cor.ui.uncheck()
            # item = self.ui.tableWidget.cellWidget(row, 5)
            #item.setCheckState(False)

    def getRows(self, state):
        """
        Method to set the UI checkbox state from slected rows.

        Loops though the rows and gets the selected state from the 'Active" column.
        If highlighted, check box is set the the 'state' input arg.

        Args:
                state (bool): Bool of whether the boxes should be checked or unchecked.
        """
        rows=[]
        for idx in self.ui.table_cor.selectedIndexes():
            rows.append(idx.row())
            item = self.ui.table_cor.item(idx.row(), 3)
            if item.flags() == QtCore.Qt.NoItemFlags:
                print("item disabled")
                continue
            item.setCheckState(state)