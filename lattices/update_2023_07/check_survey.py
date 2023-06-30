from ocelot import *
from ocelot.gui import *
import copy
import i1, l1

lat = MagneticLattice(i1.cell + l1.cell)

x, y, z, _, _ = lat.survey()

plt.plot(z, y)
plt.plot(z, x)
plt.show()
