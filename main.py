import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt

from binDec import dec_to_bin, bin_to_dec
from duodec import dec_to_duodec
from hexa import dec_to_hexa

class App(QMainWindow):
    def __init__(self):
        super().__init__() # on initialise la classe parente QMainWindow




if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    fenetre = App()
    fenetre.show()  # Affiche la fenêtre à l'écran
    
    sys.exit(app.exec())