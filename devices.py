"""
Sergey Tomin, XFEL/DESY, 2017
"""
from ocelot.optimizer.mint.opt_objects import Device
from PyQt5 import QtGui, QtCore
import numpy as np
import time
import logging
logger = logging.getLogger(__name__)

class Corrector(Device):
    def __init__(self, eid=None, server="XFEL", subtrain="SA1"):
        super(Corrector, self).__init__(eid=eid)
        self.subtrain = subtrain
        self.server = server

    def set_value(self, val):
        #self.values.append(val)
        #self.times.append(time.time())
        ch = self.server + ".MAGNETS/MAGNET.ML/" + self.eid + "/KICK_MRAD.SP"
        self.mi.set_value(ch, val)

    def get_value(self):
        ch = self.server + ".MAGNETS/MAGNET.ML/" + self.eid + "/KICK_MRAD.SP"
        val = self.mi.get_value(ch)
        return val

    def get_limits(self):
        ch_min = self.server+ ".MAGNETS/MAGNET.ML/" + self.id + "/MIN_KICK"
        min_kick = self.mi.get_value(ch_min)
        ch_max = self.server + ".MAGNETS/MAGNET.ML/" + self.id + "/MAX_KICK"
        max_kick = self.mi.get_value(ch_max)
        return [min_kick*1000, max_kick*1000]

class MITwiss(Device):
    def __init__(self, eid=None, server="XFEL", subtrain="SA1"):
        super(MITwiss, self).__init__(eid=eid)
        self.subtrain = subtrain
        self.server = server

    def get_tws(self, section):
        ch_beta_x =  self.server + ".UTIL/BEAM_PARAMETER/" + section + "/PROJECTED_X.BETA." + self.subtrain
        ch_alpha_x = self.server + ".UTIL/BEAM_PARAMETER/" + section + "/PROJECTED_X.ALPHA." + self.subtrain
        ch_beta_y =  self.server + ".UTIL/BEAM_PARAMETER/" + section + "/PROJECTED_Y.BETA." + self.subtrain
        ch_alpha_y = self.server + ".UTIL/BEAM_PARAMETER/" + section + "/PROJECTED_Y.ALPHA." + self.subtrain
        #ch_energy =  "XFEL.UTIL/BEAM_PARAMETER/" + section + "/PROJECTED_X.ENERGY.SA1"
        tws_dict = {}
        tws_dict['beta_x'] = self.mi.get_value(ch_beta_x)
        tws_dict['beta_y'] = self.mi.get_value(ch_beta_y)
        tws_dict['alpha_x']  = self.mi.get_value(ch_alpha_x)
        tws_dict['alpha_y']  = self.mi.get_value(ch_alpha_y)
        return tws_dict

class MPS(Device):
    def __init__(self, eid=None, server="XFEL", subtrain="SA1"):
        super(MPS, self).__init__(eid=eid)
        self.subtrain = subtrain
        self.server = server

    def beam_off(self):
        self.mi.set_value(self.server + ".UTIL/BUNCH_PATTERN/SA1/BEAM_ALLOWED", 0)

    def beam_on(self):
        self.mi.set_value(self.server + ".UTIL/BUNCH_PATTERN/SA1/BEAM_ALLOWED", 1)

    def num_bunches_requested(self, num_bunches=1):
        self.mi.set_value(self.server + ".UTIL/BUNCH_PATTERN/SA1/NUM_BUNCHES_REQUESTED", num_bunches)


class CavityA1(Device):
    def __init__(self, eid, server="XFEL", subtrain="SA1"):
        super(CavityA1, self).__init__(eid=eid)
        self.subtrain = subtrain
        self.server = server

    def set_value(self, val):
        ch = self.server + ".RF/LLRF.CONTROLLER/" + self.eid + "/SP.AMPL"
        self.mi.set_value(ch, val)
        logger.debug("CavityA1, ch: " + ch + " V = " + str(val))

    def get_value(self):
        ch = self.server + ".RF/LLRF.CONTROLLER/" + self.eid + "/SP.AMPL"
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
    def __init__(self, eid, server="XFEL", subtrain="SA1"):
        super(BPM, self).__init__(eid=eid)
        self.subtrain = subtrain
        self.server = server

    def get_pos(self):
        ch_x = self.server + ".DIAG/BPM/" + self.eid + "/X." + self.subtrain
        ch_y = self.server + ".DIAG/BPM/" + self.eid + "/Y." + self.subtrain
        #print(ch_x, ch_y)
        x = self.mi.get_value(ch_x)
        y = self.mi.get_value(ch_y)
        #print(x, y)
        return x, y

    def get_charge(self):
        x = self.mi.get_value(self.server + ".DIAG/BPM/" + self.eid + "/CHARGE." + self.subtrain)
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
    def __init__(self, eid=None, server="XFEL", subtrain="SA1"):
        super(MICavity, self).__init__(eid=eid)
        self.subtrain = subtrain
        self.server = server

    def get_value(self):
        #C.A3.1.1.L2
        #M4.A4.L2
        parts = self.eid.split(".")
        eid = "M"+parts[2]+"."+parts[1]+"."+parts[4]
        ch = self.server + ".RF/LLRF.ENERGYGAIN.ML/" + eid + "/ENERGYGAIN." + self.subtrain
        val = self.mi.get_value(ch)/8.
        return val


class MIOrbit(Device):
    def __init__(self, eid=None, server="XFEL", subtrain="SA1"):
        super(MIOrbit, self).__init__(eid=eid)
        self.subtrain = subtrain
        self.server = server
        self.bpm_server = "BPM" # "ORBIT"     # or "BPM"
        self.time_delay = 0.1         # sec
        self.charge_threshold = 0.005 # nC
        self.subtrain = subtrain
        self.bpm_names = []
        self.x = []
        self.y = []
        self.mean_x = []
        self.mena_y = []
        self.mean_charge = []
        #self.charge = []

    def read_positions(self):
        try:
            orbit_x = self.mi.get_value(self.server + ".DIAG/" + self.bpm_server + "/*/X." + self.subtrain)
            orbit_y = self.mi.get_value(self.server + ".DIAG/" + self.bpm_server + "/*/Y." + self.subtrain)
        except Exception as e:
            logger.critical("read_positions: self.mi.get_value: " + e)
            raise e
        #    print("ERROR: reading from DOOCS")
        #    return False
        #print(orbit_x)
        try:
            names_x = [data["str"] for data in orbit_x]
            names_y = [data["str"] for data in orbit_y]
        except Exception as e:
            logger.critical("read_positions: names_x = [data['str'] for data in orbit_x]" + str(e))
            raise e

        if not np.array_equal(names_x, names_y):
            logger.warning(" MIOrbit: read_positions: X and Y orbits are not equal")
        self.x = np.array([data["float"] for data in orbit_x])
        self.y = np.array([data["float"] for data in orbit_y])
        return [names_x, self.x, self.y]

    def read_charge(self):
        #try:
        charge = self.mi.get_value(self.server + ".DIAG/BPM/*/CHARGE." + self.subtrain)
        #except:
        #    print("ERROR: reading from DOOCS")
        #    return False
        names = [data["str"] for data in charge]
        values = np.array([data["float"] for data in charge])
        return names, values

    def read_orbit(self):
        names_xy, x, y = self.read_positions()
        names_charge, charge = self.read_charge()
        #print(names_xy)
        #print(names_charge)
        if not np.array_equal(names_xy, names_charge):
            logger.warning(" MIOrbit: read_orbit: CHARGE reading and POSITIONS are not equal")
            #return False
        return names_xy, x, y, charge


    def read_and_average(self, nreadings, take_last_n):
        orbits_x = []
        orbits_y = []
        orbits_charge = []
        saved_names = []
        for i in range(nreadings):
            names, x, y, charge = self.read_orbit()
            orbits_x.append(x)
            orbits_y.append(y)
            orbits_charge.append(charge)
            if i > 0:
                if not np.array_equal(saved_names, names):
                    logger.warning(" MIOrbit: read_and_average: error: arrays are different ")
            saved_names = names
            time.sleep(self.time_delay)
        self.bpm_names = saved_names
        self.mean_x = np.mean(orbits_x[-take_last_n:], axis=0)
        self.mean_y = np.mean(orbits_y[-take_last_n:], axis=0)
        self.mean_charge = np.mean(orbits_charge[-take_last_n:], axis=0)
        return self.bpm_names, self.mean_x, self.mean_y, self.mean_charge

    def get_bpms(self, bpms):
        """
        All bpm works with [m] but doocs gives position in [mm]

        :param bpms: list of BPM objects
        :param charge_threshold:
        :return:
        """
        if len(self.bpm_names) == 0:
            return False
        #bpm_names = [bpm.id for bpm in bpms]
        indxs = []
        valid_bpm_inx = []
        for i, bpm in enumerate(bpms):
            if bpm.id not in self.bpm_names:
                bpm.ui.uncheck()
            else:
                valid_bpm_inx.append(i)
                indxs.append(self.bpm_names.index(bpm.id))
                logger.debug(" MIOrbit: get_bpms: len(bpm)="+ str(len(bpms)) + "  len(indxs) = " + str(len(indxs)))
        bpms = [bpms[indx] for indx in valid_bpm_inx]
        for i, bpm in enumerate(bpms):
            inx = indxs[i]
            bpm.x = self.mean_x[inx]/1000      # [mm] -> [m]
            bpm.y = self.mean_y[inx]/1000      # [mm] -> [m]
            bpm.charge = self.mean_charge[inx] # nC
        return True

class MIAdviser(Device):
    def __init__(self, eid=None, server="XFEL", subtrain="SA1"):
        super(MIAdviser, self).__init__(eid=eid)
        self.bpm_server = "BPM"  # "ORBIT"     # or "BPM"
        self.subtrain = subtrain
        self.server = server

    def get_x(self):
        try:
            self.orbit_x = self.mi.get_value(self.server + ".DIAG/" + self.bpm_server + "/*/X." + self.subtrain)
        except Exception as e:
            logger.info("get_x: self.mi.get_value: " + str(e))
            self.orbit_x = []

    def get_y(self):
        try:
            self.orbit_y = self.mi.get_value(self.server + ".DIAG/" + self.bpm_server + "/*/Y." + self.subtrain)
        except Exception as e:
            logger.info("get_y: self.mi.get_value: " + str(e))
            self.orbit_y = []
        
    def get_bpm_z_pos(self):
        try:
            self.bpm_z_pos = self.mi.get_value(self.server + ".DIAG/" + self.bpm_server + "/*/Z_POS")
        except Exception as e:
            logger.info("get_bpm_z_pos: self.mi.get_value: " + str(e))
            self.bpm_z_pos = []
        #print(self.bpm_z_pos)

    def get_kicks(self):
        #"XFEL.MAGNETS/MAGNET.ML/" + self.eid + "/KICK_MRAD.SP"
        try:
            self.kicks = self.mi.get_value(self.server + ".MAGNETS/MAGNET.ML/*/KICK_MRAD.SP")
        except Exception as e:
            logger.critical("get_kicks: self.mi.get_value: " + str(e))
            raise e

    def get_momentums(self):
        #"XFEL.MAGNETS/MAGNET.ML/" + self.eid + "/KICK_MRAD.SP"
        try:
            self.moments = self.mi.get_value(self.server + ".MAGNETS/MAGNET.ML/*/MOMENTUM.SP")
        except Exception as e:
            logger.critical("get_momentums: self.mi.get_value: " + str(e))
            raise e

    def get_cor_z_pos(self):
        try:
            self.cor_z_pos = self.mi.get_value("XFEL.MAGNETS/MAGNET.ML/*/Z_POS")
        except Exception as e:
            logger.info("get_cor_z_pos: self.mi.get_value: " + str(e))
            self.cor_z_pos = []

    def get_corrs(self, ref_names):

        self.get_kicks()
        self.get_momentums()
        self.get_cor_z_pos()
        names = [x["str"] for x in self.kicks]
        kicks = np.array([x["float"] for x in self.kicks])/1000.
        moments = np.array([x["float"] for x in self.moments])
        z_poss = np.array([x["float"] for x in self.cor_z_pos])
        indxs = []
        for name in ref_names:
            indxs.append(names.index(name))
        return kicks[indxs], moments[indxs], z_poss[indxs]

    def get_bpm_z_from_ref(self, ref_names):
        self.get_bpm_z_pos()
        names = [x["str"] for x in self.bpm_z_pos]
        z_poss = np.array([x["float"] for x in self.bpm_z_pos])
        indxs = []
        for name in ref_names:
            indxs.append(names.index(name))
        
        return z_poss[indxs]
        
    def get_bpm_x(self, ref_names):

        self.get_x()
        if len(self.orbit_x) == 0:
            return None
        names = [x["str"] for x in self.orbit_x]
        pos = np.array([x["float"] for x in self.orbit_x])

        indxs = []
        for name in ref_names:
            indxs.append(names.index(name))
        
        z_pos = self.get_bpm_z_from_ref(ref_names)
        return pos[indxs], z_pos

    def get_bpm_y(self, ref_names):

        self.get_y()
        #self.get_bpm_z_pos()

        if len(self.orbit_y) == 0:
            return None

        names = [x["str"] for x in self.orbit_y]
        pos = np.array([x["float"] for x in self.orbit_y])
        #z_poss = np.array([x["float"] for x in self.bpm_z_pos])

        indxs = []
        for name in ref_names:
            indxs.append(names.index(name))
            
        z_pos = self.get_bpm_z_from_ref(ref_names)
        return pos[indxs], z_pos

class MIStandardFeedback(Device):
    def __init__(self, eid=None, server="XFEL", subtrain="SA1"):
        super(MIStandardFeedback, self).__init__(eid=eid)
        self.subtrain = subtrain
        self.server = server

    def is_running(self):
        status = self.mi.get_value(self.server + ".FEEDBACK/ORBIT.SA1/ORBITFEEDBACK/ACTIVATE_FB")
        return status
        