from PyQt5 import QtWidgets
import pyqtgraph as pg
import random


class Wykres(QtWidgets.QMainWindow):

    def __init__(self, x, ylist):
        super().__init__()
        self.setWindowTitle("wykres")
        self.graphWidget = pg.PlotWindow()
        self.setCentralWidget(self.graphWidget)
        self.x = x
        self.ylist = ylist
        self.graphWidget.setLabel('left', 'liczba zachorowań', color='white', size=30)
        self.graphWidget.setLabel('bottom', 'dni', color='white', size=30)

        for y in self.ylist:
            self.graphWidget.plot(self.x, y)

    def clear(self):
        self.graphWidget.clear()

    def rysuj(self, x, y, name):
        options = ['b', 'g', 'r', 'c', 'm', 'y', 'w']
        self.graphWidget.plot(x, y, name='%s'%name, pen='%s' % (random.choice(options)))
        self.graphWidget.addLegend()

