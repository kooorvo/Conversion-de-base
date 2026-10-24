import sys

import pyperclip as pc

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt, QTimer
from PyQt6 import uic 

from conv.binDec import dec_to_bin, bin_to_dec
from conv.duodec import dec_to_duodec, duo_to_dec
from conv.hexa import dec_to_hexa, hexa_to_dec

class App(QMainWindow):
    def __init__(self):
        super().__init__() # on initialise la classe parente QMainWindow

        uic.loadUi("ui/interface.ui", self)

        try:
            with open("ui/style.qss", "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print("Fichier style.qss introuvable.")            

        self.setFixedSize(self.size()) # Bloque la taille de la fenêtre

        self.convBtn.clicked.connect(self.convClicked)
        self.copierBtn.clicked.connect(self.copier)

    def convClicked(self):
        combo1 = int(self.baseDep.currentIndex())
        combo2 = int(self.baseF.currentIndex())
        aconv = self.aconv.text()
        match (combo1, combo2):
            case (0, 0):
                self.convFLabel.setText(dec_to_bin(int(aconv)))
            case (0, 1):
                self.convFLabel.setText(f"{aconv}")
            case (0, 2):
                self.convFLabel.setText(dec_to_duodec(int(aconv)))
            case (0, 3):
                self.convFLabel.setText(dec_to_hexa(int(aconv)))
            case (1, 0):
                self.convFLabel.setText(f"{aconv}")
            case (1, 1):
                self.convFLabel.setText(str(bin_to_dec(aconv)))
            case (1, 2):
                dec = bin_to_dec(aconv)
                self.convFLabel.setText(dec_to_duodec(int(dec)))
            case (1, 3):
                dec = bin_to_dec(aconv)
                self.convFLabel.setText(dec_to_hexa(int(dec)))
            case (2, 0):
                dec = duo_to_dec(aconv)
                self.convFLabel.setText(dec_to_bin(int(dec)))
            case (2, 1):
                self.convFLabel.setText(str(duo_to_dec(aconv)))
            case (2, 2):
                self.convFLabel.setText(f"{aconv}")
            case (2, 3):
                dec = duo_to_dec(aconv)
                self.convFLabel.setText(dec_to_hexa(int(dec)))
            case (3, 0):
                dec = hexa_to_dec(aconv)
                self.convFLabel.setText(dec_to_bin(int(dec)))
            case (3, 1):
                self.convFLabel.setText(str(hexa_to_dec(aconv)))
            case (3, 2):
                dec = hexa_to_dec(aconv)
                self.convFLabel.setText(dec_to_duodec(int(dec)))
            case (3, 3):
                self.convFLabel.setText(f"{aconv}")

    def copier(self):
        conv = self.convFLabel.text()
        pc.copy(conv)
        self.copierBtn.setText("Copié !")
        #On peut pas utiliser time, ça bloque l'app²
        QTimer.singleShot(2000, lambda : self.copierBtn.setText("Copier"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = App()
    fenetre.show()  # Affiche la fenêtre à l'écran
    sys.exit(app.exec())