"""
Sergey Tomin. XFEL/DESY, 2017.
"""

import pyqtgraph as pg
from PyQt4 import QtGui, QtCore
import numpy as np
from ocelot import *
from ocelot.optimizer.mint.opt_objects import Device
from ocelot.cpbd.track import *
import time
from ocelot.cpbd.orbit_correction import NewOrbit, OrbitSVD
from ocelot.cpbd.response_matrix import *


class Corrector(Device):

    def set_value(self, val):
        #self.values.append(val)
        #self.times.append(time.time())
        ch = "XFEL_SIM.MAGNETS/MAGNET.ML/" + self.eid + "/KICK_MRAD.SP"
        self.mi.set_value(ch, val)

    def get_value(self):
        ch = "XFEL_SIM.MAGNETS/MAGNET.ML/" + self.eid + "/KICK_MRAD.SP"
        val = self.mi.get_value(ch)
        return val

    def get_limits(self):
        ch_min = "XFEL_SIM.MAGNETS/MAGNET.ML/" + self.id + "/MIN_KICK"
        min_kick = self.mi.get_value(ch_min)
        ch_max = "XFEL_SIM.MAGNETS/MAGNET.ML/" + self.id + "/MAX_KICK"
        max_kick = self.mi.get_value(ch_max)
        return [min_kick*1000, max_kick*1000]

class CavityA1(Device):
    def set_value(self, val):
        ch = "XFEL_SIM.RF/LLRF.CONTROLLER/" + self.eid + "/SP.AMPL"
        self.mi.set_value(ch, val)

    def get_value(self):
        ch = "XFEL_SIM.RF/LLRF.CONTROLLER/" + self.eid + "/SP.AMPL"
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

    def check_values(self, val):
        if np.max(np.abs(val)) > 15.:
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
        ch_x = "XFEL_SIM.DIAG/BPM/" + self.eid + "/X.SA1"
        ch_y = "XFEL_SIM.DIAG/BPM/" + self.eid + "/Y.SA1"
        #print(ch_x, ch_y)
        x = self.mi.get_value(ch_x)
        y = self.mi.get_value(ch_y)
        #print(x, y)
        return x, y


class OrbitInterface:
    def __init__(self, parent):
        self.parent = parent
        self.ui = parent.ui
        self.online_calc = True
        #self.corrs = self.parent.load_devices(types=[Vcor, Hcor])
        #self.parent.add_devs2table(devs=self.corrs, w_table=self.ui.table_cor )
        #self.add_orbit_plot()
        self.corrs = []
        self.hcors = []
        self.vcors = []
        self.s_bpm = []
        self.x_bpm = []
        self.y_bpm = []
        self.golden_orbit = {}
        self.p_init = None
        self.add_orbit_plot()
        self.ui.pb_check.clicked.connect(lambda: self.getRows(2, self.ui.table_cor))
        self.ui.pb_uncheck.clicked.connect(lambda: self.getRows(0, self.ui.table_cor))
        self.ui.pb_bpm_uncheck.clicked.connect(lambda: self.getRows(0, self.ui.table_bpm))
        self.ui.pb_bpm_check.clicked.connect(lambda: self.getRows(2, self.ui.table_bpm))
        self.ui.pb_read_orbit.clicked.connect(self.read_orbit)

        self.ui.pb_apply_kicks.clicked.connect(self.apply_kicks)

        self.ui.pb_calc_misal.clicked.connect(self.calc_misalignment_rm)
        self.ui.pb_calc_RM.clicked.connect(self.response_matrix)
        self.ui.pb_correct_orbit.clicked.connect(self.correct)
        self.ui.pb_reset_all.clicked.connect(self.reset_all)
        self.ui.cb_x_cors.stateChanged.connect(self.choose_plane)
        self.ui.cb_y_cors.stateChanged.connect(self.choose_plane)
        self.ui.sb_kick_weight.setValue(1)
        self.ui.pb_disp_meas.clicked.connect(self.dispersion_measurement)
        self.ui.pb_uncheck_red.clicked.connect(self.uncheck_red)

        self.ui.cb_online_orbit.stateChanged.connect(self.start_stop_live_orbit)
        self.ui.cb_golden_orbit.stateChanged.connect(self.start_stop_golden_orbit)
        self.ui.pb_set_golden.clicked.connect(self.set_golden_orbit)
        self.ui.pb_zero_gold.clicked.connect(self.set_zero_golden_orbit)

        self.response_matrix = ResponseMatrix()
        try:
            self.response_matrix.load("tld_r.json")
        except:
            print("No Response Matrix")

        self.disp_response_matrix = ResponseMatrix()
        try:
            self.disp_response_matrix.load("disp_tld.json")
        except:
            print("No Dispersion Response Matrix")

        self.cavity = CavityA1(eid="CTRL.A1.I1")
        self.cavity.mi = self.parent.mi
        #print("r_matrix", self.resp_matrix.matrix)
        #self.ui.pb_update_4.cliked.connect(self.save_orbit)

        #self.ui.sb_kick_weight.valueChanged.connect(self.scale)
        #self.ui.table_bpm.itemChanged.connect(self.update_plot)

        #self.ui.cb_coupler_kick.stateChanged.connect(self.calc_orbit)
        #self.loadStyleSheet()
    def uncheck_red(self):
        corrs = self.get_dev_from_cb_state(self.corrs)

        for cor in corrs:
            if cor.ui.alarm:
                cor.ui.uncheck()
        bpms = self.get_dev_from_cb_state(self.bpms)

        for bpm in bpms:
            if bpm.ui.alarm:
                bpm.ui.uncheck()

    def dispersion_measurement(self):
        self.create_Orbit_obj()
        disp_meas = LinacDisperseSimRM(lattice=copy.deepcopy(self.orbit.lat),
                                       hcors=copy.deepcopy(self.orbit.hcors),
                                    vcors=copy.deepcopy(self.orbit.vcors),
                                       bpms=copy.deepcopy(self.orbit.bpms))

        Dx0, Dy0 = disp_meas.read_virtual_dispersion(E0=self.parent.tws0.E)

        #print(Dx0)
        n_meas = 5
        x = np.zeros(len(self.orbit.bpms))
        y = np.zeros(len(self.orbit.bpms))
        for i in range(n_meas):
            for i, elem in enumerate(self.orbit.bpms):
                x_mm, y_mm = elem.mi.get_pos()
                x[i] += x_mm
                y[i] += y_mm
            time.sleep(0.2)
        x = x/n_meas
        y = y/n_meas

        V0 = self.cavity.get_value()
        dV = self.ui.sb_dV.value()
        V = V0 + dV
        self.cavity.set_value(V)
        time.sleep(4)
        x1 = np.zeros(len(self.orbit.bpms))
        y1 = np.zeros(len(self.orbit.bpms))
        for i in range(n_meas):
            for i, elem in enumerate(self.orbit.bpms):
                x_mm, y_mm = elem.mi.get_pos()
                x1[i] += x_mm
                y1[i] += y_mm
            time.sleep(0.2)
        x1 = x1 / n_meas
        y1 = y1 / n_meas
        dx = (x1 - x) / dV
        dy = (y1 - y) / dV

        for i, elem in enumerate(self.orbit.bpms):
            elem.Dx = dx[i]/1000
            elem.Dy = dy[i]/1000
            elem.Dx_des = Dx0[i]
            elem.Dy_des = Dy0[i]

        s_bpm = np.array([bpm.s for bpm in self.orbit.bpms]) + self.parent.lat_zi
        #x_bpm = np.array([bpm.Dx for bpm in self.orbit.bpms])*1000
        self.orb_x_ref.setData(x=s_bpm, y=dx)
        self.orb_x.setData(x=s_bpm, y=Dx0)
        self.orb_y_ref.setData(x=s_bpm, y=dy)
        self.orb_y.setData(x=s_bpm, y=Dy0)

        #self.plot_cor.update()
        self.orb_y.update()
        self.orb_x.update()

    def scale(self):
        corrs = self.get_dev_from_cb_state(self.corrs)
        self.online_calc = False
        for cor in corrs:

            kick_mrad = cor.ui.get_value()
            cor.ui.set_value(kick_mrad*self.ui.sb_kick_weight.value())
            #print( cor.id," set: ", cor.ui.get_init_value(), "-->", kick_mrad)
            #if -2.5 <= kick_mrad <=2.5:
            #    cor.mi.set_value(kick_mrad)
        self.online_calc = True

    def choose_plane(self):
        x_plane = self.ui.cb_x_cors.isChecked()
        y_plane = self.ui.cb_y_cors.isChecked()

        if y_plane and not x_plane:
            for cor in self.corrs:
                if cor.__class__ == Hcor:
                    cor.ui.uncheck()
                    cor.ui.set_hide(True)
                else:
                    cor.ui.check()
                    cor.ui.set_hide(False)


        elif x_plane and not y_plane:
            for cor in self.corrs:
                if cor.__class__ == Hcor:
                    cor.ui.check()
                    cor.ui.set_hide(False)
                else:
                    cor.ui.uncheck()
                    cor.ui.set_hide(True)


        else:
            for cor in self.corrs:
                cor.ui.check()
                cor.ui.set_hide(False)



    def reset_all(self):
        corrs = self.get_dev_from_cb_state(self.corrs)
        self.online_calc = False
        for cor in corrs:
            kick_mrad = cor.ui.get_init_value()
            cor.ui.set_value(kick_mrad)
        self.online_calc = True

    def apply_kicks(self):
        corrs = self.get_dev_from_cb_state(self.corrs)
        for cor in corrs:

            kick_mrad = cor.ui.get_value() * self.ui.sb_kick_weight.value()
            print( cor.id," set: ", cor.ui.get_init_value(), "-->", kick_mrad)
            #if -2.5 <= kick_mrad <=2.5:
            cor.mi.set_value(kick_mrad)

    def intro_misal(self):
        #lat = MagneticLattice(cell)

        for elem in self.parent.lat.sequence:
            if elem.id == 'CKX.23.I1':
                elem.angle = 0.1*0.001
            if elem.id == 'CKX.24.I1':
                elem.angle = -0.2 * 0.001
            #if elem.__class__ == Quadrupole:
            #    elem.dx = np.random.normal(0, 200e-6)
            #    elem.dx = np.random.normal(0, 200e-6)
        self.parent.lat.update_transfer_maps()

    def read_traj(self):
        self.orbit = Orbit(self.parent.lat)
        X0, Y0 = self.orbit.read_virtual_orbit(p_init=Particle(x=0.00, y=-0.00, px=0.000, E=self.parent.tws0.E))


    def read_orbit_sim(self):
        self.intro_misal()
        self.read_traj()
        self.online_calc = False
        for elem in self.corrs:
            elem.kick_mrad = elem.angle*1000.
            #angle = elem.kick_mrad*1e-3
            elem.angle = 0.
            elem.angle_read = elem.kick_mrad*1e-3
            elem.i_kick = elem.kick_mrad
            #print(elem.id, elem.angle)
            elem.ui.set_init_value(elem.kick_mrad)
            elem.ui.set_value(elem.kick_mrad)
        self.online_calc = True
        self.parent.lat.update_transfer_maps()
        for elem in self.bpms:
            try:
                x_mm, y_mm = elem.x*1000, elem.y*1000
                print(elem.id, x_mm, y_mm)
                elem.x = x_mm/1000.
                elem.y = y_mm/1000.
                elem.ui.set_value((x_mm, y_mm))
            except:
                print("deleted BPM", elem.id)
                self.bpms.remove(elem)

        self.update_plot()


    def read_orbit(self):
        self.online_calc = False
        for elem in self.corrs:
            elem.kick_mrad = elem.mi.get_value()
            #angle = elem.kick_mrad*1e-3
            #elem.angle = elem.kick_mrad*1e-3
            elem.angle_read = elem.kick_mrad*1e-3
            elem.i_kick = elem.kick_mrad
            #print(elem.id, elem.angle)
            elem.ui.set_init_value(elem.kick_mrad)
            elem.ui.set_value(elem.kick_mrad)
        self.online_calc = True
        self.parent.lat.update_transfer_maps()
        for elem in self.bpms:
            try:
                x_mm, y_mm = elem.mi.get_pos()
                elem.x = x_mm/1000.
                elem.y = y_mm/1000.
                elem.Dx = 0.
                elem.Dy = 0.
                elem.Dx_des = 0.
                elem.Dy_des = 0.
                elem.ui.set_value((x_mm, y_mm))
            except:
                print("deleted BPM", elem.id)
                self.bpms.remove(elem)

        self.update_plot()

    def set_golden_orbit(self):
        self.golden_orbit = {}
        for elem in self.bpms:
            elem.x_ref = elem.x
            elem.y_ref = elem.y
            self.golden_orbit[elem.id] = [elem.x, elem.y]

    def set_zero_golden_orbit(self):
        self.golden_orbit = {}
        for elem in self.bpms:
            elem.x_ref = 0.
            elem.y_ref = 0.
            self.golden_orbit[elem.id] = [elem.x, elem.y]

    def calc_orbit(self):
        #lat = MagneticLattice(cell)
        if self.online_calc == False:
            return

        # L = 0
        start = time.time()
        for elem in self.parent.lat.sequence:
            if elem.__class__ in [Hcor, Vcor]:
                #print(elem.id, elem.row)
                elem.kick_mrad = elem.ui.get_value()


                kick_mrad_i = elem.ui.get_init_value()
                warn = (np.abs(elem.kick_mrad) - np.abs(elem.ui.get_init_value())) > 0.5
                print(elem.id, warn)
                elem.ui.check_values(elem.kick_mrad, elem.lims, warn=warn)
                angle = (elem.kick_mrad - kick_mrad_i)/1000.
                elem.angle = angle # elem.kick_mrad/1000.
                if np.abs(np.abs(elem.kick_mrad) - np.abs(elem.i_kick))> 0.001:
                    self.r_items[elem.ui.row].setBrush(pg.mkBrush("r"))
                    self.ui.table_cor.item(elem.row, 1).setForeground(QtGui.QColor(255, 101, 101))  # red
                else:
                    self.ui.table_cor.item(elem.row, 1).setForeground(QtGui.QColor(255, 255, 255))  # white
                    self.r_items[elem.ui.row].setBrush(pg.mkBrush("g"))
                r = self.r_items[elem.ui.row]
                sizes = r.init_params
                #sizes = list(r.boundingRect().getRect())
                sizes[3] = elem.kick_mrad/self.cor_ampl
                r.setRect(sizes[0]-0.1, sizes[1], sizes[2]+0.1, sizes[3])
                elem.transfer_map = self.parent.lat.method.create_tm(elem)
        print("1 = ", start - time.time())
        start = time.time()
        #self.parent.lat.update_transfer_maps()
        print("2 = ", start - time.time())
        #print("test")
        # exit(0)
        #if self.p_init == None:


        self.update_plot()
        #self.update_plot(s, x, y, s_bpm=self.s_bpm, x_ref=self.x_bpm, y_ref=self.y_bpm)

    def create_Orbit_obj(self):
        """
        function creates the Orbit object with correctors and bpms which are active in the GUI

        :return: Orbit
        """
        for elem in self.corrs:
            print("angle = ", elem.angle)
        #print("response")
        self.orbit = NewOrbit(self.parent.lat, empty=True)
        #corrs = self.get_correctors()
        corrs = self.get_dev_from_cb_state(self.corrs)
        #print("correctors" , corrs)
        s_pos = np.min([cor.s for cor in corrs])
        bpms = np.array(self.bpms)
        #print([bpm.id for bpm in self.bpms])
        bpms_unch = bpms[np.array([bpm.s for bpm in self.bpms]) < s_pos]
        [bpm.ui.uncheck() for bpm in bpms_unch]
        #bpms = bpms[np.array([bpm.s for bpm in self.bpms])>=s_pos]
        bpms = self.get_dev_from_cb_state(bpms)
        #print([bpm.x for bpm in bpms])
        #self.orbit.bpms = copy.deepcopy(bpms)
        self.orbit.bpms = bpms
        self.hcors = []
        self.vcors = []
        for cor in corrs:
            #cor = copy.deepcopy(cor)
            if cor.__class__ == Hcor:
                self.hcors.append(cor)
            else:
                self.vcors.append(cor)

        self.orbit.hcors = self.hcors
        self.orbit.vcors = self.vcors
        #print("CREATE: ", [cor.id for cor in self.orbit.hcors])
        # add and update devices in ResponseMatrices
        self.orbit.response_matrix = self.response_matrix
        self.orbit.disp_response_matrix = self.disp_response_matrix
        self.orbit.update_devices_in_RMs()

        return self.orbit

    def dict2golden_orbit(self):
        for elem in self.orbit.bpms:
            if elem.id in self.golden_orbit.keys():
                x_gold = self.golden_orbit[elem.id][0]
                y_gold = self.golden_orbit[elem.id][1]
                elem.x_ref = x_gold
                elem.y_ref = y_gold
            else:
                elem.x_ref = 0.
                elem.y_ref = 0.

    def correct(self):
        #for bpm in self.bpms:
        #    bpm.x = bpm.x_mm/1000
        #    bpm.y = bpm.y_mm/1000

        self.orbit = self.create_Orbit_obj()
        #if self.ui.cb_golden_correct.isChecked():

        self.dict2golden_orbit()
            #print("golden", elem.id, x_gold, y_gold)
        #else:
        #    for elem in self.orbit.bpms:
        #        elem.x_ref = 0.
        #        elem.y_ref = 0.
        #corr_list = np.append(np.array([c.id for c in self.hcors]), np.array([c.id for c in self.vcors]))
        #r_matrix = self.resp_matrix.extract(cor_list=corr_list,
        #                                           bpm_list=[bpm.id for bpm in self.orbit.bpms])


        #self.orbit.resp = r_matrix.matrix
        p0 = Particle(E=self.parent.tws0.E)
        for cor in self.corrs:
            cor.angle = 0.
        alpha = self.ui.sb_alpha.value()
        self.orbit.correction(alpha=alpha, p_init=p0)
        self.online_calc = False
        for cor in self.corrs:
            #print("fin = ",  cor.angle, cor.id, cor)
            kick_mrad_old = cor.ui.get_init_value()
            delta_kick_mrad = cor.angle*1000
            new_kick_mrad = kick_mrad_old + delta_kick_mrad
            cor.kick_mrad =  new_kick_mrad # cor.angle*1000
            cor.ui.set_value(cor.kick_mrad)
            warn = (np.abs(new_kick_mrad) - np.abs(kick_mrad_old)) > 0.5

            #print(cor.id, cor.ui.get_value(), cor.kick_mrad, delta_kick_mrad, warn)
            cor.ui.check_values(cor.kick_mrad, cor.lims, warn)
        self.online_calc = True

        self.calc_orbit()

    #def get_correctors(self):
    #    pvs = self.getPvsFromCbState()
    #    corrs = self.get_devices(pvs)
    #    return corrs

    #def get_devices(self, pvs):
    #    d_pvs = [dev.id for dev in self.corrs]
    #    inxs = [d_pvs.index(pv) for pv in pvs]
    #    return [self.corrs[inx] for inx in inxs]

    def get_dev_from_cb_state(self, devs):

        """
        Gets list of all pvs that have checked boxes.

        Returns:
                List of PV strings
        """
        checked_devs = []
        for dev in devs:
            state = dev.ui.state()
            #print(dev.id, state)
            if state == 2:
                checked_devs.append(dev)
        return checked_devs

    def response_matrix(self):
        self.orbit = self.create_Orbit_obj()
        #self.rmatrix = self.orbit.linac_response_matrix_r(tw_init=self.parent.tws0)

        method = LinacRmatrixRM(lattice=self.orbit.lat, hcors=self.orbit.hcors,
                                vcors=self.orbit.vcors, bpms=self.orbit.bpms)
        self.response_matrix = ResponseMatrix(method=method) #self.orbit.linac_response_matrix_r(tw_init=self.parent.tws0)
        self.response_matrix.calculate(tw_init=self.parent.tws0)
        self.response_matrix.dump("tld_r.json")

        print("response_matrix: hcor = ", len(self.response_matrix.cor_names), len(self.response_matrix.bpm_names))

        method = LinacDisperseSimRM(lattice=self.orbit.lat, hcors=self.orbit.hcors,
                                vcors=self.orbit.vcors, bpms=self.orbit.bpms)

        self.disp_response_matrix = ResponseMatrix(method=method)  # self.orbit.linac_response_matrix_r(tw_init=self.parent.tws0)
        self.disp_response_matrix.calculate(tw_init=self.parent.tws0)
        self.disp_response_matrix.dump("disp_tld.json")
        print("disp_resp_matrix: hcor = ", len(self.disp_response_matrix.cor_names),
         len(self.disp_response_matrix.bpm_names))
        #self.orbit.resp = self.resp_matrix.matrix
        #return self.resp_matrix

    def calc_misalignment_rm(self):
        for elem in self.corrs:
            print("angle = ", elem.angle)
        #self.orbit = Orbit(self.parent.lat, empty=True)

        self.misal_resp_mat = self.orbit.misalignment_rm(p_init=Particle(E=self.parent.tws0.E),
                                   elem_types=[Quadrupole, Bend, SBend,RBend], remove_elem=[])

        p = self.orbit.elem_correction(self.misal_resp_mat, elem_types=[Quadrupole, Bend, SBend, RBend], remove_elems=[])
        p.E=self.parent.tws0.E
        self.p_init = p
        self.calc_orbit()

    def create_orbit(self):
        self.orbit = Orbit(self.parent.lat)

        resp_m = self.orbit.misalignment_rm(p_init=Particle(E=self.parent.tws0.E),
                                   elem_types=[Quadrupole, Bend, SBend,RBend], remove_elem=[])
        self.orbit.elem_correction(resp_m, elem_types=[Quadrupole, Bend, SBend,RBend], remove_elems=[])
        self.calc_orbit()

    def func(self):
        pass


    def load_correctors(self):

        self.corrs = self.load_devices(types=[Hcor, Vcor])

        self.parent.add_devs2table(self.corrs, w_table=self.ui.table_cor, calc_obj=self.calc_orbit,
                                   spin_params=[-100, 100, 0.1], check_box=True)
        self.cor_ampl = np.max(np.append(1, np.abs(np.array([q.kick_mrad for q in self.corrs]))))

    def load_bpms(self, lat):
        devices = []
        L = 0
        for i, elem in enumerate(lat.sequence):
            L += elem.l
            if elem.__class__ in [Monitor]:
                elem.s = L - elem.l/2.
                devices.append(elem)

                mi_dev = BPM(eid=elem.id)
                mi_dev.mi = self.parent.mi
                elem.mi = mi_dev
                elem.lat_inx = i
                elem.x = 0
                elem.y = 0
                elem.weight = 1

        return devices

    def add_bpms2table(self, devs, w_table, check_box=False):
        """ Initialize the UI table object """
        #spin_boxes = [QtGui.QDoubleSpinBox()]*
        self.spin_boxes = []
        w_table.setRowCount(0)
        for row in range(len(devs)):
            #eng = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)
            w_table.setRowCount(row + 1)
            pv = devs[row].id
            # put PV in the table
            w_table.setItem(row, 0, QtGui.QTableWidgetItem(str(pv)))
            # put start val in
            w_table.setItem(row, 1, QtGui.QTableWidgetItem(str(devs[row].x)))
            w_table.setItem(row, 2, QtGui.QTableWidgetItem(str(devs[row].y)))

            w_table.resizeColumnsToContents()


            if check_box:
                checkBoxItem = QtGui.QTableWidgetItem()
                # checkBoxItem.setBackgroundColor(QtGui.QColor(100,100,150))
                checkBoxItem.setCheckState(QtCore.Qt.Checked)
                flags = checkBoxItem.flags()
                checkBoxItem.setFlags(flags)
                w_table.setItem(row, 3, checkBoxItem)
                #checkBoxItem.itemChanged.connect(self.calc_orbit)

            devs[row].row = row

            ui = BPMUI()
            ui.tableWidget = w_table
            ui.row = row
            ui.col = 2
            devs[row].ui = ui

    def load_orbit_devs(self):
        self.bpms = self.load_bpms(lat=self.parent.lat)
        self.add_bpms2table(self.bpms, w_table=self.ui.table_bpm, check_box=True)
        self.load_correctors()

        self.r_items = self.parent.plot_lat(plot_wdg=self.plot_cor, types=[Hcor, Vcor])

    def load_devices(self, types):
        devices = []
        mi_devs = {}
        #cell_i1_copy = copy.deepcopy(cell_i1_copy)
        #lat_tmp = MagneticLattice(cell_i1_copy)
        print("load_devices", len(self.parent.lat.sequence))
        L = 0
        for i, elem in enumerate(self.parent.lat.sequence):
            L += elem.l
            if elem.__class__ in types:
                elem.s = L - elem.l / 2.
                elem.kick_mrad = elem.angle* 1000.
                elem.i_kick = elem.kick_mrad

                elem.lat_inx = i
                #elem.mi = Device(eid="XFEL.MAGNETS/MAGNET.ML/" + elem.id + "/KICK_MRAD.SP")
                if "ps_id" in elem.__dict__:
                    if elem.ps_id not in mi_devs.keys():
                        mi_dev = Corrector(eid=elem.id) # Device(eid="XFEL.MAGNETS/MAGNET.ML/" + elem.id + "/KICK_MRAD.SP")
                        mi_dev.mi = self.parent.mi
                        elem.mi = mi_dev
                        mi_devs[elem.ps_id] = mi_dev
                    else:
                        elem.mi = mi_devs[elem.ps_id]
                else:
                    mi_dev = Corrector(eid=elem.id) # Device(eid="XFEL.MAGNETS/MAGNET.ML/" + elem.id + "/KICK_MRAD.SP")
                    mi_dev.mi = self.parent.mi
                    elem.mi = mi_dev

                elem.lims = elem.mi.get_limits()
                #print("load ", elem.id)
                if elem.__class__ == Hcor:
                    self.hcors.append(elem)
                elif elem.__class__ == Vcor:
                    self.vcors.append(elem)
                else:
                    print("wrong type")
                devices.append(elem)
        #print(devices)
        #print(self.hcors)
        #print(self.vcors)
        return devices


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
        self.ui.w_orbit.setLayout(layout)
        layout.addWidget(win, 0, 0)

        self.plot_y.setAutoVisible(y=True)

        self.plot_y.addLegend()


        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.orb_y = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Y', antialias=True)
        self.plot_y.addItem(self.orb_y)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=3)
        self.orb_y_ref = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Y ref', antialias=True)
        self.plot_y.addItem(self.orb_y_ref)

        color = QtGui.QColor(255, 255, 0)
        pen = pg.mkPen(color, width=3)
        self.orb_y_golden = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Y golden', antialias=True)
        self.plot_y.addItem(self.orb_y_golden)

        color = QtGui.QColor(0, 255, 0)
        pen = pg.mkPen(color, width=2)
        self.orb_y_live = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='Y live', antialias=True)
        self.plot_y.addItem(self.orb_y_live)


        self.plot_cor = win.addPlot(row=2, col=0)
        win.ci.layout.setRowMaximumHeight(2, 150)

        self.plot_cor.setXLink(self.plot_y)
        self.plot_cor.showGrid(1, 1, 1)

        self.plot_cor.addItem(pg.InfiniteLine(pos =62.09,  angle=90, movable=False), ignoreBounds=True)
        lh_t = pg.TextItem("I1", anchor=(0, 0))
        lh_t.setPos(62.09, 0)
        self.plot_cor.addItem(lh_t, ignoreBounds=True)

        i1_pos = 62.09
        dl_pos = 23.2 + 72
        bc0_pos = 79 + 23.2
        l1_pos = 150 + 23.2
        bc1_pos = 180 + 23.2
        l2_pos = 360 + 23.2
        bc2_pos = 392 + 23.2
        l3_pos = 1435 + 23.2
        cl_pos = 1830 + 23.2
        self.plot_cor.addItem(pg.InfiniteLine(pos =i1_pos,  angle=90, movable=False), ignoreBounds=True)
        lh_t = pg.TextItem("I1", anchor=(0, 0))
        lh_t.setPos(i1_pos, 0)
        self.plot_cor.addItem(lh_t, ignoreBounds=True)

        #self.plot_cor.addItem(pg.InfiniteLine(pos =dl_pos,  angle=90, movable=False), ignoreBounds=True)
        #dl_t = pg.TextItem("DL", anchor=(0, 0))
        #dl_t.setPos(dl_pos, 0)
        #self.plot_cor.addItem(dl_t, ignoreBounds=True)

        self.plot_cor.addItem(pg.InfiniteLine(pos =bc0_pos,  angle=90, movable=False), ignoreBounds=True)
        bc0_t = pg.TextItem("BC0", anchor=(0, 0))
        bc0_t.setPos(bc0_pos, 0)
        self.plot_cor.addItem(bc0_t, ignoreBounds=True)

        self.plot_cor.addItem(pg.InfiniteLine(pos =l1_pos,  angle=90, movable=False), ignoreBounds=True)
        l1_t = pg.TextItem("L1", anchor=(0, 0))
        l1_t.setPos(l1_pos, 0)
        self.plot_cor.addItem(l1_t, ignoreBounds=True)

        self.plot_cor.addItem(pg.InfiniteLine(pos =bc1_pos,  angle=90, movable=False), ignoreBounds=True)
        bc1_t = pg.TextItem("BC1", anchor=(0, 0))
        bc1_t.setPos(bc1_pos, 0)
        self.plot_cor.addItem(bc1_t, ignoreBounds=True)

        self.plot_cor.addItem(pg.InfiniteLine(pos =l2_pos,  angle=90, movable=False), ignoreBounds=True)
        l2_t = pg.TextItem("L2", anchor=(0, 0))
        l2_t.setPos(l2_pos, 0)
        self.plot_cor.addItem(l2_t, ignoreBounds=True)

        self.plot_cor.addItem(pg.InfiniteLine(pos =bc2_pos,  angle=90, movable=False), ignoreBounds=True)
        bc2_t = pg.TextItem("BC2", anchor=(0, 0))
        bc2_t.setPos(bc2_pos, 0)
        self.plot_cor.addItem(bc2_t, ignoreBounds=True)

        self.plot_cor.addItem(pg.InfiniteLine(pos =l3_pos,  angle=90, movable=False), ignoreBounds=True)
        l3_t = pg.TextItem("L3", anchor=(0, 0))
        l3_t.setPos(l3_pos, 0)
        self.plot_cor.addItem(l3_t, ignoreBounds=True)

        self.plot_cor.addItem(pg.InfiniteLine(pos =cl_pos,  angle=90, movable=False), ignoreBounds=True)
        cl_t = pg.TextItem("CL", anchor=(0, 0))
        cl_t.setPos(cl_pos, 0)
        self.plot_cor.addItem(cl_t, ignoreBounds=True)

        self.plot_x.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.orb_x = pg.PlotCurveItem(x=[], y=[], pen=pen,  name='X', antialias=True)

        self.plot_x.addItem(self.orb_x)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=3, symbolPen='o')
        self.orb_x_ref = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='X ref', antialias=True)
        self.plot_x.addItem(self.orb_x_ref)

        color = QtGui.QColor(0, 255, 0)
        pen = pg.mkPen(color, width=2)
        self.orb_x_live = pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='X live', antialias=True)
        self.plot_x.addItem(self.orb_x_live)

        color = QtGui.QColor(255, 255, 0)
        pen = pg.mkPen(color, width=2)
        self.orb_x_golden= pg.PlotDataItem(x=[], y=[], pen=pen, symbol='o', name='X golden', antialias=True)
        self.plot_x.addItem(self.orb_x_golden)


        self.plot_cor.sigRangeChanged.connect(self.zoom_signal)
        self.plot_cor.setYRange(-3, 3)
        self.plot_x.setYRange(-2, 2)
        self.plot_y.setYRange(-2, 2)

    def zoom_signal(self):
        if len(self.corrs) == 0:
            return


        s_up = self.plot_y.viewRange()[0][0]
        s_down = self.plot_y.viewRange()[0][1]

        s_pos = np.array([q.s for q in self.corrs]) + self.parent.lat_zi
        s_up = s_up if s_up <= s_pos[-1] else s_pos[-1]
        s_down = s_down if s_down >= s_pos[0] else s_pos[0]

        s_bpm_pos = np.array([q.s for q in self.bpms]) + self.parent.lat_zi
        s_bpm_up = s_up if s_up <= s_bpm_pos[-1] else s_bpm_pos[-1]
        s_bpm_down = s_down if s_down >= s_bpm_pos[0] else s_bpm_pos[0]

        indexes = np.arange(np.argwhere(s_pos >= s_up)[0][0], np.argwhere(s_pos <= s_down)[-1][0] + 1)
        mask = np.ones(len(self.corrs), np.bool)
        mask[indexes] = 0
        self.corrs = np.array(self.corrs)
        [q.ui.set_hide(hide=False) for q in self.corrs[indexes]]
        [q.ui.set_hide(hide=True) for q in self.corrs[mask]]

        [q.ui.check() for q in self.corrs[indexes]]
        [q.ui.uncheck() for q in self.corrs[mask]]

        indexes_bpm = np.arange(np.argwhere(s_bpm_pos >= s_bpm_up)[0][0], np.argwhere(s_bpm_pos <= s_down)[-1][0] + 1)
        mask_bpm = np.ones(len(self.bpms), np.bool)
        mask_bpm[indexes_bpm] = 0
        self.bpms = np.array(self.bpms)
        [q.ui.set_hide(hide=False) for q in self.bpms[indexes_bpm]]
        [q.ui.set_hide(hide=True) for q in self.bpms[mask_bpm]]
        [q.ui.check() for q in self.bpms[indexes_bpm]]
        [q.ui.uncheck() for q in self.bpms[mask_bpm]]
        #row = self.corrs[indx_up].ui.row
        #self.ui.tableWidget.scrollTo(row)
        #item = self.ui.tableWidget.item(row, 2)
        #self.ui.tableWidget.scrollToItem(item, QtGui.QAbstractItemView.PositionAtBottom)
        #self.ui.tableWidget.selectRow(row)

    def start_stop_live_orbit(self):
        if self.ui.cb_online_orbit.isChecked():
            self.parent.timer_live.start(1000)
        else:
            self.parent.timer_live.stop()
            self.orb_x_live.setData(x=[], y=[])
            self.orb_y_live.setData(x=[], y=[])
            self.orb_y.update()
            self.orb_x.update()

    def start_stop_golden_orbit(self):
        if self.ui.cb_golden_orbit.isChecked():
            s_bpm = np.array([])
            x_bpm = np.array([])
            y_bpm = np.array([])
            bpms = self.get_dev_from_cb_state(self.bpms)
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

            s_bpm += self.parent.lat_zi

            print("Golden")
            self.orb_x_golden.setData(x=s_bpm, y=x_bpm)
            self.orb_y_golden.setData(x=s_bpm, y=y_bpm)
            self.orb_y.update()
            self.orb_x.update()
        else:
            self.orb_x_golden.setData(x=[], y=[])
            self.orb_y_golden.setData(x=[], y=[])
            self.orb_y.update()
            self.orb_x.update()


    def live_orbit(self):

        s_bpm = np.array([])
        x_bpm = np.array([])
        y_bpm = np.array([])
        bpms = self.get_dev_from_cb_state(self.bpms)
        for elem in bpms:
            try:
                x_mm, y_mm = elem.mi.get_pos()
                s_bpm = np.append(s_bpm, elem.s)
                x_bpm = np.append(x_bpm, x_mm - elem.x_ref*1000)
                y_bpm = np.append(y_bpm, y_mm - elem.y_ref*1000)
            except:
                print("could not read BPM", elem.id)

        s_bpm += self.parent.lat_zi

        #print("LIVE")
        self.orb_x_live.setData(x=s_bpm, y=x_bpm)
        self.orb_y_live.setData(x=s_bpm, y=y_bpm)
        self.orb_y.update()
        self.orb_x.update()

    def update_plot(self):

        start = time.time()
        p_list = lattice_track(self.parent.lat, Particle(E=self.parent.tws0.E))
        print("3 = ", start - time.time())
        #else:
        #    p_list = lattice_track(self.parent.lat, copy.deepcopy(self.p_init))
        #tws = twiss(self.lat, self.tws0)
        #print(tws[-1], self.tws0)
        #plot_opt_func(lat, tws, top_plot=["Dx", "Dy"])
        #plt.show()
        x = np.array([p.x for p in p_list])*1000
        y = np.array([p.y for p in p_list])*1000
        s = np.array([p.s for p in p_list]) + self.parent.lat_zi

        bpms = self.get_dev_from_cb_state(self.bpms)

        s_bpm = np.array([bpm.s for bpm in bpms]) + self.parent.lat_zi
        x_bpm = np.array([bpm.x - bpm.x_ref for bpm in bpms])*1000
        y_bpm = np.array([bpm.y - bpm.y_ref for bpm in bpms])*1000

        # Line
        self.orb_x_ref.setData(x=s_bpm, y=x_bpm)
        self.orb_x.setData(x=s, y=x)
        self.orb_y_ref.setData(x=s_bpm, y=y_bpm)
        self.orb_y.setData(x=s, y=y)

        self.plot_cor.update()
        self.orb_y.update()
        self.orb_x.update()

    def uncheckBoxes(self):
        """ Method to unchecked all active boxes """
        for cor in self.corrs:
            cor.ui.uncheck()
            # item = self.ui.tableWidget.cellWidget(row, 5)
            #item.setCheckState(False)

    def getRows(self, state, widget):
        """
        Method to set the UI checkbox state from slected rows.

        Loops though the rows and gets the selected state from the 'Active" column.
        If highlighted, check box is set the the 'state' input arg.

        Args:
                state (bool): Bool of whether the boxes should be checked or unchecked.
        """
        rows=[]
        for idx in widget.selectedIndexes():
            rows.append(idx.row())
            item = widget.item(idx.row(), 3)
            if item.flags() == QtCore.Qt.NoItemFlags:
                print("item disabled")
                continue
            item.setCheckState(state)


