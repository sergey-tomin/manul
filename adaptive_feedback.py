"""
Sergey Tomin, XFEL/DESY, 2017
"""

import numpy as np
import json
from ocelot.optimizer.mint import opt_objects as obj
from PyQt4 import QtGui, QtCore
from scipy import io
import pyqtgraph as pg
from gui.UIadaptive_feedback import Ui_Form
from collections import deque
import time
from threading import Thread, Event

class Statistics(Thread):
    def __init__(self):
        super(Statistics, self).__init__()
        self._stop_event = Event()
        self.do = None
        self.delay = 0.1
    def run(self):
        while 1:
            self.do()
            print("do")
            time.sleep(self.delay)
    def stop(self):
        self._stop_event.set()

class UIAFeedBack(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None, orbit=None):
        QtGui.QWidget.__init__(self, parent)
        #self.paren = main_parent
        #self.ui = self.parent.ui
        self.setupUi(self)
        self.loadStyleSheet()
        self.orbit_class = orbit
        self.parent = self.orbit_class.parent
        self.mi = self.parent.mi
        self.orbit_ui = orbit.ui
        #self.parent = parent
        #self.self_ui = parent.window2
        #self.ui = parent.parent.ui

        #self.Form = parent.parent
        self.golden_orbit = {}

        self.pb_start_feedback.clicked.connect(self.start_stop_feedback)

        self.pb_start_statistics.clicked.connect(self.start_stop_statistics)

        self.orbits_x = []
        self.orbits_y = []
        self.orbit_s = []
        self.target_values = []
        self.nreadings = 100
        self.feedback_timer = pg.QtCore.QTimer()
        self.feedback_timer.timeout.connect(self.calc_golden_orbit)

        self.statistics_timer = pg.QtCore.QTimer()
        self.statistics_timer.timeout.connect(self.loop)

        self.add_orbit_plot()
        self.add_objective_func_plot()
        self.objective_func = None

        self.le_a.textChanged.connect(self.check_address)
        self.le_b.textChanged.connect(self.check_address)
        self.le_c.textChanged.connect(self.check_address)

        self.bpms_name = []

    def loop(self):

        self.read_data()


    def closeEvent(self, QCloseEvent):
        self.feedback_timer.stop()
        self.pb_start_feedback.setStyleSheet("color: rgb(85, 255, 127);")
        self.pb_start_feedback.setText("Start Feedback")
        self.stop_statistics()

    def start_stop_statistics(self):
        """
        Method to start/stop feedback timer.
        sb_feedback_sec - spinBox - set seconds for timer
        pb_feedback - pushBatton Off/On
        feedback_timer - timer
        :return:
        """
        print("I am here")
        delay = self.sb_time_delay.value()*1000
        if self.pb_start_statistics.text() == "Statistics Accum Off":
            self.statistics_timer.stop()
            #self.stat_thread.stop()
            self.pb_start_statistics.setStyleSheet("color: rgb(85, 255, 127);")
            self.pb_start_statistics.setText("Statistics Accum On")
        else:
            self.nreadings = self.sb_array_len.value()
            self.target_values = [] #deque(maxlen=self.nreadings)
            self.orbits_x = []
            self.orbits_y = []
            self.orbit_s = [] #deque(maxlen=self.nreadings)
            self.objective_func = self.set_obj_fun()
            if self.objective_func == None:
                self.stop_statistics()
                return None

            self.statistics_timer.start(delay)
            self.statistics_timer.start()
            self.pb_start_statistics.setText("Statistics Accum Off")
            self.pb_start_statistics.setStyleSheet("color: red")

    def start_stop_feedback(self):
        """
        Method to start/stop feedback timer.
        sb_feedback_sec - spinBox - set seconds for timer
        pb_feedback - pushBatton Off/On
        feedback_timer - timer
        :return:
        """
        print("I am here")
        delay = self.sb_feedback_rep.value()*1000
        if self.pb_start_feedback.text() == "Stop Feedback":
            self.feedback_timer.stop()
            self.pb_start_feedback.setStyleSheet("color: rgb(85, 255, 127);")
            self.pb_start_feedback.setText("Start Feedback")
        else:
            self.feedback_timer.start(delay)
            self.pb_start_feedback.setText("Stop Feedback")
            self.pb_start_feedback.setStyleSheet("color: red")

    def read_bpms(self):
        charge_thresh = 0.005
        beam_on = True
        orbit_x = []
        orbit_y = []
        orbit_s = []
        self.bpms_name = []
        for elem in self.orbit_class.bpms:
            try:
                x_mm, y_mm = elem.mi.get_pos()
                charge = elem.mi.get_charge()
                if charge < charge_thresh:
                    beam_on = False
                x = x_mm / 1000.
                y = y_mm / 1000.
                orbit_x.append(x) #[elem.s, x, y])
                orbit_y.append(y)
                orbit_s.append(elem.s)
                self.bpms_name.append(elem.id)
            except:
                print("BPM: " + elem.id + " was unchecked ")
                elem.ui.uncheck()

        return beam_on, np.array(orbit_x), np.array(orbit_y), np.array(orbit_s)


    def read_data(self):
        beam_on, orbit_x, orbit_y, orbit_s = self.read_bpms()
        #if not beam_on:
        #    return

        target = self.read_objective_function()
        if len(self.target_values) > self.nreadings:
            self.target_values = self.target_values[1:]
            self.orbits_x = self.orbits_x[1:]
            self.orbits_y = self.orbits_y[1:]
        self.orbits_x.append(orbit_x)
        self.orbits_y.append(orbit_y)
        self.orbit_s = orbit_s

        self.target_values = np.append(self.target_values, target)

        self.update_plot()

    def update_plot(self, ):

        self.obj_curve.setData(x=np.arange(len(self.target_values)), y=np.array(self.target_values))

        self.orb_y.setData(x=self.orbit_s, y= self.orbits_y[-1])
        self.orb_x.setData(x=self.orbit_s, y=self.orbits_x[-1])


    def stop_statistics(self):
        self.statistics_timer.stop()
        self.pb_start_statistics.setStyleSheet("color: rgb(85, 255, 127);")
        self.pb_start_statistics.setText("Statistics Accum On")

    def read_objective_function(self):
        val = self.objective_func()
        return val


    def calc_golden_orbit(self):
        targets = np.array(self.target_values)
        indx = np.argsort(targets)
        orbits_x = np.array(self.orbits_x)
        orbits_y = np.array(self.orbits_y)
        num = int(self.sb_array_len.value()*self.sb_averaging.value()*0.01)
        best_orbits_x = orbits_x[indx[-num:]]
        best_orbits_y = orbits_y[indx[-num:]]
        aver_x = np.mean(best_orbits_x, axis=0)
        aver_y = np.mean(best_orbits_y, axis=0)

        self.orb_x_ref.setData(x=self.orbit_s, y=aver_x)
        self.orb_y_ref.setData(x=self.orbit_s, y=aver_y)
        new_golden_orbit = {}
        for i, name in enumerate(self.bpms_name):
            new_golden_orbit[name] = [aver_x[i], aver_y[i]]

        self.orbit_class.golden_orbit.update_golden_orbit(new_golden_orbit)

    def set_obj_fun(self):
        """
        Method to set objective function from the GUI (channels A,B,C) or reload module obj_function.py

        :return: None
        """

        # disable button "Edit Objective Function"
        # self.ui.pb_edit_obj_func.setEnabled(False)
        a_str = str(self.le_a.text())
        state_a = self.is_le_addr_ok(self.le_a)
        b_str = str(self.le_b.text())
        state_b = self.is_le_addr_ok(self.le_b)
        c_str = str(self.le_c.text())
        state_c = self.is_le_addr_ok(self.le_c)
        func = str(self.le_of.text())
        def get_value_exp():
            A = 0.
            B = 0.
            C = 0.
            if state_a:
                A = self.mi.get_value(a_str)
            if state_b:
                B = self.mi.get_value(b_str)
            if state_c:
                C = self.mi.get_value(c_str)
            return eval(func)
        if len(func) == 0:
            return None
        self.objective_func = get_value_exp
        return self.objective_func


    def add_orbit_plot(self):
        win = pg.GraphicsLayoutWidget()
        self.plot_x = win.addPlot(row=0, col=0)

        #win.ci.layout.setRowMaximumHeight(0, 200)

        self.plot_x.showGrid(1, 1, 1)

        self.plot_y = win.addPlot(row=1, col=0)
        self.plot_x.setXLink(self.plot_y)

        self.plot_y.showGrid(1, 1, 1)

        self.plot_y.getAxis('left').enableAutoSIPrefix(enable=False)  # stop the auto unit scaling on y axes
        layout = QtGui.QGridLayout()
        self.widget.setLayout(layout)
        layout.addWidget(win, 0, 0)

        self.plot_y.setAutoVisible(y=True)

        self.plot_y.addLegend()


        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.orb_y = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Y calc', antialias=True)
        self.plot_y.addItem(self.orb_y)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=4)
        self.orb_y_ref = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Y', antialias=True)
        self.plot_y.addItem(self.orb_y_ref)

        #color = QtGui.QColor(255, 255, 0)
        #pen = pg.mkPen(color, width=3)
        #self.orb_y_golden = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Y golden', antialias=True)
        #
        #color = QtGui.QColor(0, 255, 0)
        #pen = pg.mkPen(color, width=2)
        #self.orb_y_live = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Y live', antialias=True)

        self.plot_x.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.orb_x = pg.PlotCurveItem(x=[], y=[], pen=pen,  name='X calc', antialias=True)

        self.plot_x.addItem(self.orb_x)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=4, symbolPen='o')
        self.orb_x_ref = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='X', antialias=True)
        self.plot_x.addItem(self.orb_x_ref)

        #color = QtGui.QColor(0, 255, 0)
        #pen = pg.mkPen(color, width=2)
        #self.orb_x_live = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='X live', antialias=True)
        #
        #color = QtGui.QColor(255, 255, 0)
        #pen = pg.mkPen(color, width=2)
        #self.orb_x_golden= pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='X golden', antialias=True)

        #self.plot_cor.sigRangeChanged.connect(self.zoom_signal)
        #self.plot_cor.setYRange(-3, 3)
        self.plot_x.setYRange(-2, 2)
        self.plot_y.setYRange(-2, 2)

    def add_objective_func_plot(self):
        win = pg.GraphicsLayoutWidget()
        self.plot_obj = win.addPlot()

        # win.ci.layout.setRowMaximumHeight(0, 200)

        self.plot_obj.showGrid(1, 1, 1)

        layout = QtGui.QGridLayout()
        self.widget_2.setLayout(layout)
        layout.addWidget(win, 0, 0)


        self.plot_obj.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.obj_curve = pg.PlotCurveItem(x=[], y=[], pen=pen, name='X calc', antialias=True)

        self.plot_obj.addItem(self.obj_curve)

        #color = QtGui.QColor(255, 0, 0)
        #pen = pg.mkPen(color, width=4, symbolPen='o')
        #self.obj_plot2 = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='X', antialias=True)
        #self.plot_obj.addItem(self.obj_plot2)


        # self.plot_cor.sigRangeChanged.connect(self.zoom_signal)
        # self.plot_cor.setYRange(-3, 3)
        #self.plot_x.setYRange(-2, 2)
        #self.plot_y.setYRange(-2, 2)

    def zoom_signal(self):
        if len(self.corrs) == 0:
            return

        s_up = self.plot_y.viewRange()[0][0]
        s_down = self.plot_y.viewRange()[0][1]



    def check_address(self):
        self.is_le_addr_ok(self.le_a)
        self.is_le_addr_ok(self.le_b)
        self.is_le_addr_ok(self.le_c)
        #self.is_le_addr_ok(self.le_d)
        #self.is_le_addr_ok(self.le_e)
        #self.is_le_addr_ok(self.le_alarm)

    def is_le_addr_ok(self, line_edit):
        dev = str(line_edit.text())
        state = True
        try:
            self.mi.get_value(dev)
        except:
            state = False
        if state:
            line_edit.setStyleSheet("color: rgb(85, 255, 0);")
        else:
            line_edit.setStyleSheet("color: red")
        return state

    def loadStyleSheet(self):
        """
        Sets the dark GUI theme from a css file.
        :return:
        """
        try:
            self.cssfile = "gui/style.css"
            with open(self.cssfile, "r") as f:
                self.setStyleSheet(f.read())
        except IOError:
            print ('No style sheet found!')