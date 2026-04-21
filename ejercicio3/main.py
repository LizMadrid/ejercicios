import sys
from PyQt6 import QtWidgets, uic
from sub_process import Riego

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicio3/mainthr.ui", self)
        self.btn_riego.clicked.connect(self.start)
        self.sub_process = None

    def start(self):
        zonas = int(self.txt_zon.text())
        horas = int(self.txt_ho.text())

        self.btn_riego.setEnabled(False)
        self.txt_zon.setEnabled(False)
        self.txt_ho.setEnabled(False)

        self.sub_process = Riego(zonas, horas)
        self.sub_process.update_progress.connect(self.update_barras)
        self.sub_process.finished.connect(self.fin)
        self.sub_process.start()

    def update_barras(self, zona_actual, p_zona, p_total):
        self.lbl_zon.setText(f"Regando Zona: {zona_actual}")
        self.progress_bar_zon.setValue(p_zona)
        self.progress_bar_tot.setValue(p_total)

    def fin(self):
        self.btn_riego.setEnabled(True)
        self.txt_zon.setEnabled(True)
        self.txt_ho.setEnabled(True)
        self.lbl_zon.setText("Riego finalizado")

app = QtWidgets.QApplication(sys.argv)
window = MainWindow() 
window.show()
sys.exit(app.exec())                    