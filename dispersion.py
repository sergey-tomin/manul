import numpy as np

class Dispertion:
    def __init__(self):
        pass

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