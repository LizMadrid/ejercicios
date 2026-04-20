import sys
import random
from PyQt6 import QtWidgets, uic, QtCore
from sub_process import ProcesadorImg

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        