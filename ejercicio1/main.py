import sys
import time
from PyQt6 import QtWidgets, uic, QtCore
from sub_process import SubProcess

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicio1/main.ui", self)
        self.btn_start.clicked.connect(self.charge)
        self.sub_process = None

    def charge(self):
        try:
            capacidad = float(self.txt_cap.text())
            corriente = float(self.txt_curr.text())
            tiempores = 360
            print(capacidad, corriente)
            self.progress_bar.setValue(0)
            self.sub_process = SubProcess(capacidad, corriente, tiempores)
            self.sub_process.update_value.connect(self.update_progress_bar)
            self.sub_process.start()
        except ValueError as error:
            print(error)        

    def update_progress_bar(self,value, tim):
        if value <= 100:
            self.lbl_tim.setText(str(tim)+" minutos")
            self.progress_bar.setValue(value)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())                    