"""
S.Tomin Table for sections
"""

import sys
from PyQt5.QtWidgets import QCheckBox, QHBoxLayout, QHeaderView, QApplication,QMenu, QWidget, QAction, QTableWidget, QTableWidgetItem, QDoubleSpinBox
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
#from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from gui.tables.ui_ocl_table import *
import json
#from gui.device.device_ui import SectionUI

class CustomTableWidget(QTableWidget):
    """
    Subclass the tablewidget to add a custom PV on middle click.
    """
    def __init__(self, parent=None):
        """Init for the table widget, nothing special here"""
        QTableWidget.__init__(self, parent)
        self.parent = parent
        self.doubleClicked.connect(self.double_click)
        self.last_row = None

    def double_click(self):
        print("double click")

        for currentQTableWidgetItem in self.parent.ui.tableWidget.selectedItems():

            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def mouseReleaseEvent(self, evt):
        """
        Grabs string from the clipboard if middle button click.

        Tries to then add the PV to the parent GUI pv lists.
        Calls parent.addPv() method.

        Args:
                evt (QEvent): Event object passed in from QT
        """
        button = evt.button()
        #print("TW Release event: ", button)
        if button == 4:

            pv = QApplication.clipboard().text()
            print(pv)
            #self.parent.addPv(pv)
            #print(QtGui.QApplication.clipboard().text())
        elif button == 1:
            for currentQTableWidgetItem in self.parent.ui.tableWidget.selectedItems():
                #print(currentQTableWidgetItem.row())
                self.last_row = currentQTableWidgetItem.row()
        #    #print()
        #
        #    #pv = QApplication.clipboard().text()
        #    #print(pv)
        #    #self.parent.addPv(pv)
        #    #print(QtGui.QApplication.clipboard().text())
        #    for currentQTableWidgetItem in self.parent.ui.tableWidget.selectedItems():
        #        print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
        #        if currentQTableWidgetItem.checkState() == QtCore.Qt.Checked:
        #            currentQTableWidgetItem.setCheckState(QtCore.Qt.Unchecked)
        #            print(currentQTableWidgetItem.checkState(), QtCore.Qt.Unchecked)
        #        else:
        #            currentQTableWidgetItem.setCheckState(QtCore.Qt.Checked)
        else:
            QTableWidget.mouseReleaseEvent(self, evt)


    def contextMenuEvent(self, event):
        if self.selectionModel().selection().indexes():
            rows = []
            cols = []
            for i in self.selectionModel().selection().indexes():
                row, column = i.row(), i.column()
                rows.append(row)
                cols.append(column)
            self.menu = QMenu(self)

            #deleteAction = QAction('Delete', self)
            checkAction = QAction('Check', self)
            uncheckAction = QAction('Uncheck', self)
            #deleteAction.triggered.connect(lambda: self.deleteSlot(rows))
            checkAction.triggered.connect(lambda: self.checkSlot())
            uncheckAction.triggered.connect(lambda: self.uncheckSlot())
            self.menu.addAction(checkAction)
            self.menu.addAction(uncheckAction)
            #editAction = QtGui.QAction('Edit', self)
            #self.menu.addAction(editAction)
            # add other required actions
            self.menu.popup(QtGui.QCursor.pos())


    def deleteSlot(self, rows):
        print ("delete rows called", rows)
        for row in rows[::-1]:
            self.parent.ui.tableWidget.removeRow(row)

        table = self.parent.get_state()
        pvs = table["id"]
        self.parent.getPvList(pvs)
        self.parent.uncheckBoxes()
        self.parent.set_state(table)

    def checkSlot(self):
        for currentQTableWidgetItem in self.parent.ui.tableWidget.selectedItems():
            #if currentQTableWidgetItem.column() != 0:
            currentQTableWidgetItem.setCheckState(QtCore.Qt.Checked)

    def uncheckSlot(self):
        for currentQTableWidgetItem in self.parent.ui.tableWidget.selectedItems():
            #if currentQTableWidgetItem.column() != 0:
            currentQTableWidgetItem.setCheckState(QtCore.Qt.Unchecked)


class OclTable(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.title = 'Test Table'
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        #make the custom table for middle click
        self.ui.tableWidget.setParent(None) #remove old table
        self.ui.tableWidget = CustomTableWidget(self) # make new widget
        self.ui.gridLayout_2.addWidget(self.ui.tableWidget, 0, 0, 1, 3)
        self.ui.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.h_headers = ["id", "timestamp", "sase", "author", "comment"]
        self.create_table(h_headers=self.h_headers )

        self.loadStyleSheet()


    def loadStyleSheet(self):
        """ Load in the dark theme style sheet. """
        try:
            self.cssfile = "style.css"
            with open(self.cssfile, "r") as f:
                self.setStyleSheet(f.read())
        except IOError:
            print('No style sheet found!')

    def get_state(self):
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                print(self.ui.tableWidget.cellWidget(row, col))
                print(self.ui.tableWidget.item(row, col).checkState())
                #self.ui.tableWidget.cellWidget(row, col).value()

    def close(self):
        self.save_state("asdf")

    def save_state(self, filename):
        # pvs = self.ui.widget.pvs
        table = {}
        v_headers = [self.check_header] + self.phys_proc_names
        for col, sec in enumerate(self.sections):
            for row, r_name in enumerate(v_headers):
                item = self.ui.tableWidget.item(row, col)
                table[row,col] = item.flags()
                #print(item.flags())

        #with open(filename, 'w') as f:
        #    json.dump(table, f)
        ## pickle.dump(table, filename)
        #print("SAVE State")

    def restore_state(self, filename):
        # try:
        with open(filename, 'r') as f:
            # data_new = pickle.load(f)
            table = json.load(f)
        pass


    def init_table(self, dict_list, editable=True):
        """
        Creates additional column in UI table for check box.

        Must be called again if the user adds another PV with middle click function.
        """
        self.ui.tableWidget.setRowCount(len(dict_list))
        for row, mf in enumerate(dict_list):
            for col, header in enumerate(self.h_headers):
                val = dict_list[row][header]
                if type(val) is str:
                    val = val.replace("#xKOM", "")
                self.ui.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(val)))
        #self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        if not editable:
            self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)




    def create_table(self, h_headers):
        self.h_headers = h_headers
        self.ui.tableWidget.setColumnCount(len(h_headers))
        self.ui.tableWidget.setHorizontalHeaderLabels(h_headers)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)



    #@pyqtSlot()
    #def on_click(self):
    #    print("\n")
    #    for currentQTableWidgetItem in self.ui.tableWidget.selectedItems():
    #        print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OclTable()
    window.show()
    sys.exit(app.exec_())