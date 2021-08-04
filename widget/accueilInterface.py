import sys
from PyQt5 import QtWidgets
from widget import accueilWidget
from .transformInterface import Transcription
from .listeHistoInterface import ListProjet




class Accueil(QtWidgets.QMainWindow, accueilWidget.Ui_Home):
    def __init__(self, parent=None):
        super(Accueil, self).__init__(parent)
        self.setupUi(self)
        self.cretion_btn.clicked.connect(self.lancer_creation)
        self.projets_btn.clicked.connect(self.lancer_projets)
        


    
    def lancer_creation(self):
        self.win = Transcription()
        self.win.show()
    

    def lancer_projets(self):
        self.win = ListProjet()
        self.win.show()