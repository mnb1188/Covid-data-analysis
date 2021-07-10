from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from load import Wczytywanie
from lista_krajów import Lista_krajow




class Przycisk(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Wczytywanie pliku o zachorowaniach na COVID"
        self.text = "Wczytaj plik"
        self.left = 200
        self.top = 200
        self.width = 500
        self.height = 400
        self.setGeometry(100, 100, 800, 800)
        self.window()

    def window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.button = QtWidgets.QPushButton(self.text, self)
        self.button.move((self.width)/2-40,(self.height/2)-10)
        self.button.clicked.connect(self.press)

    def press(self):
        pass


class Wczytaj(Przycisk):

    def __init__(self):
        super().__init__()
        self.__countdata = Lista_krajow()

    def press(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        self.checkfile(path)

        fileload = Wczytywanie()
        countries_data = fileload.get_count(path)
        self.__countdata.create_lists(countries_data)
        self.close()

    def get_count(self):
        return self.__countdata.get_kraje()

    def get_vect(self):
        return self.__countdata.get_wektory()

    def checkfile(self, path):
        if path != "csv":
            try:
                raise ImproperFileException("Wrong file type! Please choose a proper .csv file")
            except ImproperFileException as e:
                print(e)


class ImproperFileException(Exception):

    def __init__(self, message):
        self.__message = message
