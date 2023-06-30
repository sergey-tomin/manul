from ocelot import *
from ocelot.gui import *
import i1, l1, t3

lat = MagneticLattice(i1.cell)
tws = twiss(lat, i1.tws0)
plot_opt_func(lat, tws)
plt.show()

lat = MagneticLattice(l1.cell)
tws = twiss(lat, l1.tws0)
plot_opt_func(lat, tws)
plt.show()

lat = MagneticLattice(t3.cell)
tws = twiss(lat, t3.tws0)
plot_opt_func(lat, tws)
plt.show()