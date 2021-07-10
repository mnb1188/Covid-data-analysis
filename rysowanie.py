import matplotlib
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Rysowanie(QtWidgets.QMainWindow):

    def __init__(self, x, y):
        super(Rysowanie, self).__init__()
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot(x, y)
        self.setCentralWidget(sc)
