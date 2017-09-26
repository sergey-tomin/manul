"""
Sergey Tomin, XFEL/DESY, 2017
"""

import numpy as np
import json
from ocelot.optimizer.mint import opt_objects as obj
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QMessageBox
from scipy import io
import pyqtgraph as pg
from gui.UIadaptive_feedback import Ui_Form
from collections import deque
import time
import os
from threading import Thread, Event
from ocelot.cpbd.magnetic_lattice import *
from ocelot.optimizer.mint.xfel_interface import *


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



class UIAFeedBack(QWidget, Ui_Form):
    def __init__(self, parent=None, orbit=None):
        QWidget.__init__(self, parent)
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
        self.ref_aver_x = []
        self.ref_aver_y = []
        #self.Form = parent.parent
        #print("load style")
        self.configs_dir = "./configs/"
        self.golden_orbit = {}

        self.pb_start_feedback.clicked.connect(self.start_stop_feedback)

        self.pb_start_statistics.clicked.connect(self.start_stop_statistics)
        self.update_plot_counter = 0
        self.orbits_x = []
        self.orbits_y = []
        self.orbit_s = []
        self.target_values = []
        self.nreadings = 100
        self.feedback_timer = pg.QtCore.QTimer()
        self.feedback_timer.timeout.connect(self.auto_correction)

        self.statistics_timer = pg.QtCore.QTimer()
        self.statistics_timer.timeout.connect(self.loop)

        self.add_orbit_plot()
        self.add_objective_func_plot()
        self.objective_func = None
        self.le_a.setText("XFEL.FEL/XGM.PREPROCESSING/XGM.2643.T9.CH0/RESULT.TD")
        self.le_of.setText("np.mean(np.array(A)[:,1])")
        self.le_a.textChanged.connect(self.check_address)
        self.le_b.textChanged.connect(self.check_address)
        self.le_c.textChanged.connect(self.check_address)

        self.bpms_name = []
        self.counter = 0
        self.debug_mode = False
        if self.parent.mi.__class__ == TestMachineInterface:
            self.debug_mode = True
        self.first_go_x = []
        self.first_go_y = []
        self.cur_go_x = []
        self.cur_go_y = []
        self.cb_load_settings.addItem("SASE1 launch")
        #self.cb_load_settings.addItem("SASE1 aircoils")
        self.cb_load_settings.setCurrentIndex(0)
        self.pb_load_settings.clicked.connect(self.load_presettings)
        self.pb_save_settings.clicked.connect(self.save_presettings)

    def save_state(self, filename):
        # pvs = self.ui.widget.pvs
        table = {}
        bpms = [bpm.id for bpm in self.orbit_class.get_dev_from_cb_state(self.orbit_class.bpms)]
        corrs = [cor.id for cor in self.orbit_class.get_dev_from_cb_state(self.orbit_class.corrs)]
        table["active_corrs"] = corrs
        table["active_bpms"] = bpms
        table["feedback_reprate"] = self.sb_feedback_rep.value()
        table["close_orbit"] = self.orbit_class.ui.cb_close_orbit.checkState()
        table["current_lattice"] = self.orbit_class.ui.cb_lattice.currentText()
        table["array_len"] = self.sb_array_len.value()
        table["go_recalc_delay"] = self.sb_go_recalc_delay.value()
        table["ref_orbit_nread"] = self.sb_ref_orbit_nread.value()
        table["averaging"] = self.sb_averaging.value()
        with open(filename, 'w') as f:
            json.dump(table, f)
        # pickle.dump(table, filename)
        print("SAVE State")

    def load_state(self, filename):
        # pvs = self.ui.widget.pvs
        with open(filename, 'r') as f:
            table = json.load(f)
        corrs = table["active_corrs"]
        bpms = table["active_bpms"]

        self.orbit_class.ui.cb_close_orbit.setCheckState(table["close_orbit"])

        all_items = [str(self.parent.ui.cb_lattice.itemText(i)) for i in range(self.parent.ui.cb_lattice.count())]
        inx = all_items.index(table["current_lattice"])
        self.parent.ui.cb_lattice.setCurrentIndex(inx)

        self.sb_feedback_rep.setValue(table["feedback_reprate"])
        self.sb_array_len.setValue(table["array_len"])
        self.sb_go_recalc_delay.setValue(table["go_recalc_delay"] )
        self.sb_ref_orbit_nread.setValue(table["ref_orbit_nread"])
        self.sb_averaging.setValue(table["averaging"])
        print("LOAD State")
        return corrs, bpms

    def save_presettings(self):
        update = self.question_box("Rewrite config?")
        if update:
            if not os.path.exists(self.configs_dir):
                os.makedirs(self.configs_dir)
                #self.error_box("Config file does not exist.")
                #return
            self.save_state(self.configs_dir+ self.cb_load_settings.currentText()+".json")

    def load_presettings(self):
        if self.cb_load_settings.currentText() == "SASE1 launch":
            if not os.path.exists(self.configs_dir+ str(self.cb_load_settings.currentText()) +".json"):
                self.error_box("Config file does not exist.")
                return
            active_corrs, active_bpms = self.load_state(self.configs_dir+ str(self.cb_load_settings.currentText()) +".json")


        for cor in self.orbit_class.corrs:
            if cor.id not in active_corrs:
                cor.ui.uncheck()
        for bpm in self.orbit_class.bpms:
            if bpm.id not in active_bpms:
                bpm.ui.uncheck()
        self.orbit_class.correct()
        self.orbit_class.golden_orbit.set_golden_orbit()




    def loop(self):
        self.counter += 1
        beam_on = self.read_data()
        if not beam_on:
            self.counter -= 1
            print("beam OFF. counter -= 1")
        bpm_delay = self.sb_time_delay.value()
        go_delay = self.sb_go_recalc_delay.value()
        #print(self.counter, int(go_delay/bpm_delay), self.counter % int(go_delay/bpm_delay))
        if self.counter % int(go_delay/bpm_delay) == int(go_delay/bpm_delay)-1:
            go_x, go_y = self.calc_golden_orbit()
            if self.counter  == int(go_delay/bpm_delay)*3-1:
                self.first_go_x = go_x
                self.first_go_y = go_y

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
        #print("I am here")

        self.counter = 0
        delay = self.sb_time_delay.value()*1000
        #self.corrs = self.get_dev_from_cb_state(self.orbit_class.corrs)
        #self.bpms = self.orbit_class.get_dev_from_cb_state(self.orbit_class.bpms)
        self.orbit_class.read_orbit()

        self.orbit_class.uncheck_red()

        self.orbit_class.golden_orbit.set_golden_orbit()

        self.orbit = self.orbit_class.create_Orbit_obj()


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
                print("objective function = None")
                return None

            self.statistics_timer.start(delay)
            self.statistics_timer.start()
            self.pb_start_statistics.setText("Statistics Accum Off")
            self.pb_start_statistics.setStyleSheet("color: red")

    def stop_feedback(self):
        self.feedback_timer.stop()
        self.pb_start_feedback.setStyleSheet("color: rgb(85, 255, 127);")
        self.pb_start_feedback.setText("Start Feedback")

    def start_stop_feedback(self):
        """
        Method to start/stop feedback timer.
        sb_feedback_sec - spinBox - set seconds for timer
        pb_feedback - pushBatton Off/On
        feedback_timer - timer
        :return:
        """
        #print("I am here")

        if self.pb_start_statistics.text() == "Statistics Accum On":
            return 0

        #self.orbit = self.orbit_class.create_Orbit_obj()

        delay = self.sb_feedback_rep.value()*1000
        if self.pb_start_feedback.text() == "Stop Feedback":
            self.stop_feedback()
        else:
            self.feedback_timer.start(delay)
            self.pb_start_feedback.setText("Stop Feedback")
            self.pb_start_feedback.setStyleSheet("color: red")


    def auto_correction(self):
        """
        Method repeats correction in a loop.
        repetation rate is defined by spinBox - sb_feedback_sec
        feedback_timer - QTimer to repats correction oin different thread

        :return:
        """
        #beam_on = self.read_orbit()
        #time.sleep(0.01)
        #if beam_on:
        self.ref_orbit_calc()
        stop_flag = self.correct()
        time.sleep(0.01)
        if not stop_flag:
            self.apply_kicks()
            time.sleep(0.5)
            self.le_warn.clear()
        else:
            print("Exceed limits")
            self.le_warn.clear()
            self.le_warn.setText("Stop flag. Kicks are not applied")
            self.le_warn.setStyleSheet("color: red")
            time.sleep(1)

    def correct(self):
        """
        Method to the Orbit correctiion. Method calculate correctors strengths (kicks)
        and call function to calculate (self.calc_orbit()) and draw orbit on the plot
        but does not send it to the DOOCS server.

        :return:
        """
        stop_flag = False
        self.orbit_class.online_calc = False
        # read orbit devs
        for elem in self.orbit.corrs:
            elem.kick_mrad = elem.mi.get_value()
            elem.angle_read = elem.kick_mrad*1e-3
            elem.i_kick = elem.kick_mrad
            elem.ui.set_init_value(elem.kick_mrad)
            elem.ui.set_value(elem.kick_mrad)
            #elem.transfer_map = create_transfer_map(elem)
            elem.transfer_map = self.parent.lat.method.create_tm(elem)
            if elem.ui.alarm:
                stop_flag = True


        #self.parent.lat.update_transfer_maps()

        for elem in self.orbit.bpms:
            if elem.id not in self.new_ref_orbit.keys():
                stop_flag = True
                return stop_flag
            elem.x = self.new_ref_orbit[elem.id][0]
            elem.y = self.new_ref_orbit[elem.id][1]
            elem.ui.set_value((elem.x*1000., elem.y*1000.))
            #print(elem.id, (elem.x*1000., elem.y*1000.))
            if elem.ui.alarm:
                stop_flag = True
        if stop_flag:
            return stop_flag
        self.orbit_class.online_calc = True
        #self.uncheck_red()

        #self.orbit = self.create_Orbit_obj()

        if not self.orbit_class.is_rm_ok(self.orbit):
            self.parent.error_box("Calculate Response Matrix")
            return 0

        self.orbit_class.golden_orbit.dict2golden_orbit()
        # for bpm in self.bpms:
        #    print(bpm.id, bpm.x, bpm.y)

        if self.orbit_class.ui.cb_close_orbit.isChecked():
            self.orbit_class.close_orbit()

        self.calc_correction = {}
        for cor in self.orbit.corrs:
            cor.angle = 0.
            self.calc_correction[cor.id] = cor.angle

        alpha = 0.#self.ui.sb_alpha.value()
        self.orbit.correction(alpha=alpha, p_init=None, epsilon_x=1e-3, epsilon_y=1e-3)

        for cor in self.orbit.corrs:
            self.calc_correction[cor.id] = cor.angle

        self.set_values2correctors()
        return stop_flag

    def apply_kicks(self):
        """
        Methos sends correctors kicks to DOOCS, if strengths below the limits,
        otherwise error box will appear

        :return:
        """

        #corrs = self.get_dev_from_cb_state(self.corrs)

        for cor in self.orbit.corrs:
            if cor.ui.alarm:
                self.stop_feedback()
                self.error_box("kick exceeds limits. Try 'Uncheck Red' and recalculate correction")
                return 0

        for cor in self.orbit.corrs:
            kick_mrad = cor.ui.get_value()
            print(cor.id," set: ", cor.ui.get_init_value(), "-->", kick_mrad)
            cor.mi.set_value(kick_mrad)

    def set_values2correctors(self):

        apply_fraction = self.sb_afeed_fraction.value()
        self.orbit_class.online_calc = False
        for cor in self.orbit.corrs:
            kick_mrad_old = cor.ui.get_init_value()
            if cor.id in self.calc_correction.keys():
                cor.angle = self.calc_correction[cor.id]

            delta_kick_mrad = cor.angle*1000*apply_fraction
            #print(cor.angle*1000, delta_kick_mrad)
            new_kick_mrad = kick_mrad_old + delta_kick_mrad
            cor.kick_mrad = new_kick_mrad
            cor.ui.set_value(cor.kick_mrad)
            warn = (np.abs(new_kick_mrad) - np.abs(kick_mrad_old)) > 0.5

            cor.ui.check_values(cor.kick_mrad, cor.lims, warn)
        self.orbit_class.online_calc = True
        if self.cb_update_display.isChecked():
            self.orbit_class.calc_orbit()

    def read_bpms(self):
        charge_thresh = 0.005
        beam_on = True
        orbit_x = []
        orbit_y = []
        orbit_s = []
        self.bpms_name = []

        for elem in self.orbit.bpms:
            try:
                x_mm, y_mm = elem.mi.get_pos()
                charge = elem.mi.get_charge()
                if not self.debug_mode and charge < charge_thresh:
                    print("charge < charge_thresh", charge < charge_thresh)
                    self.le_warn.clear()
                    self.le_warn.setText(elem.id+" charge < charge_thresh")
                    self.le_warn.setStyleSheet("color: red")
                    beam_on = False
                x = x_mm / 1000.
                y = y_mm / 1000.
                orbit_x.append(x) #[elem.s, x, y])
                orbit_y.append(y)
                orbit_s.append(elem.s)
                self.bpms_name.append(elem.id)
            except:
                #print("BPM: " + elem.id + " was unchecked ")
                #elem.ui.uncheck()
                self.le_warn.clear()
                self.le_warn.setText("beam OFF")
                print("beam OFF")
                beam_on = False
        #print(beam_on)
        return beam_on, np.array(orbit_x), np.array(orbit_y), np.array(orbit_s)


    def read_data(self):
        beam_on, orbit_x, orbit_y, orbit_s = self.read_bpms()
        if not beam_on:
            return beam_on
        print("read data")
        target = self.read_objective_function()
        if target == None:
            self.stop_statistics()
            return None
        if len(self.target_values) >= self.nreadings:
            self.target_values = self.target_values[1:]
            #self.orbits_x = np.roll(self.orbits_x, -1) #self.orbits_x[1:]
            #self.orbits_y = np.roll(self.orbits_y, -1) #self.orbits_y[1:]
            self.orbits_x = self.orbits_x[1:]
            self.orbits_y = self.orbits_y[1:]
        self.target_values = np.append(self.target_values, target)
        self.orbits_x.append(orbit_x)
        self.orbits_y.append(orbit_y)
        #print(np.shape(self.orbits_x), len(self.target_values)-1)
        #self.orbits_x[len(self.target_values)-1] = orbit_x
        #self.orbits_y[len(self.target_values)-1] = orbit_y
        self.orbit_s = orbit_s

        self.update_plot_counter += 1
        if self.update_plot_counter%2 == 0:
            self.update_obj_plot()
        return beam_on

    def update_obj_plot(self, ):

        self.obj_curve.setData(x=np.arange(len(self.target_values)), y=np.array(self.target_values))

    def update_orb_plot(self):
        self.orb_y.setData(x=self.orbit_s, y= self.ref_aver_x)
        self.orb_x.setData(x=self.orbit_s, y= self.ref_aver_y)


    def stop_statistics(self):
        self.statistics_timer.stop()
        self.pb_start_statistics.setStyleSheet("color: rgb(85, 255, 127);")
        self.pb_start_statistics.setText("Statistics Accum On")

    def read_objective_function(self):
        try:
            val = self.objective_func()
        except:
            self.error_box("Wrong Objective Function")
            return None
        return val


    def calc_golden_orbit(self):
        targets = np.array(self.target_values)
        indx = np.argsort(targets)
        orbits_x = np.array(self.orbits_x)
        orbits_y = np.array(self.orbits_y)
        n_orbits = len(orbits_x)
        num_good_obits = int(n_orbits*self.sb_averaging.value()*0.01)
        if num_good_obits<1:
            num_good_obits = 1
        best_orbits_x = orbits_x[indx[-num_good_obits:]]
        best_orbits_y = orbits_y[indx[-num_good_obits:]]
        if len(best_orbits_x) ==1:
            aver_x = best_orbits_x[0]
            aver_y = best_orbits_y[0]
        else:
            aver_x = np.mean(best_orbits_x, axis=0)
            aver_y = np.mean(best_orbits_y, axis=0)
        new_golden_orbit = {}
        for i, name in enumerate(self.bpms_name):
            new_golden_orbit[name] = [aver_x[i], aver_y[i]]
        self.orbit_class.golden_orbit.update_golden_orbit(new_golden_orbit)
        #self.update_orb_plot()
        if len(self.first_go_x) != len(aver_x) or len(self.first_go_y) != len(aver_y) :
            delta_go_x = aver_x
            delta_go_y = aver_y
        else:
            delta_go_x = aver_x - self.first_go_x
            delta_go_y = aver_y - self.first_go_y
        self.orb_x_ref.setData(x=self.orbit_s, y=delta_go_x*1000)
        self.orb_y_ref.setData(x=self.orbit_s, y=delta_go_y*1000)

        self.cur_go_x = aver_x
        self.cur_go_y = aver_y
        return aver_x, aver_y

    def ref_orbit_calc(self):
        # ********* reference orbit ***********

        nlast_readings = int(self.sb_ref_orbit_nread.value())

        orbits_x = np.array(self.orbits_x)
        orbits_y = np.array(self.orbits_y)
        n_orbits = len(orbits_x)

        if n_orbits < nlast_readings:
            nlast_readings = n_orbits - 1

        num_bad_orbits = int(n_orbits*0.2) # 20% bad orbits

        #ref_orbits_x = orbits_x[indx[num_bad_orbits : n_orbits - num_good_obits]]
        #ref_orbits_y = orbits_y[indx[num_bad_orbits : n_orbits - num_good_obits]]

        ref_orbits_x = orbits_x[-nlast_readings:]
        ref_orbits_y = orbits_y[-nlast_readings:]

        self.ref_aver_x = np.mean(ref_orbits_x, axis=0)
        self.ref_aver_y = np.mean(ref_orbits_y, axis=0)

        self.new_ref_orbit = {}
        for i, name in enumerate(self.bpms_name):
            self.new_ref_orbit[name] = [self.ref_aver_x[i], self.ref_aver_y[i]]

        if len(self.cur_go_x) != len(self.ref_aver_x ) or len(self.cur_go_y) != len(self.ref_aver_y ):
            delta_ro_x = self.ref_aver_x
            delta_ro_y = self.ref_aver_y
        else:
            delta_ro_x = self.ref_aver_x - self.cur_go_x
            delta_ro_y = self.ref_aver_y - self.cur_go_y

        self.orb_y.setData(x=self.orbit_s, y=delta_ro_x*1000)
        self.orb_x.setData(x=self.orbit_s, y=delta_ro_y*1000)


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
            if func == "":
                return 0
            return eval(func)
        #if len(func) == 0:
        #    return None

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
        if len(self.orbit.corrs) == 0:
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

    def error_box(self, message):
        QtGui.QMessageBox.about(self, "Error box", message)

    def question_box(self, message):
        #QtGui.QMessageBox.question(self, "Question box", message)
        reply = QtGui.QMessageBox.question(self, "Question Box",
                message,
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if reply==QtGui.QMessageBox.Yes:
            return True

        return False