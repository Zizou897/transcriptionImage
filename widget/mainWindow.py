from posixpath import splitdrive, splitext
from re import split
import sys
import os
import shutil
import pytesseract
import PIL
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.uic import loadUiType
from pprint import pprint


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
FORM_CLASS,_ = loadUiType(os.path.join(os.path.dirname("__file__"), "ui/transform.ui"))

class Main(QtWidgets.QMainWindow, FORM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boutons()
        self.gestionDossier()
        self.images = []
        self.indice = 0
        self.taille = 0
        self.total_image.setText(str(self.taille))
        self.image_actuelle.setText(str(self.indice))


    def boutons(self):
        self.image_btn.clicked.connect(self.recupereImages)
        self.suivant_btn.clicked.connect(self.imageSuivante)
        self.precedant_btn.clicked.connect(self.imagePrecedante)
        self.transforme_btn.clicked.connect(self.transformeTexte)


    def gestionDossier(self):
        if os.path.exists(r"c://Marie") == False:
            os.mkdir(r"c://Marie")


    def recupereImages(self):
        image = QtWidgets.QFileDialog.getOpenFileNames(self, "Choisir photo", "c://", "images (*.png *.jpg *.jpeg *.gif)")
        self.images = image[0]
        for i in self.images :
            shutil.copy(i, r"c://Marie")
        self.champ_image.setPixmap(QtGui.QPixmap(self.images[0]))
        self.champ_image.setScaledContents(True)
        self.indice = 0
        self.taille = len(self.images)
        self.total_image.setText(str(self.taille))
        self.image_actuelle.setText(str(self.indice+1))


    def imageSuivante(self):
        if self.indice != self.taille - 1:
            self.champ_image.setPixmap(QtGui.QPixmap(self.images[self.indice + 1]))
            self.champ_image.setScaledContents(True)
            self.indice += 1
        self.image_actuelle.setText(str(self.indice+1))


    def imagePrecedante(self):
        if self.indice != 0:
            self.champ_image.setPixmap(QtGui.QPixmap(self.images[self.indice - 1]))
            self.champ_image.setScaledContents(True)
            self.indice -= 1
        self.image_actuelle.setText(str(self.indice+1))


    def transformeTexte(self):
        img_obj = PIL.Image.open(self.images[self.indice])
        img_text = pytesseract.image_to_string(img_obj)
        print(img_text)
        # with open(f".keep", "w") as f :
        #     f.write(img_text)
        # with open(f".keep", "r") as f:
        #     lire = f.read().splitlines()
        # for i in lire :
        #     if i == "":
        #         lire.remove(i)

        # self.tableWidget.setRowCount(len(lire))
        # self.tableWidget.setColumnCount(len(lire[0]))
        # for i, row_data in enumerate(lire):
        #     for j in range(len(lire)):
        #         item = QtWidgets.QTableWidgetItem(str(row_data))
        #         self.tableWidget.setItem(i,j, item)


                


a = QtWidgets.QApplication(sys.argv)
b = Main()
b.show()
a.exec_()
