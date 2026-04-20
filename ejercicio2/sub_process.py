import time
from PyQt6.QtCore import QThread, pyqtSignal

class ProcesadorImg(QThread):
    update_ui = pyqtSignal(int, int)

    def __init__(self, totales, complejidad):
        super().__init__()
        self.totales = totales
        self.complejidad = complejidad

    def run(self):
        procesadas = 0
        tiempo_espera = 0.01 * self.complejidad

        while procesadas < self.totales:
            time.sleep(tiempo_espera)
            procesadas += 100

            if procesadas > self.totales:
                procesadas = self.totales

            porcentaje = int((procesadas/ self.totales)*100)
            self.update_ui.emit(procesadas,porcentaje)        


         