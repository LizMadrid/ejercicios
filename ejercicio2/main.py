import sys
import random
from PyQt6 import QtWidgets, uic, QtCore
from sub_process import ProcesadorImg

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicio2/maintw.ui", self)
        self.btn_process.clicked.connect(self.start_process)
        self.sub_process = None


    def start_process(self):
        resolucion = self.combo_res.currentText()
        lineas_totales = 1080 if "FHD" in resolucion else 1440 if "2K" in resolucion else 2160 
        complejidad = self.slider_compl.value()

        self.progress_bar.setValue(0)
        self.sub_process = ProcesadorImg(lineas_totales, complejidad)
        self.sub_process.update_ui.connect(self.update_value)
        self.sub_process.start()

    def update_value(self, lineas, porcentaje):
        self.progress_bar.setValue(porcentaje)
        self.lbl_info.setText(f"Líneas: {lineas} de {self.progress_bar.maximum()}")

        color = "#{:06x}".format(random.randint(0,0xFFFFFF))
        self.lbl_color.setStyleSheet(f"background-color: {color};")

app = QtWidgets.QApplication(sys.argv)
window = MainWindow() 
window.show()
sys.exit(app.exec())           