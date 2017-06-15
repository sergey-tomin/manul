"""
Sergey Tomin, XFEL/DESY, 2017
"""
import numpy as np
from devices import *
import time
import pyqtgraph as pg
from PyQt4 import QtGui, QtCore


class DispertionInterface:
    def __init__(self, parent):
        self.ui = parent.ui
        self.parent = parent
        self.ui.pb_start_meas.clicked.connect(self.dispersion_measurement)
        self.add_orbit_plot()
        self.ui.cb_cav_list.addItem("A1")
        self.ui.cb_cav_list.addItem("A2")
        self.ui.cb_cav_list.addItem("A3")
        self.ui.cb_cav_list.addItem("A4")
        self.ui.cb_cav_list.addItem("A5")

        self.ui.cb_cav_list.addItem("A6")
        self.ui.cb_cav_list.addItem("A7")
        self.ui.cb_cav_list.addItem("A8")
        self.ui.cb_cav_list.addItem("A9")
        self.ui.cb_cav_list.addItem("A10")
        self.ui.cb_cav_list.addItem("A11")
        self.ui.cb_cav_list.addItem("A12")
        self.ui.cb_cav_list.addItem("A13")
        self.ui.cb_cav_list.addItem("A14")
        self.ui.cb_cav_list.addItem("A15")
        self.ui.cb_cav_list.addItem("A16")
        self.ui.cb_cav_list.addItem("A17")
        self.ui.cb_cav_list.addItem("A18")
        self.ui.cb_cav_list.addItem("A19")
        self.ui.cb_cav_list.addItem("A20")
        self.ui.cb_cav_list.addItem("A21")
        self.ui.cb_cav_list.addItem("A22")
        self.ui.cb_cav_list.addItem("A23")
        self.ui.cb_cav_list.addItem("A24")
        self.ui.cb_cav_list.addItem("A25")

    def read_bpms(self, bpms):
        """
        Method to read bpms

        :param bpms: list of the bpm objects
        :return: X, Y, bpm_list - List of the X and Y beam positions in [m] and list of the bpm names
        """
        x = []
        y = []
        bpm_list = []
        for bpm in bpms:
            x_mm, y_mm = bpm.mi.get_pos()
            charge = bpm.mi.get_charge()
            bpm_list.append(bpm.id)
            x.append(x_mm * 1000)
            y.append(y_mm * 1000)
        return np.array(x), np.array(y), bpm_list

    def get_orbit(self, bpms):
        n_readings = self.ui.n_readings.value()
        n_bpms = len(bpms)
        X = np.zeros(n_bpms)
        Y = np.zeros(n_bpms)
        for n in range(n_readings):
            x, y, bpm_list = self.read_bpms(bpms)
            X = np.vstack((X, x))
            Y = np.vstack((Y, y))
            time.sleep(0.11)
        s_bpm = np.array([bpm.s for bpm in bpms])
        x_mean = np.mean(X, axis=0)
        y_mean = np.mean(Y, axis=0)
        x_std = np.std(x, axis=0)
        y_std = np.std(y, axis=0)
        return x_mean, y_mean, x_std, y_std

    def get_section_energy(self):
        return 13200 # MeV

    def dispersion_measurement(self):
        time_delay = self.ui.sb_time_delay.value()

        current_cav = self.ui.cb_cav_list.currentText()
        cav_id = "CTRL." + current_cav + ".I1"
        self.cavity = CavityA1(eid=cav_id)
        self.cavity.mi = self.parent.mi

        V_init = self.cavity.get_value()

        dV = self.ui.sb_voltage.value()
        n_steps = self.ui.sb_n_steps.value()
        bpms = self.parent.orbit.bpms
        bpms = self.parent.orbit.get_dev_from_cb_state(bpms)

        disp_orbit = {}

        x_mean_i, y_mean_i, x_std_i, y_std_i = self.get_orbit(bpms)

        for n in range(n_steps):
            self.cavity.set_value(V_init + dV*(n + 1))
            time.sleep(time_delay)
            x_mean, y_mean, x_std, y_std = self.get_orbit(bpms)

        energy = self.get_section_energy()
        Dx = (x_mean - x_mean_i) / (dV * n_steps) * energy
        Dy = (y_mean - y_mean_i) / (dV * n_steps) * energy
        s_bpm = np.array([bpm.s for bpm in bpms])

        self.cavity.set_value(V_init)

        self.plot_dispersion(s_bpm, Dx, Dy)

    def add_orbit_plot(self):
        win = pg.GraphicsLayoutWidget()
        self.plot_x = win.addPlot(row=0, col=0)
        axis = self.plot_x.getAxis("bottom")
        axis.setStyle(showValues=False)
        # win.ci.layout.setRowMaximumHeight(0, 200)
        self.plot_x.showGrid(1, 1, 1)

        self.plot_y = win.addPlot(row=1, col=0)
        axis = self.plot_y.getAxis("bottom")
        axis.setStyle(showValues=False)

        self.plot_x.setXLink(self.plot_y)
        #self.plot_x.hideAxis("bottom")

        self.plot_y.showGrid(1, 1, 1)

        self.plot_y.getAxis('left').enableAutoSIPrefix(enable=False)  # stop the auto unit scaling on y axes
        layout = QtGui.QGridLayout()

        self.ui.w_disp.setLayout(layout)
        layout.addWidget(win, 0, 0)

        self.plot_y.setAutoVisible(y=True)

        self.plot_y.addLegend()

        #color = QtGui.QColor(0, 255, 255)
        #pen = pg.mkPen(color, width=3)
        #self.orb_y = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Y calc', antialias=True)
        #self.plot_y.addItem(self.orb_y)
        #


        #color = QtGui.QColor(255, 255, 0)
        #pen = pg.mkPen(color, width=3)
        #self.orb_y_golden = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Y golden', antialias=True)

        #color = QtGui.QColor(0, 255, 0)
        #pen = pg.mkPen(color, width=2)
        #self.orb_y_live = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Y live', antialias=True)

        self.plot_Dx = win.addPlot(row=2, col=0)
        axis = self.plot_Dx.getAxis("bottom")
        axis.setStyle(showValues=False)
        self.plot_Dy = win.addPlot(row=3, col=0)

        self.plot_Dy.showGrid(1, 1, 1)
        self.plot_Dy.setXLink(self.plot_y)
        #win.ci.layout.setRowMaximumHeight(2, 150)

        self.plot_Dx.setXLink(self.plot_y)
        self.plot_Dx.showGrid(1, 1, 1)

        #color = QtGui.QColor(255, 0, 0)
        #pen = pg.mkPen(color, width=3)
        #
        #self.orb_x0 = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Y', antialias=True)
        #self.plot_x.addItem(self.orb_x0)
        #
        #self.orb_y = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Y', antialias=True)
        #self.plot_y.addItem(self.orb_y0)
        #
        #color = QtGui.QColor(0, 255, 255)
        #pen = pg.mkPen(color, width=3)
        #
        #self.orb_x1 = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Y', antialias=True)
        #self.plot_x.addItem(self.orb_x1)
        #
        #self.orb_y1 = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Y', antialias=True)
        #self.plot_y.addItem(self.orb_y1)

        #self.plot_Dx.addItem(pg.InfiniteLine(pos=62.09, angle=90, movable=False), ignoreBounds=True)
        #lh_t = pg.TextItem("I1", anchor=(0, 0))
        #lh_t.setPos(62.09, 0)
        #self.plot_cor.addItem(lh_t, ignoreBounds=True)


        self.plot_Dx.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.Dx_curve = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Dx', antialias=True)
        self.plot_Dx.addItem(self.Dx_curve)

        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3, symbolPen='o')
        self.Dy_curve = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Dy', antialias=True)
        self.plot_Dy.addItem(self.Dy_curve)

    def plot_orbits(self):
        pass

    def plot_dispersion(self, s, Dx, Dy):
        s = s + self.parent.lat_zi
        self.Dx_curve.setData(x=s, y=Dx)
        self.Dy_curve.setData(x=s, y=Dy)
        self.Dx_curve.update()
        self.Dy_curve.update()


    def dispersion_measurement_sim(self):
        self.create_Orbit_obj()
        disp_meas = LinacDisperseSimRM(lattice=copy.deepcopy(self.orbit.lat),
                                       hcors=copy.deepcopy(self.orbit.hcors),
                                    vcors=copy.deepcopy(self.orbit.vcors),
                                       bpms=copy.deepcopy(self.orbit.bpms))

        Dx0, Dy0 = disp_meas.read_virtual_dispersion(E0=self.parent.tws0.E)

        #print(Dx0)
        n_meas = 5
        x = np.zeros(len(self.orbit.bpms))
        y = np.zeros(len(self.orbit.bpms))
        for i in range(n_meas):
            for i, elem in enumerate(self.orbit.bpms):
                x_mm, y_mm = elem.mi.get_pos()
                x[i] += x_mm
                y[i] += y_mm
            time.sleep(0.2)
        x = x/n_meas
        y = y/n_meas

        V0 = self.cavity.get_value()
        dV = self.ui.sb_dV.value()
        V = V0 + dV
        self.cavity.set_value(V)
        time.sleep(4)
        x1 = np.zeros(len(self.orbit.bpms))
        y1 = np.zeros(len(self.orbit.bpms))
        for i in range(n_meas):
            for i, elem in enumerate(self.orbit.bpms):
                x_mm, y_mm = elem.mi.get_pos()
                x1[i] += x_mm
                y1[i] += y_mm
            time.sleep(0.2)
        x1 = x1 / n_meas
        y1 = y1 / n_meas
        dx = (x1 - x) / dV
        dy = (y1 - y) / dV

        for i, elem in enumerate(self.orbit.bpms):
            elem.Dx = dx[i]/1000
            elem.Dy = dy[i]/1000
            elem.Dx_des = Dx0[i]
            elem.Dy_des = Dy0[i]

        s_bpm = np.array([bpm.s for bpm in self.orbit.bpms]) + self.parent.lat_zi
        #x_bpm = np.array([bpm.Dx for bpm in self.orbit.bpms])*1000
        self.orb_x_ref.setData(x=s_bpm, y=dx)
        self.orb_x.setData(x=s_bpm, y=Dx0)
        self.orb_y_ref.setData(x=s_bpm, y=dy)
        self.orb_y.setData(x=s_bpm, y=Dy0)

        #self.plot_cor.update()
        self.orb_y.update()
        self.orb_x.update()