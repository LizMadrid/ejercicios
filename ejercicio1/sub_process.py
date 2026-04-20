import time
from PyQt6.QtCore import QThread, pyqtSignal

class SubProcess(QThread):
    update_value = pyqtSignal(int, int)
    def __init__(self, capacidad, corriente, tiempores):
        super().__init__()
        self.capacidad = capacidad
        self.corriente = corriente
        self.tiempores = tiempores
        self.cont = 0

    def run(self):
        t = self.tiempores
        while self.cont < 80:
            print(t)
            self.tiempores -= 60
            self.cont += round(100/(self.capacidad/self.corriente))
            self.update_value.emit(self.cont, self.tiempores)
            time.sleep(3)
        while self.cont < 100:
            time.sleep(6)
            self.tiempores -= 30 
            self.cont +- round(25/(self.capacidad/self.corriente))
            self.update_value.emit(self.cont, self.tiempores)   
