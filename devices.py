"""
Sergey Tomin, XFEL/DESY, 2017
"""
from ocelot.optimizer.mint.opt_objects import Device
from PyQt4 import QtGui, QtCore
import numpy as np


class Corrector(Device):

    def set_value(self, val):
        #self.values.append(val)
        #self.times.append(time.time())
        ch = "XFEL.MAGNETS/MAGNET.ML/" + self.eid + "/KICK_MRAD.SP"
        self.mi.set_value(ch, val)

    def get_value(self):
        ch = "XFEL.MAGNETS/MAGNET.ML/" + self.eid + "/KICK_MRAD.SP"
        val = self.mi.get_value(ch)
        return val

    def get_limits(self):
        ch_min = "XFEL.MAGNETS/MAGNET.ML/" + self.id + "/MIN_KICK"
        min_kick = self.mi.get_value(ch_min)
        ch_max = "XFEL.MAGNETS/MAGNET.ML/" + self.id + "/MAX_KICK"
        max_kick = self.mi.get_value(ch_max)
        return [min_kick*1000, max_kick*1000]

class CavityA1(Device):
    def __init__(self, eid):
        super(CavityA1, self).__init__(eid=eid)

    def set_value(self, val):
        ch = "XFEL.RF/LLRF.CONTROLLER/" + self.eid + "/SP.AMPL"
        self.mi.set_value(ch, val)
        print(ch, "V = ", val)

    def get_value(self):
        ch = "XFEL.RF/LLRF.CONTROLLER/" + self.eid + "/SP.AMPL"
        val = self.mi.get_value(ch)
        return val


class BPMUI:
    def __init__(self, ui=None):
        self.tableWidget = None
        self.row = 0
        self.col = 0
        self.alarm = False

    def get_value(self):
        x = float(self.tableWidget.item(self.row, 1).text())
        y = float(self.tableWidget.item(self.row, 2).text())
        return (x, y)

    def set_value(self, val):
        x = val[0]
        y = val[1]
        x = np.round(x, 4)
        y = np.round(y, 4)
        self.tableWidget.item(self.row, 1).setText(str(x))
        self.tableWidget.item(self.row, 2).setText(str(y))
        self.check_values(val)

    def check_values(self, vals):
        if np.max(np.abs(vals)) > 15.:
            self.tableWidget.item(self.row, 1).setBackground(QtGui.QColor(255, 0, 0))  # red
            self.tableWidget.item(self.row, 2).setBackground(QtGui.QColor(255, 0, 0))  # red
            self.alarm = True
        elif vals[0] == 0 and vals[1] == 0:
            self.tableWidget.item(self.row, 1).setBackground(QtGui.QColor(255, 0, 0))  # red
            self.tableWidget.item(self.row, 2).setBackground(QtGui.QColor(255, 0, 0))  # red
            self.alarm = True
        else:
            self.tableWidget.item(self.row, 1).setBackground(QtGui.QColor(89, 89, 89))  # grey
            self.tableWidget.item(self.row, 2).setBackground(QtGui.QColor(89, 89, 89))  # grey
            self.alarm = False

    def set_init_value(self, val):
        self.tableWidget.item(self.row, 1).setText(str(val))

    def get_init_value(self):
        return float(self.tableWidget.item(self.row, 1).text())

    def uncheck(self):
        item = self.tableWidget.item(self.row, 3)
        item.setCheckState(False)

    def check(self):
        item = self.tableWidget.item(self.row, 3)
        item.setCheckState(QtCore.Qt.Checked)

    def state(self):
        item = self.tableWidget.item(self.row, 3)
        state = item.checkState()
        return state

    def set_hide(self, hide):
        #if hide:
        #    self.uncheck()
        #else:
        #    self.check()
        self.tableWidget.setRowHidden(self.row, hide)


class BPM(Device):

    def get_pos(self):
        ch_x = "XFEL.DIAG/BPM/" + self.eid + "/X.SA1"
        ch_y = "XFEL.DIAG/BPM/" + self.eid + "/Y.SA1"
        #print(ch_x, ch_y)
        x = self.mi.get_value(ch_x)
        y = self.mi.get_value(ch_y)
        #print(x, y)
        return x, y

    def get_charge(self):
        x = self.mi.get_value("XFEL.DIAG/BPM/" + self.eid + "/CHARGE.SA1")
        return x

class DeviceUI:
    def __init__(self, ui=None):
        self.tableWidget = None
        self.row = 0
        self.col = 0
        self.alarm = False

    def get_value(self):
        return self.tableWidget.cellWidget(self.row, self.col).value()

    def set_value(self, val):
        self.tableWidget.cellWidget(self.row, self.col).setValue(val)

    def set_init_value(self, val):
        val = np.round(val, 4) # "{:1.4e}".format(val)
        self.tableWidget.item(self.row, 1).setText(str(val))

    def get_init_value(self):
        return float(self.tableWidget.item(self.row, 1).text())

    def uncheck(self):
        item = self.tableWidget.item(self.row, 3)
        item.setCheckState(False)

    def check(self):
        item = self.tableWidget.item(self.row, 3)
        item.setCheckState(QtCore.Qt.Checked)

    def state(self):
        item = self.tableWidget.item(self.row, 3)
        state = item.checkState()
        return state

    def check_values(self, val, lims, warn=False):
        if warn:
            self.tableWidget.item(self.row, 0).setBackground(QtGui.QColor(255, 255, 0))  # yellow
        else:
            #print("grey")
            self.tableWidget.item(self.row, 0).setBackground(QtGui.QColor(89, 89, 89))  # grey
        self.alarm = False
        if not(lims[0]<= val <=lims[1]):
            self.tableWidget.item(self.row, 0).setBackground(QtGui.QColor(255, 0, 0))  # red
            self.alarm = True

    def set_hide(self, hide):
        #if hide and uncheck:
        #    self.uncheck()
        #else:
        #    self.check()
        self.tableWidget.setRowHidden(self.row, hide)

class MICavity(Device):
    def __init__(self, eid=None):
        super(MICavity, self).__init__(eid=eid)

    def get_value(self):
        #C.A3.1.1.L2
        #M4.A4.L2
        parts = self.eid.split(".")
        eid = "M"+parts[2]+"."+parts[1]+"."+parts[4]
        print(eid)
        ch = "XFEL.RF/LLRF.ENERGYGAIN.ML/" + eid + "/ENERGYGAIN.SA1"
        val = self.mi.get_value(ch)/8.
        return val

