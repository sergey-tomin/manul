"""
Adviser GUI. S.Tomin.
"""

import sys
from PyQt5.QtWidgets import QCheckBox, QHBoxLayout, QMessageBox, QApplication, QMenu, QWidget, QAction, QTableWidget, \
    QTableWidgetItem, QDoubleSpinBox
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from gui.UIAdviser import Ui_Form
from ml.adviser import Adviser
import json
import numpy as np
from devices import MIAdviser

class ManulAdviser(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        # QWidget.__init__(self, parent)
        self.master = parent
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # self.setStyleSheet("background-color:black;")
        self.loadStyleSheet()
        # self.ui.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.mi_adv = MIAdviser()
        self.mi_adv.mi = self.master.mi
        self.adviser = Adviser(cor_file="./ml/cor_essence.json", bpm_file="./ml/bpm_essence.json")
        self.set_slider()
        self.update_min_sase()
        self.ui.horizontalSlider.valueChanged.connect(self.update_min_sase)

        self.ui.pb_find_go.clicked.connect(self.find_go)
        self.ui.pb_show.clicked.connect(self.show_diff)
        self.ui.pb_get_state.clicked.connect(self.get_current_state)
        #self.ui.cb_single_shot.stateChanged.connect(self.single_shot_set)
        #self.ui.pb_cancel.clicked.connect(self.close)
        #
        #self.load_state(filename=self.master.config_dir + "settings.json")

    def set_slider(self):
        min_sase = np.min(self.adviser.sases)
        max_sase = np.max(self.adviser.sases)
        self.ui.horizontalSlider.setMinimum(min_sase)
        self.ui.horizontalSlider.setMaximum(max_sase)
        self.ui.lab_sase_max.setText(str(max_sase))

    def update_min_sase(self):
        val = self.ui.horizontalSlider.value()
        self.ui.lab_sase_cur.setText(str(val))

        self.indxs_above_thr = self.adviser.get_indices(min_sase=val)
        self.ui.lab_nfiles.setText(str(len(self.indxs_above_thr)))

    def show_diff(self):
        if self.ui.mf_table.ui.tableWidget.last_row == None:
            return

        n = self.ui.mf_table.ui.tableWidget.last_row

        mf = self.m_files[n]
        mf_id = float(mf["id"])
        indx = np.where(self.adviser.cor_ids == mf_id)[0]
        print(self.adviser.sases[indx])
        go_kick = self.adviser.cor_kicks[indx][0]
        #print(go_kick)
        go_bpm_x = self.adviser.bpm_X[indx][0]
        #print(go_bpm_x)
        go_bpm_y = self.adviser.bpm_Y[indx][0]
        x_indx = []
        y_indx = []
        for i, name in enumerate(self.adviser.cor_ref_names):
            if "X" in name:
                x_indx.append(i)
            else:
                y_indx.append(i)
                
        delta_kick = (go_kick-self.ckicks)*1000
        if self.ui.rb_x_plane.isChecked():
            delta = delta_kick[x_indx]
        else:
            delta = delta_kick[y_indx]
        big_diff_indx = np.where(np.abs(delta_kick) > 0.5)[0]
        
        print(np.array(self.adviser.cor_ref_names)[big_diff_indx])
        self.ui.plot_widget.update_plot(sx=np.arange(len(go_bpm_x)), delta_x=go_bpm_x,
                                        sk=np.arange(len(delta)), delta_k=delta)


    def find_go(self):
        n_files = self.ui.sb_nneighbors.value()
        if n_files > len(self.indxs_above_thr):
            self.ui.sb_nneighbors.setValue(len(self.indxs_above_thr))
            n_files = len(self.indxs_above_thr)
        min_sase = self.ui.horizontalSlider.value()
        cur_state = self.get_current_state()
        if self.ui.rb_energy_prof.isChecked():
            fit_db = "moment"
        elif self.ui.rb_cor_kick.isChecked():
            fit_db = "kick"
        else:
            print("error")

        self.m_files = self.adviser.find_mfiles(n_files, min_sase, cur_state, fit_db=fit_db)
        self.ui.mf_table.init_table(self.m_files)
        #self.ui.tableWidget
        for file in self.m_files:
            print(file)

    def get_current_state(self):
        #self.adviser.cor_ref_names

        self.ckicks, self.cmoments = self.mi_adv.get_corrs(ref_names=self.adviser.cor_ref_names)
        #cx = self.mi_adv.get_bpm_x(ref_names=self.adviser.bpm_ref_names)
        #cy = self.mi_adv.get_bpm_y(ref_names=self.adviser.bpm_ref_names)

        if self.ui.rb_energy_prof.isChecked():
            fit_array = self.cmoments
        else:# self.ui.rb_cor_kick.isChecked():
            fit_array = self.ckicks
        #print(self.indxs_above_thr)
        #fit_array = fit_array[self.indxs_above_thr]
        return fit_array

    def save_set(self):
        update = self.question_box("Rewrite Settings?")
        if update:
            if not os.path.exists(self.master.config_dir):
                os.makedirs(self.master.config_dir)
            self.save_state(self.master.config_dir + "settings.json")
        self.master.load_settings()

    def save_state(self, filename):
        table = {}
        table["show_correction_result"] = self.ui.cb_show_correction_result.checkState()
        table["nlast"] = self.ui.sb_nlast.value()
        table["nreadings"] = self.ui.sb_nreadings.value()
        table["lattice"] = self.ui.le_lattice.text()
        table["logbook"] = self.ui.le_logbook.text()
        table["epsilon_x"] = self.ui.sb_epsilon_x.value()
        table["epsilon_y"] = self.ui.sb_epsilon_y.value()
        table["uncheck_corrs"] = self.string2list(self.ui.te_corrs.toPlainText())
        table["uncheck_bpms"] = self.string2list(self.ui.te_bpms.toPlainText())
        table["single_shot"] = self.ui.cb_single_shot.checkState()

        table["le_cl_energy"] = self.ui.le_cl_energy.text()
        table["le_b2_energy"] = self.ui.le_b2_energy.text()
        table["le_b1_energy"] = self.ui.le_b1_energy.text()
        table["le_i1_energy"] = self.ui.le_i1_energy.text()

        table["co_nlast"] = self.ui.sb_co_nlast.value()

        with open(filename, 'w') as f:
            json.dump(table, f)
        print("SAVE State")

    def list2string(self, dev_list):
        return ", ".join(dev_list)

    def string2list(self, dev_str):
        lst = dev_str.split(",")
        lst = [text.replace(" ", "") for text in lst]
        lst = [text.replace("\n", "") for text in lst]
        return lst

    def load_state(self, filename):
        # pvs = self.ui.widget.pvs
        with open(filename, 'r') as f:
            table = json.load(f)

        self.ui.cb_show_correction_result.setCheckState(table["show_correction_result"])
        self.ui.sb_nlast.setValue(table["nlast"])
        self.ui.sb_nreadings.setValue(table["nreadings"])
        self.ui.le_lattice.setText(table["lattice"])
        if "logbook" in table.keys():  self.ui.le_logbook.setText(table["logbook"])

        if "epsilon_x" in table.keys():  self.ui.sb_epsilon_x.setValue(table["epsilon_x"])
        if "epsilon_y" in table.keys():  self.ui.sb_epsilon_y.setValue(table["epsilon_y"])
        if "uncheck_corrs" in table.keys(): self.ui.te_corrs.setPlainText(self.list2string(table["uncheck_corrs"]))
        if "uncheck_bpms" in table.keys():  self.ui.te_bpms.setPlainText(self.list2string(table["uncheck_bpms"]))
        if "single_shot" in table.keys(): self.ui.cb_single_shot.setCheckState(table["single_shot"])

        if "le_cl_energy" in table.keys(): self.ui.le_cl_energy.setText(table["le_cl_energy"])
        if "le_b2_energy" in table.keys(): self.ui.le_b2_energy.setText(table["le_b2_energy"])
        if "le_b1_energy" in table.keys(): self.ui.le_b1_energy.setText(table["le_b1_energy"])
        if "le_i1_energy" in table.keys(): self.ui.le_i1_energy.setText(table["le_i1_energy"])

        if "co_nlast" in table.keys(): self.ui.sb_co_nlast.setValue(table["co_nlast"])

        # if "cb_lattice" in table.keys(): self.ui.sb_co_nlast.setValue(table["co_nlast"])

        #        a = table["uncheck_corrs"].split(",")
        #        a = [text.replace(" ", "") for text in a]
        #        a = [text.replace("\n", "") for text in a]
        #        print(a)
        print("LOAD State")

    def save_presettings(self):
        update = self.question_box("Rewrite Settings?")
        if update:
            if not os.path.exists(self.master.configs_dir):
                os.makedirs(self.master.configs_dir)
            self.save_state(self.master.configs_dir + "settings.json")

    def question_box(self, message):
        # QtGui.QMessageBox.question(self, "Question box", message)
        reply = QMessageBox.question(self, "Question Box",
                                     message,
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            return True

        return False

    def loadStyleSheet(self):
        """ Load in the dark theme style sheet. """
        try:
            self.cssfile = self.master.gui_dir + "style.css"
            print(self.cssfile)
            with open(self.cssfile, "r") as f:
                # print(f)
                self.setStyleSheet(f.read())
        except IOError:
            print('No style sheet found!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ManulAdviser()
    window.show()
    sys.exit(app.exec_())