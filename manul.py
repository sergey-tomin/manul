"""

"""
#QT imports
from PyQt4.QtGui import QApplication, QFrame, QPixmap, QMessageBox
from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
#normal imports
import numpy as np
#import epics
import sys
import os


path = os.path.realpath(__file__)
indx = path.find("manul")
print("PATH", os.path.realpath(__file__), path[:indx])
sys.path.append(path[:indx])

import time
import pyqtgraph as pg
from gui_main import *
from lattices.xfel_i1_890 import *
from lattices.xfel_l1_890 import *
from lattices.xfel_l2_890 import *
from lattices.xfel_l3_890 import *
from ocelot import *
from ocelot.gui.accelerator import *
from ocelot.optimizer.mint.xfel_interface import *

from ocelot.optimizer.mint.opt_objects import Device
from ocelot.optimizer.mint.xfel_interface import *

#GUI layout file



#import taperThread

class DeviceUI:
    def __init__(self, ui=None):
        self.tableWidget = None
        self.row = 0
        self.col = 0

    def get_value(self):
        return self.tableWidget.cellWidget(self.row, self.col).value()

    def set_value(self, val):
        self.tableWidget.cellWidget(self.row, self.col).setValue(val)

    def set_init_value(self, val):
        self.tableWidget.item(self.row, 1).setText(str(val))


class MDevice(Device):
    def __init__(self, eid=None):
        super(MDevice, self).__init__(eid=eid)





class ManulInterfaceWindow(QFrame):
    """ Main class for the GUI application """
    def __init__(self):
        """
        Initialize the GUI and QT UI aspects of the application.
        Initialize the scan parameters.
        Connect start and logbook buttons on the scan panel.
        Initialize the plotting.
        Make the timer object that updates GUI on clock cycle during a scan.
        """
        # PATHS
        path = os.path.realpath(__file__)
        indx = path.find("ocelot" + os.sep + "optimizer")
        self.path2ocelot = path[:indx]
        self.optimizer_path = self.path2ocelot + "ocelot" + os.sep + "optimizer" + os.sep
        self.config_dir = self.path2ocelot + "config_optim" +os.sep
        self.set_file = self.config_dir + "default.json" # ./parameters/default.json"
        self.obj_func_path = self.optimizer_path + "mint" + os.sep + "obj_function.py"
        self.obj_save_path = self.config_dir +  "obj_funcs" + os.sep
        # initialize
        QFrame.__init__(self)

        self.logbook = "xfellog"
        self.dev_mode = True

        self.ui = MainWindow(self)
        #self.mi = XFELMachineInterface()
        self.mi = TestMachineInterface()
        #QFrame.__init__(self)
        #self.ui = Ui_Form()
        #self.ui.setupUi(self)


        #load in the dark theme style sheet
        self.loadStyleSheet()

        #timer for plots, starts when scan starts
        self.multiPvTimer = QtCore.QTimer()
        #self.multiPvTimer.timeout.connect(self.getPlotData)
        self.pvs = ["sdf","asdf"]
        #self.initTable()
        self.add_plot()

        self.lat = self.return_lat()
        self.tws0 = self.return_tws()
        self.load_lattice()
        #taperThread.Taper(initPVs = True, mi=self.mi) #update taper PVs with initial taper parameters


        self.ui.pb_write.clicked.connect(self.calc)
        self.ui.pb_read.clicked.connect(self.read_quads)
        self.ui.pb_reset.clicked.connect(self.reset_quads)


    def update_table(self):
        for quad in self.quads:
            quad.ui.set_init_value(quad.kick_mrad)
            quad.ui.set_value(quad.kick_mrad)


    def reset_quads(self):
        for quad in self.quads:
            print(quad.i_kick)
            quad.ui.set_value(quad.i_kick)
        #self.calc()

    def read_quads(self):
        for elem in self.quads:
            elem.kick_mrad = elem.mi.get_value()
            k1 = elem.kick_mrad/elem.l*1e-3
            elem.k1 = k1
            elem.i_kick = elem.kick_mrad
            print(elem.i_kick)
            elem.ui.set_init_value(elem.kick_mrad)
            elem.ui.set_value(elem.kick_mrad)
        self.lat.update_transfer_maps()
        tws0 = self.read_twiss()
        lat_tmp = MagneticLattice(self.lat.sequence, stop=otrc_55_i1)
        lat_tmp = MagneticLattice(lat_tmp.sequence[::-1])
        tws0.alpha_x = -tws0.alpha_x
        tws0.alpha_y = -tws0.alpha_y
        tws = twiss(lat_tmp, tws0)
        print(tws[-1])
        self.tws0 = tws[-1]
        self.tws0.alpha_x = -tws0.alpha_x
        self.tws0.alpha_y = -tws0.alpha_y
        self.tws0.s = 0
        tws = twiss(self.lat, self.tws0)
        beta_x = [tw.beta_x for tw in tws]
        beta_y = [tw.beta_y for tw in tws]
        dx = [tw.Dx for tw in tws]
        dy = [tw.Dy for tw in tws]
        s = [tw.s for tw in tws]
        self.update_plot(s, beta_x, beta_y, dx, dy)
        #self.update_table()

    def read_twiss(self):
        ch_beta_x = "XFEL.UTIL/BEAM_PARAMETER/I1/PROJECTED_X.BETA.SA1"
        ch_alpha_x = "XFEL.UTIL/BEAM_PARAMETER/I1/PROJECTED_X.ALPHA.SA1"
        ch_beta_y = "XFEL.UTIL/BEAM_PARAMETER/I1/PROJECTED_Y.BETA.SA1"
        ch_alpha_y = "XFEL.UTIL/BEAM_PARAMETER/I1/PROJECTED_Y.ALPHA.SA1"
        ch_energy = "XFEL.UTIL/BEAM_PARAMETER/I1/PROJECTED_X.ENERGY.SA1"
        tws = Twiss()
        tws.beta_x = self.mi.get_value(ch_beta_x)
        tws.beta_y = self.mi.get_value(ch_beta_y)
        tws.alpha_x = self.mi.get_value(ch_alpha_x)
        tws.alpha_y = self.mi.get_value(ch_alpha_y)
        tws.E = self.mi.get_value(ch_energy)
        return tws


    def return_lat(self):
        self.lat = MagneticLattice(cell_i1)
        return self.lat

    def return_tws(self):
        tws0 = Twiss()
        tws0.E = 0.005
        tws0.beta_x = 55.7887190242
        tws0.beta_y = 55.7887190242
        tws0.alpha_x = 18.185436973
        tws0.alpha_y = 18.185436973
        return tws0

    def load_lattice(self):
        self.quads = []
        mi_devs = {}
        L = 0
        for elem in self.lat.sequence:
            L += elem.l
            if elem.__class__ in [Quadrupole]:
                elem.s_pos = L - elem.l/2.
                elem.k1_th = elem.k1
                elem.kick_mrad = elem.k1 * elem.l * 1000.
                elem.i_kick = elem.kick_mrad
                self.quads.append(elem)
                #elem.mi = Device(eid="XFEL.MAGNETS/MAGNET.ML/" + elem.id + "/KICK_MRAD.SP")
                if elem.ps_id not in mi_devs.keys():

                    mi_dev = Device(eid="XFEL.MAGNETS/MAGNET.ML/" + elem.id + "/KICK_MRAD.SP")
                    mi_dev.mi = self.mi
                    elem.mi = mi_dev
                    mi_devs[elem.ps_id] = mi_dev
                else:
                    elem.mi = mi_devs[elem.ps_id]

        self.add_devs2table(self.quads)
        #self.init_kick_mrad = np.array([q.kick_mrad for q in self.quads])
        self.quad_ampl = np.max(np.abs(np.array([q.kick_mrad for q in self.quads])))
        self.plot_lat()

    def calc(self):
        #lat = MagneticLattice(cell)


        # L = 0
        for elem in self.lat.sequence:
            if elem.__class__ in [Quadrupole]:
                #print(elem.id, elem.row)
                elem.kick_mrad = elem.ui.get_value()
                elem.k1 = elem.kick_mrad/elem.l/1000.
                if np.abs(np.abs(elem.kick_mrad) - np.abs(elem.i_kick))> 1:
                    self.r_items[elem.ui.row].setBrush(pg.mkBrush("r"))
                    self.ui.tableWidget.item(elem.row, 1).setForeground(QtGui.QColor(255, 101, 101))  # red
                else:
                    self.ui.tableWidget.item(elem.row, 1).setForeground(QtGui.QColor(255, 255, 255))  # white
                    self.r_items[elem.ui.row].setBrush(pg.mkBrush("g"))
                r = self.r_items[elem.ui.row]
                sizes = r.init_params
                #sizes = list(r.boundingRect().getRect())
                sizes[3] = 10*elem.kick_mrad/self.quad_ampl
                r.setRect(sizes[0], sizes[1], sizes[2], sizes[3])

        self.lat.update_transfer_maps()
        print("test")
        # exit(0)
        tws = twiss(self.lat, self.tws0)
        #plot_opt_func(lat, tws, top_plot=["Dx", "Dy"])
        #plt.show()
        beta_x = [tw.beta_x for tw in tws]
        beta_y = [tw.beta_y for tw in tws]
        dx = [tw.Dx for tw in tws]
        dy = [tw.Dy for tw in tws]
        s = [tw.s for tw in tws]
        self.update_plot(s, beta_x, beta_y, dx, dy)

    def add_devs2table(self, devs):
        """ Initialize the UI table object """
        #spin_boxes = [QtGui.QDoubleSpinBox()]*
        self.spin_boxes = []
        for row in range(len(devs)):
            eng = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)
            self.ui.tableWidget.setRowCount(row + 1)
            pv = devs[row].id
            # put PV in the table
            self.ui.tableWidget.setItem(row, 0, QtGui.QTableWidgetItem(str(pv)))
            # put start val in
            self.ui.tableWidget.setItem(row, 1, QtGui.QTableWidgetItem(str(devs[row].kick_mrad)))
            spin_box = QtGui.QDoubleSpinBox()
            spin_box.setStyleSheet("color: rgb(153,204,255); font-size: 16px; background-color:#595959;")
            spin_box.setLocale(eng)
            spin_box.setDecimals(4)
            spin_box.setMaximum(5000)
            spin_box.setMinimum(-5000)
            spin_box.setSingleStep(5)
            spin_box.setValue(devs[row].kick_mrad)

            #dev.k1 = spin_box.value()
            spin_box.setAccelerated(True)
            spin_box.valueChanged.connect(self.calc)
            # spin_box.setFixedWidth(50)
            self.ui.tableWidget.setCellWidget(row, 2, spin_box)
            self.ui.tableWidget.resizeColumnsToContents()
            self.spin_boxes.append(spin_box)
            devs[row].row = row

            ui = DeviceUI()
            ui.tableWidget = self.ui.tableWidget
            ui.row = row
            ui.col = 2
            devs[row].ui = ui


    def add_plot_matplotlib(self):

        #fig = plt.figure()#(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)
        #self.axes = plt.plot([1,2,3,4])
        ##self.compute_initial_figure()
        #
        #FigureCanvas.__init__(self, fig)
        ##self.setParent(parent)
        #
        #FigureCanvas.setSizePolicy(self,
        #                           QtGui.QSizePolicy.Expanding,
        #                           QtGui.QSizePolicy.Expanding)
        #FigureCanvas.updateGeometry(self)
        # a figure instance to plot on
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)
        self.axes.plot([1,2,3])
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)
        # set the layout
        layout = QtGui.QVBoxLayout()

        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        self.ui.widget_2.setLayout(layout)

    def plot_lat(self):
        self.r_items = []
        L = 0.
        for elem in self.lat.sequence:
            a = 1
            L += elem.l
            if elem.__class__ == Quadrupole:
                s = L - elem.l
                r1 = pg.QtGui.QGraphicsRectItem(s, -10, elem.l, 10*elem.k1/self.quad_ampl)
                #print()
                #color = QtGui.QColor(164, 230, 10)
                #pen = pg.mkPen(color, width=1)
                r1.setPen(pg.mkPen(None))
                r1.setBrush(pg.mkBrush("g"))
                r1.init_params = [s, 0, elem.l, 1*elem.k1/self.quad_ampl]
                self.r_items.append(r1)
                self.plot2.addItem(r1)

        #print(self.plot2.items())

    def zoom_signal(self):
        s = self.plot1.viewRange()[0][0]
        s_pos = np.array([q.s_pos for q in self.quads])
        indx = np.argwhere(s_pos>s)[0][0]
        row = self.quads[indx].ui.row
        #self.ui.tableWidget.scrollTo(row)
        item = self.ui.tableWidget.item(row, 2)
        self.ui.tableWidget.scrollToItem(item, QtGui.QAbstractItemView.PositionAtBottom)
        self.ui.tableWidget.selectRow(row)


    def add_plot(self):
        #self.plot1 = pg.PlotWidget(title="Objective Function Monitor",
        #                           labels={'left': str("adsfasf"), 'bottom': "Time (seconds)"})
        #self.ui.verticalLayout_5.setSpacing(0)
        #self.ui.verticalLayout_5.setMargin(0)
        #self.ui.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        #self.ui.verticalLayout_5.setVerticalSpacing(0)
        #self.ui.verticalLayout_5.insertStretch(-1, 1)


        #win = pg.GraphicsWindow()
        win = pg.GraphicsLayoutWidget()
        #win = pg.GraphicsView()
        #gl = pg.GraphicsLayout(border=(100,100,100))
        #w.ci.layout.setRowMaximumHeight(1, 200)
        #gl.setLayout()
        #win.setCentralItem(gl)

        #win.setWindowTitle('pyqtgraph example: crosshair')
        #print(win.size())
        #label = pg.LabelItem(justify='right')
        #win.addItem(label)
        #l2 = gl.addLayout(rowspan=3, border=(50, 0, 0))
        self.plot3 = win.addPlot(row=0, col=0)
        win.ci.layout.setRowMaximumHeight(0, 200)

        self.plot3.showGrid(1, 1, 1)


        self.plot1 = win.addPlot(row=1, col=0)
        self.plot3.setXLink(self.plot1)
        # gl.nextRow()

        #l3 = gl.addLayout(rowspan=1, border=(10, 0, 0))
        #self.plot2 = gl.addPlot(row=5, col=0, rowspan=1)
        #print(self.plot1.resize(800, 400))
        #self.plot2 = win.addPlot(row=2, col=0, rowspan=2)
        self.plot1.showGrid(1, 1, 1)

        self.plot1.getAxis('left').enableAutoSIPrefix(enable=False)  # stop the auto unit scaling on y axes
        layout = QtGui.QGridLayout()
        self.ui.widget_2.setLayout(layout)
        layout.addWidget(win, 0, 0)
        #layout.addWidget(win, 0, 0)

        #region = pg.LinearRegionItem()
        #region.setZValue(10)
        # Add the LinearRegionItem to the ViewBox, but tell the ViewBox to exclude this
        # item when doing auto-range calculations.
        #self.plot2.addItem(region, ignoreBounds=True)

        # pg.dbg()
        self.plot1.setAutoVisible(y=True)

        #self.plot1.showGrid(1, 1, 1)
        #self.plot1.getAxis('left').enableAutoSIPrefix(enable=False)  # stop the auto unit scaling on y axes
        #layout = QtGui.QGridLayout()
        #self.ui.widget_2.setLayout(layout)
        #layout.addWidget(self.plot1, 0, 0)

        self.plot1.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.beta_x = pg.PlotCurveItem(x=[], y=[], pen=pen, name='beta_x', antialias=True)
        self.plot1.addItem(self.beta_x)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=3)
        self.beta_y = pg.PlotCurveItem(x=[], y=[], pen=pen, name='beta_y', antialias=True)
        self.plot1.addItem(self.beta_y)

        self.plot2 = win.addPlot(row=2, col=0)
        win.ci.layout.setRowMaximumHeight(2, 150)

        #self.plot2.showAxis('left', False)
        #self.plot2.showAxis('bottom', False)
        self.plot2.setXLink(self.plot1)
        self.plot2.showGrid(1, 1, 1)

        self.plot3.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.Dx = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Dx', antialias=True)
        self.plot3.addItem(self.Dx)

        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=3)
        self.Dy = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Dy', antialias=True)
        self.plot3.addItem(self.Dy)
        self.plot2.sigRangeChanged.connect(self.zoom_signal)
        #win2 = pg.GraphicsWindow()
        #self.beta = pg.PlotCurveItem(x=[], y=[], pen=pen, name='test', antialias=True)
        #self.plot2 = win2.addPlot()
        #self.plot2.showAxis('bottom', False)
        #self.plot2.showAxis('left', False)
        #self.plot2.addItem(self.beta)

        #layout2 = QtGui.QGridLayout()

        #layout2.addWidget(win2, 0, 0)
        #self.ui.widget_3.setLayout(layout2)


        #layout.setContentsMargins(-1, -1, -1, 0)
        #layout2.setContentsMargins(-1, 0, -1, -1)

        #def update():
        #    region.setZValue(10)
        #    minX, maxX = region.getRegion()
        #    self.plot1.setXRange(minX, maxX, padding=0)
        #
        #region.sigRegionChanged.connect(update)
        #
        #def updateRegion(window, viewRange):
        #    rgn = viewRange[0]
        #    region.setRegion(rgn)
        #
        #self.plot1.sigRangeChanged.connect(updateRegion)
        #
        #region.setRegion([0, 100])

        #vb = win.addViewBox(col=0, row=1)
        #r1 = pg.QtGui.QGraphicsRectItem(0, 0, 0.4, 1)
        #r1.setPen(pg.mkPen(None))
        #r1.setBrush(pg.mkBrush('r'))
        #self.plot2.addItem(r1)
        #r2 = pg.QtGui.QGraphicsRectItem(0.2, -5, 0.1, 10)
        #r2.setPen(pg.mkPen((0, 0, 0, 100)))
        #r2.setBrush(pg.mkBrush((50, 50, 200)))
        #self.plot2.addItem(r2)

    def update_plot(self, s, bx, by, dx, dy):
        # Line
        self.beta_x.setData(x=s, y=bx)
        self.beta_y.setData(x=s, y=by)
        self.plot1.update()
        self.plot2.update()
        self.Dx.setData(x=s, y=dx)
        self.Dy.setData(x=s, y=dy)
        self.plot3.update()


    def loadStyleSheet(self):
        """ Sets the dark GUI theme from a css file."""
        try:
            self.cssfile = "style.css"
            with open(self.cssfile, "r") as f:
                self.setStyleSheet(f.read())
        except IOError:
            print ('No style sheet found!')







def main():


    #make pyqt threadsafe
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_X11InitThreads)
    #create the application
    app    = QApplication(sys.argv)


    window = ManulInterfaceWindow()





    #show app
    #window.setWindowIcon(QtGui.QIcon('ocelot.png'))
    window.show()

    #Build documentaiton if source files have changed
    # TODO: make more universal
    #os.system("cd ./docs && xterm -T 'Ocelot Doc Builder' -e 'bash checkDocBuild.sh' &")
    #exit script
    sys.exit(app.exec_())

if __name__ == "__main__":

    main()
"""
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np

win = pg.plot()
win.setWindowTitle('pyqtgraph example: FillBetweenItem')
win.setXRange(-10, 10)
win.setYRange(-10, 10)

N = 200
x = np.linspace(-10, 10, N)
gauss = np.exp(-x ** 2 / 20.)
mn = mx = np.zeros(len(x))
curves = [win.plot(x=x, y=np.zeros(len(x)), pen='k') for i in range(4)]
brushes = [0.5, (100, 100, 255), 0.5]
fills = [pg.FillBetweenItem(curves[i], curves[i + 1], brushes[i]) for i in range(3)]
for f in fills:
    win.addItem(f)


def update():
    global mx, mn, curves, gauss, x
    a = 5 / abs(np.random.normal(loc=1, scale=0.2))
    y1 = -np.abs(a * gauss + np.random.normal(size=len(x)))
    y2 = np.abs(a * gauss + np.random.normal(size=len(x)))

    s = 0.01
    mn = np.where(y1 < mn, y1, mn) * (1 - s) + y1 * s
    mx = np.where(y2 > mx, y2, mx) * (1 - s) + y2 * s
    curves[0].setData(x, mn)
    curves[1].setData(x, y1)
    curves[2].setData(x, y2)
    curves[3].setData(x, mx)


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(30)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
"""