

class Simulator:
    def __init__(self):
        pass
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