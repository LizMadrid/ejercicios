import time
from PyQt6.QtCore import QThread, pyqtSignal

class Riego(QThread):
    update_progress = pyqtSignal(int, int, int)

    def __init__(self, zonas, horas):
        super().__init__()
        self.zonas = zonas
        self.horas = horas

    def run(self):
        for z in range(1, self.zonas +1):
            for h in range(1, self.horas + 1):
                time.sleep(1)

                p_zona = int((h/self.horas)* 100)
                horas_totales =self.zonas * self.horas
                horas_actuales = ((z-1) * self.horas) +h
                p_total = int((horas_actuales/horas_totales)*100)

                self.update_progress.emit(z,p_zona, p_total)    