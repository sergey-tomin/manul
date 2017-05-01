from lattices.xfel_i1_mad import *
from lattices.xfel_l1_mad import *
from lattices.xfel_l2_mad import *
from lattices.xfel_l3_mad import *
from lattices.xfel_tld_892 import *
from ocelot import *
from ocelot.cpbd.track import *
from ocelot.gui.accelerator import *

tws0 = Twiss()
tws0.E = 0.005


tws0.beta_x  = 55.7887190242
tws0.beta_y  = 55.7887190242
tws0.alpha_x = 18.185436973
tws0.alpha_y = 18.185436973

cell = cell_i1 + cell_l1 + cell_l2 #+ cell_l3

#lat = MagneticLattice(cell, start=d_12, stop = d_23)
#for elem in lat.sequence:
#    print(elem.id)
#R = lattice_transfer_map(lat, energy = 0.005)
#print("test", R)
lat = MagneticLattice(cell)
tws2 = twiss(lat, tws0)
plot_opt_func(lat, tws2, top_plot=["Dx", "Dy"], font_size=13)
plt.show()


def lattice_track_fast(lat, p):
    plist = [copy(p)]

    for elem in lat.R_seq:
        elem.transfer_map.apply([p])
        #print(p)
        if not (elem.__class__ in [Bend, RBend, SBend] and elem.l != 0.): #, "hcor", "vcor"
            if elem.__class__ == Edge:
                #print elem.pos
                if elem.pos == 1:
                    continue
        plist.append(copy(p))
    return plist


lat_sr = shrinker(lat, remaining_types=[Quadrupole, Hcor, Vcor, Monitor, Bend, SBend, RBend], init_energy=0.005)
L = 0.
for elem in lat_sr.sequence:
    L += elem.l
    print(L, elem.id, elem.__class__.__name__, elem.l)

p_list = lattice_track(lat, Particle(x = 0.001, E=0.005))
p_list_s = lattice_track(lat_sr, Particle(x = 0.001, E=0.005))
x = np.array([p.x for p in p_list]) * 1000
y = np.array([p.y for p in p_list]) * 1000
s = np.array([p.s for p in p_list])
x_s = np.array([p.x for p in p_list_s]) * 1000
y_s = np.array([p.y for p in p_list_s]) * 1000
s_s = np.array([p.s for p in p_list_s])

plt.plot(s, x)
plt.plot(s_s, x_s)
plt.show()

from ocelot.cpbd.orbit_correction import *

orbit = Orbit(lat)
rmatrix = orbit.linac_response_matrix_r(tws0)
#print(rmatrix.matrix[4])
orbit_s = Orbit(lat_sr)
rmatrix_s = orbit_s.linac_response_matrix_r(tws0)
print(rmatrix_s.matrix)

#print(len(lat.fast_seq))
#L = 0
#for elem in lat.fast_seq:
#    print(elem.l, L, elem.transfer_map._r)
#    L += elem.l
#    #print(elem.transfer_map.R(0))
#lat = MagneticLattice(cell, start=start_lin)
print(len(lat.sequence))
print(tws0)
tws2 = twiss(lat, tws0)
tws = twiss(lat_sr, tws0)



beta_x = np.array([p.mux for p in tws])
beta_y = np.array([p.muy for p in tws])
s = np.array([p.s for p in tws])
#print(s[:3])
#print(beta_y[:3])

beta_x2 = np.array([p.mux for p in tws2])
beta_y2 = np.array([p.muy for p in tws2])
s2 = np.array([p.s for p in tws2])

plt.plot(s, beta_x, "r.-")
plt.plot(s, beta_y, "b.-")
plt.plot(s2, beta_x2)
plt.plot(s2, beta_y2)
plt.show()




