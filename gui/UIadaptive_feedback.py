# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIadaptive_feedback.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1223, 861)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # Form.setStyleSheet("background-color: white")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_7.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.widget_2 = QtWidgets.QWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(300, 200))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_7.addWidget(self.widget_2, 0, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 205))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.le_b = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_b.setFont(font)
        self.le_b.setObjectName("le_b")
        self.gridLayout_3.addWidget(self.le_b, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)
        self.le_c = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_c.setFont(font)
        self.le_c.setObjectName("le_c")
        self.gridLayout_3.addWidget(self.le_c, 2, 1, 1, 1)
        self.le_a = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_a.setFont(font)
        self.le_a.setObjectName("le_a")
        self.gridLayout_3.addWidget(self.le_a, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.le_of = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_of.setFont(font)
        self.le_of.setObjectName("le_of")
        self.gridLayout_3.addWidget(self.le_of, 3, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 1, 1, 1, 1)
        self.sb_sr_delay = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_sr_delay.setFont(font)
        self.sb_sr_delay.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_sr_delay.setDecimals(2)
        self.sb_sr_delay.setMinimum(0.1)
        self.sb_sr_delay.setMaximum(10.0)
        self.sb_sr_delay.setSingleStep(0.1)
        self.sb_sr_delay.setProperty("value", 0.3)
        self.sb_sr_delay.setObjectName("sb_sr_delay")
        self.gridLayout_8.addWidget(self.sb_sr_delay, 0, 2, 1, 1)
        self.sb_sr_period = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_sr_period.setFont(font)
        self.sb_sr_period.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_sr_period.setMinimum(1.0)
        self.sb_sr_period.setMaximum(100.0)
        self.sb_sr_period.setSingleStep(0.1)
        self.sb_sr_period.setProperty("value", 3.0)
        self.sb_sr_period.setObjectName("sb_sr_period")
        self.gridLayout_8.addWidget(self.sb_sr_period, 2, 2, 1, 1)
        self.sb_sr_noise_amp = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_sr_noise_amp.setFont(font)
        self.sb_sr_noise_amp.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_sr_noise_amp.setDecimals(1)
        self.sb_sr_noise_amp.setMaximum(1000.0)
        self.sb_sr_noise_amp.setSingleStep(1.0)
        self.sb_sr_noise_amp.setProperty("value", 10.0)
        self.sb_sr_noise_amp.setObjectName("sb_sr_noise_amp")
        self.gridLayout_8.addWidget(self.sb_sr_noise_amp, 1, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 0, 1, 1, 1)
        self.pb_active_search = QtWidgets.QPushButton(self.groupBox_3)
        self.pb_active_search.setStyleSheet("color: rgb(85, 255, 127)")
        self.pb_active_search.setObjectName("pb_active_search")
        self.gridLayout_8.addWidget(self.pb_active_search, 3, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 2, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_3, 1, 1, 1, 1)
        self.pb_start_feedback = QtWidgets.QPushButton(self.tab)
        self.pb_start_feedback.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pb_start_feedback.setFont(font)
        self.pb_start_feedback.setStyleSheet("color: rgb(85, 255, 127);")
        self.pb_start_feedback.setObjectName("pb_start_feedback")
        self.gridLayout_7.addWidget(self.pb_start_feedback, 4, 0, 1, 1)
        self.pb_start_statistics = QtWidgets.QPushButton(self.tab)
        self.pb_start_statistics.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pb_start_statistics.setFont(font)
        self.pb_start_statistics.setStyleSheet("color: rgb(85, 255, 127);")
        self.pb_start_statistics.setObjectName("pb_start_statistics")
        self.gridLayout_7.addWidget(self.pb_start_statistics, 4, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_9.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.le_warn = QtWidgets.QLineEdit(self.groupBox_4)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.le_warn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_warn.setFont(font)
        self.le_warn.setObjectName("le_warn")
        self.gridLayout_9.addWidget(self.le_warn, 1, 0, 1, 3)
        self.cb_update_display = QtWidgets.QCheckBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_update_display.setFont(font)
        self.cb_update_display.setChecked(False)
        self.cb_update_display.setObjectName("cb_update_display")
        self.gridLayout_9.addWidget(self.cb_update_display, 0, 2, 1, 1)
        self.cb_freeze_adapt = QtWidgets.QCheckBox(self.groupBox_4)
        self.cb_freeze_adapt.setObjectName("cb_freeze_adapt")
        self.gridLayout_9.addWidget(self.cb_freeze_adapt, 0, 0, 1, 2)
        self.gridLayout_7.addWidget(self.groupBox_4, 3, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_10.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.cb_load_settings = QtWidgets.QComboBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_load_settings.sizePolicy().hasHeightForWidth())
        self.cb_load_settings.setSizePolicy(sizePolicy)
        self.cb_load_settings.setObjectName("cb_load_settings")
        self.gridLayout_10.addWidget(self.cb_load_settings, 0, 1, 1, 2)
        self.gridLayout_7.addWidget(self.groupBox_5, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.widget_sase = QtWidgets.QWidget(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_sase.sizePolicy().hasHeightForWidth())
        self.widget_sase.setSizePolicy(sizePolicy)
        self.widget_sase.setObjectName("widget_sase")
        self.gridLayout_13.addWidget(self.widget_sase, 2, 0, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_13.addWidget(self.label_15, 0, 0, 1, 1)
        self.slider = QtWidgets.QSlider(self.tab_3)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.gridLayout_13.addWidget(self.slider, 1, 0, 1, 2)
        self.widget_orbit = QtWidgets.QWidget(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_orbit.sizePolicy().hasHeightForWidth())
        self.widget_orbit.setSizePolicy(sizePolicy)
        self.widget_orbit.setMinimumSize(QtCore.QSize(0, 300))
        self.widget_orbit.setObjectName("widget_orbit")
        self.gridLayout_13.addWidget(self.widget_orbit, 4, 0, 3, 1)
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_13.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_13.addWidget(self.label_17, 3, 1, 1, 1)
        self.widget_cor_tab = OclTable(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_cor_tab.sizePolicy().hasHeightForWidth())
        self.widget_cor_tab.setSizePolicy(sizePolicy)
        self.widget_cor_tab.setMinimumSize(QtCore.QSize(0, 300))
        self.widget_cor_tab.setObjectName("widget_cor_tab")
        self.gridLayout_13.addWidget(self.widget_cor_tab, 4, 1, 3, 1)
        self.pb_restore = QtWidgets.QPushButton(self.tab_3)
        self.pb_restore.setObjectName("pb_restore")
        self.gridLayout_13.addWidget(self.pb_restore, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 205))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.sb_array_len = QtWidgets.QSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_array_len.setFont(font)
        self.sb_array_len.setMaximum(5000)
        self.sb_array_len.setSingleStep(10)
        self.sb_array_len.setProperty("value", 100)
        self.sb_array_len.setObjectName("sb_array_len")
        self.gridLayout_5.addWidget(self.sb_array_len, 0, 1, 1, 1)
        self.sb_averaging = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_averaging.setFont(font)
        self.sb_averaging.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_averaging.setMaximum(100.0)
        self.sb_averaging.setSingleStep(10.0)
        self.sb_averaging.setProperty("value", 10.0)
        self.sb_averaging.setObjectName("sb_averaging")
        self.gridLayout_5.addWidget(self.sb_averaging, 2, 1, 1, 1)
        self.sb_time_delay = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_time_delay.setFont(font)
        self.sb_time_delay.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_time_delay.setMaximum(10.0)
        self.sb_time_delay.setSingleStep(0.01)
        self.sb_time_delay.setProperty("value", 0.1)
        self.sb_time_delay.setObjectName("sb_time_delay")
        self.gridLayout_5.addWidget(self.sb_time_delay, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)
        self.sb_go_recalc_delay = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_go_recalc_delay.setFont(font)
        self.sb_go_recalc_delay.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_go_recalc_delay.setMinimum(1.0)
        self.sb_go_recalc_delay.setMaximum(100.0)
        self.sb_go_recalc_delay.setSingleStep(1.0)
        self.sb_go_recalc_delay.setProperty("value", 1.0)
        self.sb_go_recalc_delay.setObjectName("sb_go_recalc_delay")
        self.gridLayout_5.addWidget(self.sb_go_recalc_delay, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 3, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_11.addWidget(self.label_12, 1, 1, 1, 1)
        self.sb_ref_orbit_nread = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_ref_orbit_nread.setFont(font)
        self.sb_ref_orbit_nread.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_ref_orbit_nread.setDecimals(0)
        self.sb_ref_orbit_nread.setMinimum(1.0)
        self.sb_ref_orbit_nread.setMaximum(100.0)
        self.sb_ref_orbit_nread.setSingleStep(1.0)
        self.sb_ref_orbit_nread.setProperty("value", 1.0)
        self.sb_ref_orbit_nread.setObjectName("sb_ref_orbit_nread")
        self.gridLayout_11.addWidget(self.sb_ref_orbit_nread, 0, 2, 1, 1)
        self.sb_feedback_rep = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_feedback_rep.setFont(font)
        self.sb_feedback_rep.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_feedback_rep.setMinimum(1.0)
        self.sb_feedback_rep.setMaximum(100.0)
        self.sb_feedback_rep.setSingleStep(1.0)
        self.sb_feedback_rep.setProperty("value", 3.0)
        self.sb_feedback_rep.setObjectName("sb_feedback_rep")
        self.gridLayout_11.addWidget(self.sb_feedback_rep, 2, 2, 1, 1)
        self.sb_afeed_fraction = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_afeed_fraction.setFont(font)
        self.sb_afeed_fraction.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_afeed_fraction.setMaximum(1.0)
        self.sb_afeed_fraction.setSingleStep(0.1)
        self.sb_afeed_fraction.setProperty("value", 0.7)
        self.sb_afeed_fraction.setObjectName("sb_afeed_fraction")
        self.gridLayout_11.addWidget(self.sb_afeed_fraction, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_11.addWidget(self.label_13, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_11.addWidget(self.label_14, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_6, 2, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(600, 0))
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.pb_save_settings = QtWidgets.QPushButton(self.tab_2)
        self.pb_save_settings.setStyleSheet("color: rgb(255, 0, 0);")
        self.pb_save_settings.setObjectName("pb_save_settings")
        self.gridLayout_12.addWidget(self.pb_save_settings, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem, 1, 1, 1, 1)
        self.pb_settings = QtWidgets.QPushButton(self.tab_2)
        self.pb_settings.setEnabled(False)
        self.pb_settings.setObjectName("pb_settings")
        self.gridLayout_12.addWidget(self.pb_settings, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_12, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ocelot Interface"))
        self.groupBox.setTitle(_translate("Form", "Objective Function"))
        self.label_6.setText(_translate("Form", "Objective Function   "))
        self.label.setText(_translate("Form", "A:"))
        self.label_4.setText(_translate("Form", "B:"))
        self.label_5.setText(_translate("Form", "C:"))
        self.groupBox_3.setTitle(_translate("Form", "Active search"))
        self.label_10.setText(_translate("Form", "Noise amplitude [urad]"))
        self.label_11.setText(_translate("Form", "Delay between sets [s]"))
        self.pb_active_search.setText(_translate("Form", "Start Search"))
        self.label_8.setText(_translate("Form", "Period [s]  "))
        self.pb_start_feedback.setText(_translate("Form", "Start Feedback"))
        self.pb_start_statistics.setText(_translate("Form", "Statistics Accum On"))
        self.groupBox_4.setTitle(_translate("Form", "Indication"))
        self.cb_update_display.setText(_translate("Form", "Update Main Display"))
        self.cb_freeze_adapt.setText(_translate("Form", "Freeze Adaptation"))
        self.groupBox_5.setTitle(_translate("Form", "Load Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Adaptive FB"))
        self.label_15.setText(_translate("Form", "Data Explorrer "))
        self.label_16.setText(_translate("Form", "Orbit"))
        self.label_17.setText(_translate("Form", "Correctors"))
        self.pb_restore.setText(_translate("Form", "Restore Correctors"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Data Browser"))
        self.groupBox_2.setTitle(_translate("Form", "Statistics Data Control"))
        self.label_3.setText(_translate("Form", "Reading Delay (s)"))
        self.label_2.setText(_translate("Form", "Array Length"))
        self.label_7.setText(_translate("Form", "Averaging Over (%)"))
        self.label_9.setText(_translate("Form", "Recalculate GO (s)"))
        self.groupBox_6.setTitle(_translate("Form", "Correction control"))
        self.label_12.setText(_translate("Form", "Apply Fraction"))
        self.label_13.setText(_translate("Form", "Ref Orbit avaraging over last (readings)"))
        self.label_14.setText(_translate("Form", "Apply Feedback Every s  "))
        self.pb_save_settings.setText(_translate("Form", "Save config"))
        self.pb_settings.setText(_translate("Form", "Settimgs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Expert"))

from gui.tables.ocl_table import OclTable

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

