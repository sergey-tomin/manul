"""
Sergey Tomin, XFEL/DESY, 2018
"""

import sys, os
from decimal import Decimal
import time
import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
#from mint.xfel_interface import XFELMachineInterface, TestMachineInterface
#from machine_interface import *

#mi = XFELMachineInterface()
#mi = TestMachineInterface()




class Statistics():
    def __init__(self, device, npoints=100, delay=100):
        self.delay = delay
        self.N = npoints
        self.device = device
        self.dx = []
        self.dy = []
        #self.spots = []
        self.sig_y = np.empty(self.N)
        self.sig_x = np.empty(self.N)
        self.cur_inx = 0

        self.sigmas_title = "Sigma X/Y"
        self.x_hist_title = "X pos Distrib"
        self.y_hist_title = "Y pos Distrib"
        self.scatter_title = "Correlation"
        self.win = pg.GraphicsWindow()
        self.win.resize(800, 800)
        self.win.setWindowTitle('Photon beam pointing: XGM.2643.T9')

        self.setup_ui()



        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update)

    def set_titles(self):
        self.scat_plot.setTitle(self.scatter_title)
        self.plot_x_hist.setTitle(self.x_hist_title)
        self.plot_y_hist.setTitle(self.y_hist_title)
        self.sigmas.setTitle(self.sigmas_title)

    def setup_ui(self):

        self.plot_x_hist = self.win.addPlot(row=0, col=0, title=self.x_hist_title)
        self.plot_x_hist.showGrid(1, 1, 1)
        self.plot_x_hist.hideAxis('bottom')
        self.data_hist_x = pg.PlotDataItem([0,0], [0], stepMode=True, fillLevel=0, brush=(255, 0, 0, 100))

        self.plot_x_hist.addItem(self.data_hist_x)
        
        self.scat_plot = self.win.addPlot(row=1, col=0, rowspan=1, title=self.scatter_title)
        self.scat_plot.showGrid(1, 1, 1)
        self.scat_plot.setXLink(self.plot_x_hist)
        
        self.plot_y_hist = self.win.addPlot(row=1, col=1, title=self.y_hist_title)
        self.plot_y_hist.showGrid(1, 1, 1)
        self.plot_y_hist.hideAxis('left')

        self.sigmas = self.win.addPlot(row=0, col=1, title=self.sigmas_title)
        self.sigmas.showGrid(1, 1, 1)
        
        color = QtGui.QColor(255, 0, 0)
        pen = pg.mkPen(color, width=4)
        self.plt_sig_x = pg.PlotDataItem(x=[], y=[], pen=pen, symbol=None, name='X', antialias=True)
        self.sigmas.addItem(self.plt_sig_x )
        
        
        color = QtGui.QColor(255, 255, 0)
        pen = pg.mkPen(color, width=4)
        self.plt_sig_y = pg.PlotDataItem(x=[], y=[], pen=pen, symbol=None, name='Y', antialias=True)
        self.sigmas.addItem(self.plt_sig_y )
        #sigmas.addLegend()
        
        self.data_hist_y = pg.PlotDataItem([0,0], [0], stepMode=True, fillLevel=0, brush=(255, 255, 0, 200))
        self.data_hist_y.rotate(-90)
        self.plot_y_hist.addItem(self.data_hist_y)
        self.plot_y_hist.setYLink(self.scat_plot)
        
        
        
        self.scatter = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(255, 100, 255, 120))
        self.scat_plot.addItem(self.scatter)


    def update(self):
        #global dx, dy, spots, i, sig_y, sig_x

        x = self.device.get_x()
        y = self.device.get_y()
        if len(self.dx) > self.N:
            self.dx = np.delete(self.dx, 0)
            self.dy = np.delete(self.dy, 0)

        if self.cur_inx >= self.sig_y.shape[0]:

            tmp = self.sig_y
            self.sig_y = np.empty(self.sig_y.shape[0] * 2)
            self.sig_y[:tmp.shape[0]] = tmp

            tmpx = self.sig_x
            self.sig_x = np.empty(self.sig_x.shape[0] * 2)
            self.sig_x[:tmpx.shape[0]] = tmpx

        self.dx = np.append(self.dx, x)
        self.dy = np.append(self.dy, y)

        y_hist, x_hist = np.histogram(self.dx, bins=100)
        y_hist_y, x_hist_y = np.histogram(self.dy, bins=100)
        self.data_hist_y.setData(x_hist_y, y_hist_y)
        sigy = np.std(self.dy)
        self.data_hist_x.setData(x_hist, y_hist)


        self.scatter.setData(self.dx, self.dy)
        sigx = np.std(self.dx)

        self.sig_y[self.cur_inx] = sigy
        self.sig_x[self.cur_inx] = sigx
        self.plt_sig_y.setPos(-self.cur_inx, 0)
        self.plt_sig_x.setPos(-self.cur_inx, 0)
        datay = self.sig_y[:self.cur_inx]
        self.plt_sig_y.setData(np.arange(len(datay)), datay)

        datax = self.sig_x[:self.cur_inx]
        self.plt_sig_x.setData(np.arange(len(datax)), datax)
        #txt_sigma_x.setText("sigma_x="+'%.2E' % Decimal(str(sigx)))
        if self.cur_inx > 50 and  self.cur_inx % self.N == 0:
            #print("here")
            data = np.append(datay[-self.N:], datax[-self.N:])
            self.sigmas.setRange(yRange=[np.min(data), np.max(data)])
        self.cur_inx += 1

    def start(self):
        self.dx = []
        self.dy = []
        #self.spots = []
        self.sig_y = np.empty(self.N)
        self.sig_x = np.empty(self.N)
        self.cur_inx = 0
        self.sigmas.setRange(xRange=[-self.N, 0])
        self.timer.start(self.delay)

    def stop(self):
        self.timer.stop()




#timer_bc1 = pg.QtCore.QTimer()
#timer_bc1.timeout.connect(update_bc1)
#timer_bc1.start(100)

#timer_bc2 = pg.QtCore.QTimer()
#timer_bc2.timeout.connect(update_bc2)
#timer_bc2.start(100)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()