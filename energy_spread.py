"""
S Tomin
"""
import sys, os
#path = sys.path[0]
#indx = path.find("ocelot")
#sys.path.append(path[:indx])
path = os.path.realpath(__file__)
indx = path.find("manul")
print("PATH", os.path.realpath(__file__), path[:indx])
sys.path.append(path[:indx])

from ocelot import *
from ocelot.gui.accelerator import *
#from ocelot.test.xfel_lat.lattices.I1B2 import *
#from ocelot.test.xfel_lat.lattices.I1B2_screen2 import *
from lattices.xfel_i1_mad import *
from lattices.xfel_l1_mad import *
from lattices.xfel_l2_mad import *
from lattices.xfel_l3_mad import *

#from ocelot.adaptors import *
#import time
#from matplotlib.colors import LogNorm
#from matplotlib.ticker import NullFormatter
tws0 = Twiss()
tws0.E = 0.005

tws0.beta_x  = 55.7887190242
tws0.beta_y  = 55.7887190242
tws0.alpha_x = 18.185436973
tws0.alpha_y = 18.185436973

cell = cell_i1 + cell_l1 + cell_l2 + cell_l3

lat = MagneticLattice(cell)#,  start=bpmf_393_b2, stop=bpmf_414_b2)
print(lat.totalLen+3.2)

#R = lattice_transfer_map(lat, energy=2.4)
#print(R)
#tws = twiss(lat, tws0)

#plot_opt_func(lat, tws, top_plot=["Dx", "Dy"])
#plt.show()



from decimal import Decimal
import time
import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
from ocelot.optimizer.mint.xfel_interface import XFELMachineInterface, TestMachineInterface

Rab11 = 9.15990180e-01
Rab12 = 1.36083204e+00
Rab16 = -3.00933180e-02
Rac11 = 7.84400129e-01
Rac12 = 5.58849103e+00
Rterms_LH = [Rab11, Rab12, Rab16, Rac11, Rac12]
Rterms_bc1 = [1., 1.09263106e+01, 4.87107400e-01, 1., 2.18731202e+01]
Rterms_bc2 = [1., 1.09506535e+01, 4.11011033e-01, 1, 2.17861671e+01]
def delta_energy(x_a, x_b, x_c, Rterms):
    Rab11 = Rterms[0]
    Rab12 = Rterms[1]
    Rab16 = Rterms[2]
    Rac11 = Rterms[3]
    Rac12 = Rterms[4]
    x1_a = (x_c - Rac11*x_a)/Rac12
    delta_e = (x_b - Rab11*x_a - Rab12*x1_a)/Rab16
    return delta_e



mi = XFELMachineInterface()



def get_xy(bpm):
    x = mi.get_value("XFEL.DIAG/BPM/" + bpm + "/X.SA1")*0.001
    y = mi.get_value("XFEL.DIAG/BPM/" + bpm + "/Y.SA1")*0.001
    return x, y


win = pg.GraphicsWindow()
win.resize(800,350)
win.setWindowTitle('pyqtgraph example: Histogram')
pw = win.addPlot()
pw_bc1 = win.addPlot()
pw_bc2 = win.addPlot()


d = np.zeros(1000)
text = pg.TextItem(text="test", border='w', fill = (255,0,255,150))
pw.addItem(text)
def update():
    global d, text
    xa, ya = get_xy("BPMF.47.I1")
    xb, yb = get_xy("BPMF.48.I1")
    xc, yc = get_xy("BPMF.52.I1")
    #print(xa)
    delta = delta_energy(xa, xb, xc, Rterms_LH)
    d1 = np.delete(d, 0)
    d = np.append(d1, delta)

    y, x = np.histogram(d, bins=60)
    pw.plot(x, y, clear=True, stepMode=True, fillLevel=0, brush=(0,255,255,200))
    sig = np.std(d)
    text.setText("sigma_lh="+'%.2E' % Decimal(str(sig)))
    text.setPos(np.mean(d),y.max())
    pw.addItem(text)


d_2 = np.zeros(1000)
text_bc1 = pg.TextItem(text="test", border='w', fill = (255,0,255,150))
pw_bc1.addItem(text_bc1)
def update_bc1():
    global d_2, text_bc1
    xa, ya = get_xy("BPMF.181.B1")
    xb, yb = get_xy("BPMS.192.B1")
    xc, yc = get_xy("BPMF.203.B1")

    delta = delta_energy(ya, yb, yc, Rterms_bc1)
    d1 = np.delete(d_2, 0)
    d_2 = np.append(d1, delta)

    y, x = np.histogram(d_2, bins=60)
    pw_bc1.plot(x, y, clear=True, stepMode=True, fillLevel=0, brush=(0,255,255,200))
    sig = np.std(d_2)
    text_bc1.setText("sigma_bc1="+'%.2E' % Decimal(str(sig)))
    text_bc1.setPos(np.mean(d_2), y.max())
    pw_bc1.addItem(text_bc1)


d_3 = np.zeros(1000)
text_bc2 = pg.TextItem(text="test", border='w', fill = (255,0,255,150))
pw_bc2.addItem(text_bc2)
def update_bc2():
    global d_3, text_bc2
    xa, ya = get_xy("BPMF.393.B2")
    xb, yb = get_xy("BPMS.404.B2")
    xc, yc = get_xy("BPMF.414.B2")
    #print(yb)
    delta = delta_energy(ya, yb, yc, Rterms_bc2)
    d1 = np.delete(d_3, 0)
    d_3 = np.append(d1, delta)

    y, x = np.histogram(d_3, bins=60)
    pw_bc2.plot(x, y, clear=True, stepMode=True, fillLevel=0, brush=(0,255,255,200))
    sig = np.std(d_3)
    text_bc2.setText("sigma_bc2="+'%.2E' % Decimal(str(sig)))
    text_bc2.setPos(np.mean(d_3), y.max())
    pw_bc2.addItem(text_bc2)


timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(100)

timer_bc1 = pg.QtCore.QTimer()
timer_bc1.timeout.connect(update_bc1)
timer_bc1.start(100)

timer_bc2 = pg.QtCore.QTimer()
timer_bc2.timeout.connect(update_bc2)
timer_bc2.start(100)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

