import sys
from PyQt5 import QtWidgets
from widget import listeHistoWidget



class ListProjet(QtWidgets.QMainWindow, listeHistoWidget.Ui_ListHisto):
    def __init__(self):
        super().__init__()
        self.setupUi(self)




