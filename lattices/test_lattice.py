from ocelot import *
from ocelot.gui.accelerator import *
#from ocelot.test.xfel_lat.lattices.I1B2 import *
#from ocelot.test.xfel_lat.lattices.I1B2_screen2 import *
from ocelot.test.xfel_lat.xfel_i1_nina import *
from ocelot.test.xfel_lat.xfel_l1_nina import *
from ocelot.test.xfel_lat.xfel_l2_nina import *
from ocelot.test.xfel_lat.xfel_l3_nina import *
from ocelot.adaptors import *
import time
from matplotlib.colors import LogNorm
from matplotlib.ticker import NullFormatter
undu_49_i1.Kx = 0


tws0 = Twiss()
tws0.E = 0.005

tws0.beta_x = 25.543
tws0.alpha_x = -0.3773
tws0.beta_y = 25.543
tws0.alpha_y = -0.3773

tws0.beta_x  = 55.7887190242
tws0.beta_y  = 55.7887190242
tws0.alpha_x = 18.185436973
tws0.alpha_y = 18.185436973

cell = cell_i1 + cell_l1 + cell_l2 + cell

lat = MagneticLattice(cell)
#lat = MagneticLattice(cell, start=start_lin)


tws = twiss(lat, tws0)

plot_opt_func(lat, tws, top_plot=["Dx", "Dy"])
plt.show()