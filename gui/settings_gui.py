"""
Settings. S.Tomin.
"""

import sys
from PyQt5.QtWidgets import QCheckBox, QHBoxLayout, QMessageBox, QApplication,QMenu, QWidget, QAction, QTableWidget, QTableWidgetItem, QDoubleSpinBox
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from gui.UISettings import Ui_Form
import json


class ManulSettings(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        #QWidget.__init__(self, parent)
        self.master = parent
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #self.setStyleSheet("background-color:black;")
        self.loadStyleSheet()
        #self.ui.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.ui.pb_apply.clicked.connect(self.apply_settings)
        self.ui.cb_single_shot.stateChanged.connect(self.single_shot_set)
        self.ui.pb_cancel.clicked.connect(self.close)

        self.load_state(filename=self.master.config_dir + "settings.json")


    def single_shot_set(self):
        if self.ui.cb_single_shot.isChecked():
            self.ui.sb_nreadings.setEnabled(False)
            self.ui.sb_nlast.setEnabled(False)
            self.ui.label_2.setEnabled(False)
            self.ui.label_8.setEnabled(False)
        else:
            self.ui.sb_nreadings.setEnabled(True)
            self.ui.sb_nlast.setEnabled(True)
            self.ui.label_2.setEnabled(True)
            self.ui.label_8.setEnabled(True)

    def apply_settings(self):
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

        #if "cb_lattice" in table.keys(): self.ui.sb_co_nlast.setValue(table["co_nlast"])

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
        #QtGui.QMessageBox.question(self, "Question box", message)
        reply = QMessageBox.question(self, "Question Box",
                message,
                QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            return True

        return False

    def loadStyleSheet(self):
        """ Load in the dark theme style sheet. """
        try:
            self.cssfile = self.master.gui_dir +"style.css"
            print(self.cssfile)
            with open(self.cssfile, "r") as f:
                #print(f)
                self.setStyleSheet(f.read())
        except IOError:
            print('No style sheet found!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ManulSettings()
    window.show()
    sys.exit(app.exec_())