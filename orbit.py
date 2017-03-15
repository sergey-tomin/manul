
import pyqtgraph as pg
from PyQt4 import QtGui, QtCore
import numpy as np
from ocelot import *
from ocelot.optimizer.mint.opt_objects import Device
from ocelot.cpbd.track import *
class BPM(Device):

    def get_pos(self):
        ch_x = "XFEL.DIAG/BPM/" + self.eid + "/X.SA1"
        ch_y = "XFEL.DIAG/BPM/" + self.eid + "/Y.SA1"
        x = self.mi.get_value(ch_x)
        y = self.mi.get_value(ch_y)
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
        self.add_orbit_plot()
        self.ui.pb_check.clicked.connect(lambda: self.getRows(2))
        self.ui.pb_uncheck.clicked.connect(lambda: self.getRows(0))
        self.ui.pb_read_orbit.clicked.connect(self.read_orbit)

        #self.ui.cb_coupler_kick.stateChanged.connect(self.calc_orbit)

    #def return_lattice(self):
    #    self.load_lattice()
    #    self.calc_twiss()

    def read_orbit(self):
        self.online_calc = False
        for elem in self.corrs:
            elem.kick_mrad = elem.mi.get_value()
            angle = elem.kick_mrad*1e-3
            elem.k1 = angle
            elem.i_kick = elem.kick_mrad
            #print(elem.i_kick)
            elem.ui.set_init_value(elem.kick_mrad)
            elem.ui.set_value(elem.kick_mrad)
        self.online_calc = True
        self.parent.lat.update_transfer_maps()
        for elem in self.bpms:
            x, y = elem.mi.get_pos()
            elem.x_pos = x
            elem.y_pos = y

        #self.tws0 = self.back_tracking()
        #print("back_tracking = ", self.tws0)
        #tws = twiss(self.lat, self.tws0)
        #beta_x = [tw.beta_x for tw in tws]
        #beta_y = [tw.beta_y for tw in tws]
        #dx = [tw.Dx for tw in tws]
        #dy = [tw.Dy for tw in tws]
        #s = [tw.s for tw in tws]
        s_bpm = np.array([bpm.s_pos for bpm in self.bpms])
        x_bpm = np.array([bpm.x_pos for bpm in self.bpms])
        y_bpm = np.array([bpm.y_pos for bpm in self.bpms])
        self.update_plot(s=[], x=[], y=[], s_bpm=s_bpm, x_ref=x_bpm, y_ref=y_bpm)

    def calc_orbit(self):
        #lat = MagneticLattice(cell)
        if self.online_calc == False:
            return

        # L = 0
        for elem in self.parent.lat.sequence:
            if elem.__class__ in [Hcor, Vcor]:
                #print(elem.id, elem.row)
                elem.kick_mrad = elem.ui.get_value()
                elem.angle = elem.kick_mrad/1000.
                if np.abs(np.abs(elem.kick_mrad) - np.abs(elem.i_kick))> 0.01:
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

        self.parent.lat.update_transfer_maps()
        #print("test")
        # exit(0)
        p_list = lattice_track(self.parent.lat, Particle(E=self.parent.tws0.E))
        #tws = twiss(self.lat, self.tws0)
        #print(tws[-1], self.tws0)
        #plot_opt_func(lat, tws, top_plot=["Dx", "Dy"])
        #plt.show()
        x = np.array([p.x for p in p_list])*1000
        y = np.array([p.y for p in p_list])*1000
        #dx = [p.Dx for p in p_list]
        #dy = [p.Dy for p in p_list]
        s = [p.s for p in p_list]

        self.update_plot(s, x, y, s_bpm=[], x_ref=[], y_ref=[])

    def load_bpms(self, lat):
        devices = []
        L = 0
        for elem in lat.sequence:
            L += elem.l
            if elem.__class__ in [Monitor]:
                elem.s_pos = L - elem.l/2.
                devices.append(elem)

                mi_dev = BPM(eid=elem.id)
                mi_dev.mi = self.parent.mi
                elem.mi = mi_dev

        return devices

    def load_correctors(self):

        self.corrs = self.parent.load_devices(types=[Hcor, Vcor])

        self.parent.add_devs2table(self.corrs, w_table=self.ui.table_cor, calc_obj=self.calc_orbit,
                                   spin_params=[-100, 100, 0.1], check_box=True)
        self.cor_ampl = np.max(np.append(1, np.abs(np.array([q.kick_mrad for q in self.corrs]))))

    def load_orbit_devs(self):
        self.bpms = self.load_bpms(lat=self.parent.lat)
        self.load_correctors()

        self.r_items = self.parent.plot_lat(plot_wdg=self.plot_cor, types=[Hcor, Vcor])

    def load_devices(self, types):
        devices = []
        mi_devs = {}
        #cell_i1_copy = copy.deepcopy(cell_i1_copy)
        #lat_tmp = MagneticLattice(cell_i1_copy)

        L = 0
        for elem in self.parent.lat.sequence:
            L += elem.l
            if elem.__class__ in types:
                elem.s_pos = L - elem.l/2.
                elem.kick_mrad = elem.angle* 1000.
                elem.i_kick = elem.kick_mrad
                devices.append(elem)
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
        pen = pg.mkPen(color, width=1)
        self.orb_y_ref = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Y ref', antialias=True)
        self.plot_y.addItem(self.orb_y_ref)

        self.plot_cor = win.addPlot(row=2, col=0)
        win.ci.layout.setRowMaximumHeight(2, 150)

        self.plot_cor.setXLink(self.plot_y)
        self.plot_cor.showGrid(1, 1, 1)

        self.plot_x.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.orb_x = pg.PlotCurveItem(x=[], y=[], pen=pen, name='X', antialias=True)
        self.plot_x.addItem(self.orb_x)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=1)
        self.orb_x_ref = pg.PlotCurveItem(x=[], y=[], pen=pen, name='X ref', antialias=True)
        self.plot_x.addItem(self.orb_x_ref)
        self.plot_cor.sigRangeChanged.connect(self.zoom_signal)
        self.plot_cor.setYRange(-3, 3)
        self.plot_x.setYRange(-5, 5)
        self.plot_y.setYRange(-5, 5)

    def zoom_signal(self):
        if len(self.corrs) == 0:
            return
        s = self.plot_y.viewRange()[0][0]
        s_pos = np.array([q.s_pos for q in self.corrs])
        indx = np.argwhere(s_pos>s)[0][0]
        row = self.corrs[indx].ui.row
        #self.ui.tableWidget.scrollTo(row)
        item = self.ui.tableWidget.item(row, 2)
        self.ui.tableWidget.scrollToItem(item, QtGui.QAbstractItemView.PositionAtBottom)
        self.ui.tableWidget.selectRow(row)

    def update_plot(self, s, x, y, s_bpm, x_ref, y_ref):
        # Line
        self.orb_x_ref.setData(x=s_bpm, y=x_ref)
        self.orb_x.setData(x=s, y=x)
        self.orb_y_ref.setData(x=s_bpm, y=y_ref)
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