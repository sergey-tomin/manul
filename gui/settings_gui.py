"""
Settings. S.Tomin.
"""

import sys
from PyQt5.QtWidgets import QCheckBox, QHBoxLayout, QMessageBox, QApplication,QMenu, QWidget, QAction, QTableWidget, QTableWidgetItem, QDoubleSpinBox
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from gui.UISettings import *
import json


class ManulSettings(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.master = parent
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.loadStyleSheet()
        #self.ui.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.load_state(filename=self.master.config_dir + "settings.json")
        self.ui.pb_apply.clicked.connect(self.apply_settings)
        self.ui.pb_cancel.clicked.connect(self.close)


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

        with open(filename, 'w') as f:
            json.dump(table, f)
        print("SAVE State")

    def load_state(self, filename):
        # pvs = self.ui.widget.pvs
        with open(filename, 'r') as f:
            table = json.load(f)

        self.ui.cb_show_correction_result.setCheckState(table["show_correction_result"])
        self.ui.sb_nlast.setValue(table["nlast"])
        self.ui.sb_nreadings.setValue(table["nreadings"])
        self.ui.le_lattice.setText(table["lattice"])
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
            self.cssfile = "gui/style.css"
            print("load style")
            with open(self.cssfile, "r") as f:
                print(f)
                self.setStyleSheet(f.read())
        except IOError:
            print('No style sheet found!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ManulSettings()
    window.show()
    sys.exit(app.exec_())