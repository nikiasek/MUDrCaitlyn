import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui


class UI_MainWindow(QMainWindow):
    def __init__(self):
        Main.setObjectName("Main")
        Main.setWindowIcon(QtGui.QIcon("Caitlyn.png"))
        Main.setWindowTitle("Professsor Caitlyn")

        Main.resize(1280,720)


        self.round_label = QtWidgets.QLabel(self.centralwidget)
        self.round_label.setGeometry(60, 20, 100, 22)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.round_label.setFont(font)
        self.round_label.setObjectName("round_label")


if __name__ == "__main___":
    import sys 
    app = QtWidgets.QApplication(sys.argv)
    style = """
        QWidget
        {
            background: #262D37;
        }
    """
    app.useStyleSheet(style)
    Main = QtWidgets.QMainWindow()
    Main.show()
    sys.exit(app.exec_())