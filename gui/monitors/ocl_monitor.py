"""
S.Tomin PyQtGraph monitor
"""

import sys
from PyQt5.QtWidgets import QCheckBox,QPushButton, QHBoxLayout, QHeaderView, QApplication,QMenu, QWidget, QAction, QTableWidget, QTableWidgetItem, QDoubleSpinBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from gui.monitors.ui_ocl_monitor import *
import numpy as np
import pyqtgraph as pg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class OclMonitor(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.title = 'Twiss'
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        #make the custom table for middle click
        #self.ui.tableWidget.setParent(None) #remove old table
        #self.ui.tableWidget = CustomTableWidget(self) # make new widget
        #self.ui.gridLayout_2.addWidget(self.ui.tableWidget, 0, 0)
        #self.createTable()
        self.add_plot()
        self.loadStyleSheet()

    def loadStyleSheet(self):
        """ Load in the dark theme style sheet. """
        try:
            self.cssfile = "style.css"
            with open(self.cssfile, "r") as f:
                self.setStyleSheet(f.read())
        except IOError:
            print('No style sheet found!')



    def zoom_signal(self):
        pass
        # s = self.plot1.viewRange()[0][0]
        # s_pos = np.array([q.s_pos for q in self.quads])
        #s_pos = np.array([q.s_pos for q in self.quads]) + self.lat_zi
        #s_up = self.plot1.viewRange()[0][0]
        #s_down = self.plot1.viewRange()[0][1]
        #s_up = s_up if s_up <= s_pos[-1] else s_pos[-1]
        #s_down = s_down if s_down >= s_pos[0] else s_pos[0]
        #indexes = np.arange(np.argwhere(s_pos >= s_up)[0][0], np.argwhere(s_pos <= s_down)[-1][0] + 1)
        #mask = np.ones(len(self.quads), np.bool)
        #mask[indexes] = 0
        #self.quads = np.array(self.quads)
        #[q.ui.set_hide(hide=False) for q in self.quads[indexes]]
        #[q.ui.set_hide(hide=True) for q in self.quads[mask]]

    def update_plot(self, sx, delta_x, sk, delta_k):
        # Line
        #s = np.array(sx) #+ self.lat_zi
        self.delta_x.setData(x=sx, y=delta_x)
        self.bpm_plot.update()
        self.delta_k.setData(x=sk, y=delta_k)
        self.cor_plot.update()

    #def update_plot_track(self, s, bx, by, E):
    #    # Line
    #    s = np.array(s) #+ self.lat_zi
    #    self.delta_x.setData(x=s, y=bx)
    #    #self.beta_y.setData(x=s, y=by)
    #    self.bpm_plot.update()
    #    #self.plot1.setYRange(-5, 200)
    #    #self.plot2.update()
    #    self.cor_plot.removeItem(self.delta_k)
    #    self.cor_plot.update()

    def add_plot(self):
        win = pg.GraphicsLayoutWidget()
        self.cor_plot = win.addPlot(row=0, col=0)
        win.ci.layout.setRowMaximumHeight(0, 200)
        self.cor_plot.showGrid(1, 1, 1)
        self.bpm_plot = win.addPlot(row=1, col=0)
        self.cor_plot.setXLink(self.bpm_plot)
        self.bpm_plot.showGrid(1, 1, 1)
        self.bpm_plot.getAxis('left').enableAutoSIPrefix(enable=False)  # stop the auto unit scaling on y axes
        layout = QtGui.QGridLayout()
        layout.setContentsMargins(0,0,0,0)
        self.ui.w_monitor.setLayout(layout)
        layout.addWidget(win, 0, 0)
        self.bpm_plot.setAutoVisible(y=True)
        self.bpm_plot.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.delta_x = pg.PlotCurveItem(x=[], y=[], pen=pen, name='dX', antialias=True)
        self.bpm_plot.addItem(self.delta_x)

        #pen = pg.mkPen(color, width=1)
        #self.beta_x_des = pg.PlotCurveItem(x=[], y=[], pen=pen, name='beta_x', antialias=True)
        #self.bpm_plot.addItem(self.beta_x_des)

        #color = QtGui.QColor(255, 0, 0)
        #pen = pg.mkPen(color, width=3)
        #self.beta_y = pg.PlotCurveItem(x=[], y=[], pen=pen, name='beta_y', antialias=True)
        #self.bpm_plot.addItem(self.beta_y)
        #color = QtGui.QColor(255, 0, 0)
        #pen = pg.mkPen(color, width=1)
        #self.beta_y_des = pg.PlotCurveItem(x=[], y=[], pen=pen, name='beta_y', antialias=True)
        #self.bpm_plot.addItem(self.beta_y_des)

        #self.plot2 = win.addPlot(row=2, col=0)
        #win.ci.layout.setRowMaximumHeight(2, 150)
        #self.plot2.setXLink(self.plot1)
        #self.plot2.showGrid(1, 1, 1)

        self.cor_plot.addLegend()
        color = QtGui.QColor(0, 255, 255)
        pen = pg.mkPen(color, width=3)
        self.delta_k = pg.PlotCurveItem(x=[], y=[], pen=pen, name='delta_kick', antialias=True)
        self.cor_plot.addItem(self.delta_k)

        #color = QtGui.QColor(255, 0, 0)
        #pen = pg.mkPen(color, width=3)
        #self.Dy = pg.PlotCurveItem(x=[], y=[], pen=pen, name='Dy', antialias=True)
        #self.cor_plot.addItem(self.Dy)
        #self.plot2.sigRangeChanged.connect(self.zoom_signal)

    #@pyqtSlot()
    #def on_click(self):
    #    print("\n")
    #    for currentQTableWidgetItem in self.ui.tableWidget.selectedItems():
    #        print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OclMonitor()
    window.show()
    sys.exit(app.exec_())