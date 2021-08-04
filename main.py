import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from widget.accueilInterface import Accueil

def main():
    app = QApplication(sys.argv)
    accueil = Accueil()
    accueil.show()
    app.exec_()


if __name__ == '__main__':
    main()