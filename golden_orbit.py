"""
Sergey Tomin, XFEL/DESY, 2017
"""

import numpy as np
import json
from PyQt4 import QtGui, QtCore
from scipy import io


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
    # print(orbit)
    save_json(json_file, orbit)


class GoldenOrbit:
    def __init__(self, parent):
        self.ui = parent.ui
        self.parent = parent
        self.Form = parent.parent
        self.golden_orbit = {}

        self.ui.pb_golden_orbit.clicked.connect(self.start_stop_golden_orbit)
        self.ui.pb_set_golden.clicked.connect(self.set_golden_orbit)
        self.ui.pb_zero_gold.clicked.connect(self.set_zero_golden_orbit)

        self.ui.pb_save_golden.clicked.connect(self.save_golden_as)
        self.ui.pb_load_golden.clicked.connect(self.load_golden_from)
        self.ui.actionLoad_Golden_Orbit.triggered.connect(self.load_golden_from)
        self.ui.actionSave_Golden_Orbit.triggered.connect(self.save_golden_as)

    def set_golden_orbit(self):
        """
        reads orbit and set BPM.x_ref and BPM.y_ref from actual readings.
        Writes these refs to dictionary: self.golden_orbit

        :return:
        """
        self.parent.read_orbit()
        self.golden_orbit = {}
        for elem in self.parent.bpms:
            elem.x_ref = elem.x
            elem.y_ref = elem.y
            self.golden_orbit[elem.id] = [elem.x, elem.y]

    def set_zero_golden_orbit(self):
        """
        Set BPM.x_ref and BPM.y_ref to zeros.
        Writes these refs to dictionary: self.golden_orbit

        :return:
        """
        self.golden_orbit = {}
        for elem in self.parent.bpms:
            elem.x_ref = 0.
            elem.y_ref = 0.
            self.golden_orbit[elem.id] = [0., 0.]



    def dict2golden_orbit(self):
        """
        Method sets BPM.x_ref and BPM.y_ref from dictionary: self.golden_orbit

        :return:
        """
        for elem in self.parent.orbit.bpms:
            if elem.id in self.golden_orbit.keys():
                x_gold = self.golden_orbit[elem.id][0]
                y_gold = self.golden_orbit[elem.id][1]
                elem.x_ref = x_gold
                elem.y_ref = y_gold
            else:
                elem.x_ref = 0.
                elem.y_ref = 0.


    def start_stop_golden_orbit(self):

        if self.ui.pb_golden_orbit.text() == "Show Golden Orbit":
            self.ui.pb_golden_orbit.setText("Hide Golden Orbit")
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

            print("Golden")

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
            self.ui.pb_golden_orbit.setText("Show Golden Orbit")
            #self.orb_x_golden.setData(x=[], y=[])
            #self.orb_y_golden.setData(x=[], y=[])
            #self.orb_y.update()
            #self.orb_x.update()

    def save_golden_orbit(self, filename):
        orbit = {}
        for bpm in self.Form.orbit.bpms:
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
        print(self.Form.gold_orbits_dir)
        filename = QtGui.QFileDialog.getSaveFileName(self.Form, 'Save Golden Orbit',
        self.Form.gold_orbits_dir, "txt (*.json)", QtGui.QFileDialog.DontUseNativeDialog)
        if filename:
            name = filename.split("/")[-1]
            parts = name.split(".")
            body_name = parts[0]

            if len(parts)<2 or parts[1] !="json":
                part = filename.split(".")[0]
                filename = part + ".json"

            self.save_golden_orbit(filename)


    def load_golden_from(self):
        filename = QtGui.QFileDialog.getOpenFileName(self.Form, 'Load Golden Orbit',
        self.Form.gold_orbits_dir, "txt (*.json *.mat)", QtGui.QFileDialog.DontUseNativeDialog)
        if filename:
            #print(filename)
            (body_name, extension) = filename.split("/")[-1].split(".")
            if extension == "mat":
                self.restore_golden_orbit_from_mat(filename=filename)
            else:
                self.restore_golden_orbit(filename)
