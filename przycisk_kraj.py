from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QScrollArea, QFormLayout, QGroupBox)
from projekt_wykres import Wykres


class Przycisk_kraj(QWidget):
    def __init__(self, nazwa, data):
        super().__init__()
        self.setWindowTitle("Przycisk kraje")
        self.text = nazwa
        self.data = data
        self.__active_btn = []
        self.formlayout = QFormLayout()
        self.setGeometry(100, 100, 800, 800)

        groupbox = QGroupBox()
        buttonlist = []

        for i in range(len(nazwa)):
            self.btn = QPushButton(self.text[i])
            func = lambda _, text=self.btn.text(): self.press(text)
            self.btn.clicked.connect(func)
            buttonlist.append(self.btn)
            self.formlayout.addRow(buttonlist[i])

        groupbox.setLayout(self.formlayout)
        scroll = QScrollArea()
        scroll.setWidget(groupbox)
        scroll.setWidgetResizable(True)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(scroll)
        self.x = list(range(len(self.data[0])))
        self.wykres = Wykres(self.x, [self.znajdz_wektor(self.text[1])])
        self.layout.addWidget(self.wykres)
        self.wykres.clear()
        self.btn.clear = QPushButton("clear")
        self.btn.clear.clicked.connect(self.clear_func)
        self.layout.addWidget(self.btn.clear)

    def press(self, text):
        if text not in self.__active_btn:
            self.__active_btn.append(text)
            self.wykres.clear()
            self.wykres.rysuj(self.x, self.znajdz_wektor(text), text)
            for cou in self.__active_btn:
                self.wykres.rysuj(self.x, self.znajdz_wektor(cou), cou)

        elif text in self.__active_btn:
            self.__active_btn.remove(text)
            self.wykres.clear()
            for cou in self.__active_btn:
                self.wykres.rysuj(self.x, self.znajdz_wektor(cou), cou)
        print(self.get_pressed())

    def get_pressed(self):
        return self.__active_btn

    def znajdz_wektor(self, count):
        n = 0
        for country in self.text:
            if country == count:
                break
            else:
                n += 1

        return self.data[n]

    def clear_func(self):
        self.wykres.clear()
        self.__active_btn = []

