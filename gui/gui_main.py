"""
Most of GUI logic is placed here.
S.Tomin, 2017
"""

#from ocelot.optimizer.UIOcelotInterface_gen import *
import json
import scipy
from PyQt5.QtGui import QPixmap, QImage, QScreen
from PyQt5 import QtWidgets
from PIL import Image
import subprocess
import base64
from datetime import datetime
import numpy as np
import sys
import os
import webbrowser
from shutil import copy
#from gui.UImanul2 import Ui_Form
from gui.UImanul2 import Ui_MainWindow
#from gui.UIadaptive_feedback import Ui_Form

from PyQt5 import QtGui, QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def send_to_desy_elog(author, title, severity, text, elog, image=None):
    """
    Send information to a supplied electronic logbook.
    Author: Christopher Behrens (DESY)
    """

    # The DOOCS elog expects an XML string in a particular format. This string
    # is beeing generated in the following as an initial list of strings.
    succeded = True  # indicator for a completely successful job
    # list beginning
    elogXMLStringList = ['<?xml version="1.0" encoding="ISO-8859-1"?>', '<entry>']

    # author information
    elogXMLStringList.append('<author>')
    elogXMLStringList.append(author)
    elogXMLStringList.append('</author>')
    # title information
    elogXMLStringList.append('<title>')
    elogXMLStringList.append(title)
    elogXMLStringList.append('</title>')
    # severity information
    elogXMLStringList.append('<severity>')
    elogXMLStringList.append(severity)
    elogXMLStringList.append('</severity>')
    # text information
    elogXMLStringList.append('<text>')
    elogXMLStringList.append(text)
    elogXMLStringList.append('</text>')
    # image information
    if image:
        try:
            #encodedImage = base64.b64encode(image)
            elogXMLStringList.append('<image>')
            elogXMLStringList.append(image)
            elogXMLStringList.append('</image>')
        except:  # make elog entry anyway, but return error (succeded = False)
            succeded = False
    # list end
    elogXMLStringList.append('</entry>')
    # join list to the final string
    elogXMLString = '\n'.join(elogXMLStringList)
    # open printer process
    try:
        lpr = subprocess.Popen(['/usr/bin/lp', '-o', 'raw', '-d', elog],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # send printer job
        lpr.communicate(elogXMLString.encode('utf-8'))
    except:
        succeded = False
    return succeded



class MainWindow(Ui_MainWindow):
    def __init__(self, Form):
        Ui_MainWindow.__init__(self)
        self.setupUi(Form)
        self.menuBar.setNativeMenuBar(False)
        self.mainToolBar.setVisible(False)
        self.Form = Form
        self.settings_file = self.Form.config_file
        # load in the dark theme style sheet
        self.restore_state(self.Form.config_file)

        style_index = self.get_style_name_index()
        style_name = self.Form.gui_styles[style_index]
        #if self.style_file != "standard.css":
        self.loadStyleSheet(filename=self.Form.gui_dir + style_name)

        self.tableWidget = self.add_table(widget=self.widget, headers=["Quadrupole", "Init. Val.", "Cur. Val."])
        self.table_cor = self.add_table(widget=self.w_cor, headers=["Corrector", "Init. Val.", "Cur. Val.", "Active"])
        self.table_bpm = self.add_table(widget=self.w_bpm, headers=["BPM", "       X       ", "       Y       ", "Act."])
        self.table_golden_bpm = self.add_table(widget=self.widget_7,
                                        headers=["BPM", "       X       ", "       Y       ", "Act."])
        if self.show_cor_panel:
            self.show_device_panel(True)
        else:
            self.show_device_panel(False)
        #self.hide_show_divece_panel()
        self.pb_hide_show_dev_panel.clicked.connect(self.hide_show_device_panel)
        self.actionSend_orbit.triggered.connect(lambda: self.logbook(self.w_orbit))
        self.actionSend_all.triggered.connect(lambda: self.logbook(self.Form))

        if self.show_extension:
            self.show_gentle_panel(True)
        else:
            self.show_gentle_panel(False)
        #self.hide_show_divece_panel()
        self.pb_extend.clicked.connect(self.advance_panel)



    def show_device_panel(self, show=True):
        if show:
            self.tabWidget_3.show()
            self.pb_hide_show_dev_panel.setText("Hide Cor/BPM panel")
            self.pb_hide_show_dev_panel.setStyleSheet("color: rgb(85, 255, 255);")
        else:
            self.pb_hide_show_dev_panel.setText("Show Cor/BPM panel")
            self.pb_hide_show_dev_panel.setStyleSheet("color: rgb(255, 0, 255);")
            self.tabWidget_3.hide()

    def hide_show_device_panel(self):
        if self.pb_hide_show_dev_panel.text() == "Hide Cor/BPM panel":
            self.show_device_panel(False)
        else:
            self.show_device_panel(True)

    def show_gentle_panel(self, show=True):
        if show:
            self.widget_5.show()
            self.pb_extend.setText("Close Gentle Correction Panel")
            self.pb_extend.setStyleSheet("color: rgb(85, 255, 255);")
        else:
            self.pb_extend.setText("Open Gentle Correction Panel")
            self.pb_extend.setStyleSheet("color: rgb(255, 0, 255);")
            self.widget_5.hide()

    def advance_panel(self):
        if self.pb_extend.text() == "Close Gentle Correction Panel":
            self.show_gentle_panel(False)
            if self.cb_freeze_bpms.isChecked():
                print("CLOSING ... unfreeze BPMs")
                self.cb_freeze_bpms.setChecked(False)
        else:
            self.show_gentle_panel(True)

    def add_table(self, widget, headers):

        tableWidget = QtWidgets.QTableWidget(self.Form)
        tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        tableWidget.setObjectName(_fromUtf8("tableWidget"))
        tableWidget.setColumnCount(0)
        tableWidget.setRowCount(0)
        layout = QtWidgets.QGridLayout()
        widget.setLayout(layout)
        layout.addWidget(tableWidget, 0, 0)

        tableWidget.setColumnCount(len(headers))
        tableWidget.setHorizontalHeaderLabels(headers)
        header = tableWidget.horizontalHeader()
        header.setStretchLastSection(True)

        tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # No user edits on talbe

        return tableWidget

    def add_cor_table(self):

        self.table_cor = QtWidgets.QTableWidget(self.Form)
        self.table_cor.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table_cor.setObjectName(_fromUtf8("tableWidget"))
        self.table_cor.setColumnCount(0)
        self.table_cor.setRowCount(0)
        layout = QtWidgets.QGridLayout()
        self.w_orbit.setLayout(layout)
        layout.addWidget(self.table_cor, 0, 0)

        headers = ["Correctors", "Init. Val.", "Cur. Val."]
        self.table_cor.setColumnCount(len(headers))
        self.table_cor.setHorizontalHeaderLabels(headers)
        header = self.table_cor.horizontalHeader()
        header.setResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.table_cor.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # No user edits on talbe
        self.table_cor.horizontalHeader().setResizeMode(QtWidgets.QHeaderView.Stretch)

    def alarm_value(self):
        """
        reading alarm value
        :return:
        """
        dev = str(self.le_alarm.text())
        try:
            value = self.Form.mi.get_value(dev)
            self.label_alarm.setText(str(np.round(value, 2)))
        except:
            self.label_alarm.setText(str("None"))

    def set_cycle(self):
        """
        Select time for objective method data collection time.
        Scanner will wait this long to collect new data.
        """
        self.trim_delay = self.sb_tdelay.value()
        data_delay = self.sb_ddelay.value()*self.sb_nreadings.value()
        self.label_7.setText("Cycle Period = " + str(np.around(self.trim_delay + data_delay, 3)))
        self.Form.total_delay = self.trim_delay

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
            self.Form.mi.get_value(dev)
        except:
            state = False
        if state:
            line_edit.setStyleSheet("color: rgb(85, 255, 0);")
        else:
            line_edit.setStyleSheet("color: red")
        return state

    def save_state(self, filename):
        # pvs = self.ui.widget.pvs
        table = self.widget.get_state()

        table["use_predef"] = self.cb_use_predef.checkState()

        max_pen = self.sb_max_pen.value()
        timeout = self.sb_tdelay.value()


        max_iter = self.sb_num_iter.value()
        # objective function
        fun_a = str(self.le_a.text())
        fun_b = str(self.le_b.text())
        fun_c = str(self.le_c.text())
        obj_fun = str(self.le_obf.text())
        # alarm
        alarm_dev = str(self.le_alarm.text())
        alarm_min = self.sb_alarm_min.value()
        alarm_max = self.sb_alarm_max.value()

        table["max_pen"] = max_pen
        table["timeout"] = timeout
        table["nreadings"] = self.sb_nreadings.value()
        table["interval"] = self.sb_ddelay.value()

        table["max_iter"] = max_iter
        table["fun_a"] = fun_a
        table["fun_b"] = fun_b
        table["fun_c"] = fun_c
        table["fun_d"] = str(self.le_d.text())
        table["fun_e"] = str(self.le_e.text())
        table["obj_fun"] = obj_fun

        table["alarm_dev"] = alarm_dev
        table["alarm_min"] = alarm_min
        table["alarm_max"] = alarm_max
        table["alarm_timeout"] = self.sb_alarm_timeout.value()

        table["seed_iter"] = self.sb_seed_iter.value()
        table["use_live_seed"] = self.cb_use_live_seed.checkState()

        table["isim_rel_step"] = self.sb_isim_rel_step.value()
        table["use_isim"] = self.cb_use_isim.checkState()

        table["hyper_file"] = self.Form.hyper_file

        table["set_best_sol"] = self.cb_set_best_sol.checkState()

        table["algorithm"] = str(self.cb_select_alg.currentText())

        with open(filename, 'w') as f:
            json.dump(table, f)
        # pickle.dump(table, filename)
        print("SAVE State")

    def restore_state(self, filename):
        # try:
        with open(filename, 'r') as f:
            # data_new = pickle.load(f)
            table = json.load(f)
        self.style_file = ""
        self.show_cor_panel = False
        self.show_extension = False
        try:
            self.style_file = table["style_file"]
            self.show_cor_panel = table["show_cor_panel"]
            if "show_extension" in table: self.show_extension = table["show_extension"]
            print("RESTORE STATE: OK")
        except:
            print("RESTORE STATE: ERROR")


    def get_hyper_file(self):
        #filename = QtGui.QFileDialog.getOpenFileName(self.Form, 'Load Hyper Parameters', filter="txt (*.npy *.)")
        filename = QtGui.QFileDialog.getOpenFileName(self.Form, 'Load Hyper Parameters',
        self.Form.optimizer_path  + "parameters", "txt (*.npy)", QtGui.QFileDialog.DontUseNativeDialog)
        if filename:
            self.Form.hyper_file = str(filename)
            self.pb_hyper_file.setText(self.Form.hyper_file)
            # print(filename)

    def rewrite_default(self):
        #self.Form.set_file = "default.json"
        self.save_state(self.Form.set_file)

    def logbook(self, widget):
        """
        Method to send Optimization parameters + screenshot to eLogboob
        :return:
        """

        filename = "screenshot"
        filetype = "png"
        #self.screenShot(filename, filetype)

        # curr_time = datetime.now()
        # timeString = curr_time.strftime("%Y-%m-%dT%H:%M:%S")
        text = ""


        #screenshot = open(self.Form.optimizer_path + filename + "." + filetype, 'rb')
        
        screenshot = self.get_screenshot(widget)
        #res = send_to_desy_elog(author="", title="OCELOT Correction tool", severity="INFO", text=text, elog=self.Form.logbook,
        #                  image=screenshot.read())
        
        res = send_to_desy_elog(author="", title="OCELOT Correction tool", severity="INFO", text=text, elog=self.Form.logbook,
                          image=screenshot)

        if not res:
            self.Form.error_box("error during eLogBook sending")

    def get_screenshot(self, window_widget):
        screenshot_tmp = QtCore.QByteArray()
        screeshot_buffer = QtCore.QBuffer(screenshot_tmp)
        screeshot_buffer.open(QtCore.QIODevice.WriteOnly)
        widget = QtWidgets.QWidget.grab(window_widget)
        widget.save(screeshot_buffer, "png")
        return screenshot_tmp.toBase64().data().decode()

    def screenShot(self, filename, filetype):

        """
        Takes a screenshot of the whole gui window, saves png and ps images to file
        :param filename: (str) Directory string of where to save the file
        :param filetype: (str) String of the filetype to save
        :return:
        """

        s = str(filename) + "." + str(filetype)
        p = QScreen.grabWindow(self.Form.winId())
        p.save(s, 'png')
        # im = Image.open(s)
        # im.save(s[:-4]+".ps")
        p = p.scaled(465, 400)
        # save again a small image to use for the logbook thumbnail
        p.save(str(s[:-4]) + "_sm.png", 'png')

    def get_style_name_index(self):
        # pvs = self.ui.widget.pvs
        # check if file here
        if not os.path.isfile(self.settings_file):
            return 0

        with open(self.settings_file, 'r') as f:
            table = json.load(f)
        if "style" in table.keys():

            return table["style"]
        else:
            return 0

    def loadStyleSheet(self, filename="dark.css"):
        """
        Sets the dark GUI theme from a css file.
        :return:
        """
        try:

            #self.cssfile = self.Form.gui_dir + filename
            with open(filename, "r") as f:
                self.Form.setStyleSheet(f.read())
        except IOError:
            print ('No style sheet found!')


    def open_help(self):
        """
        method to open the Help in the webbrowser
        :return: None
        """

        if sys.platform == 'win32':
            url = self.Form.optimizer_path+"docs\\_build\\html\\index.html"
            #os.startfile(url)
            webbrowser.open(url)
        elif sys.platform == 'darwin':
            url = "file://"+self.Form.optimizer_path+"docs/_build/html/index.html"
            webbrowser.open(url)
            #subprocess.Popen(['open', url])
        else:
            url = "file://" + self.Form.optimizer_path + "docs/_build/html/index.html"
            try:
                subprocess.Popen(['xdg-open', url])
            except OSError:
                print('Please open a browser on: ' + url)

