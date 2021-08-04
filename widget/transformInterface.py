import sys
from  PyQt5 import QtWidgets
from widget import transformWidget



class Transcription(QtWidgets.QMainWindow, transformWidget.Ui_Transform):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    
