from lista_krajów import Lista_krajow
from przycisk import Wczytaj, QApplication
from przycisk_kraj import Przycisk_kraj
import sys

count_data = Lista_krajow()

app = QApplication(sys.argv)
win = Wczytaj()
win.show()
app.exec_()
print("done")
count_data.join_count(win.get_count())                              # tworzy listę krajów
count_data.join_vect(win.get_vect())                                # tworzy listę wektorów
y = list(range(0, len(count_data.get_wektory()[0])))

win_kraj = Przycisk_kraj(count_data.get_kraje(), count_data.get_wektory())
win_kraj.show()


c = app.exec()
sys.exit(c)








