import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui

class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.iconsize = QSize(64, 64)
        self.resize(1280,720)
        self.setWindowTitle("Professor Caitlyn")
        self.setWindowIcon(QtGui.QIcon("C:\\Users\\nikia\\Documents\\Codes\\Python\\Professor Caitlyn\\Caitlyn.ico"))
        # === Main Window Gui === #

        self.table_widget = tabs(self)
        self.setCentralWidget(self.table_widget)
        style = """
        QVBoxLayout#maintab {
            background: #2b2e2b;
        }      
        """

        self.show()

class tabs(QWidget):   
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        # === Tabs Window Gui === #

        self.tabs = QTabWidget()
        self.maintab = QWidget()
        self.championstab = QWidget()
        self.runetab = QWidget()

        # === Add tabs === #

        self.tabs.addTab(self.maintab, "Main")
        self.tabs.addTab(self.championstab, "Champions")
        self.tabs.addTab(self.runetab, "Runes")


        # === Champions tab === #

        self.maintab.layout = QVBoxLayout(self)



        # === Add tabs to main window === #



def smain():
    app = QApplication(sys.argv)
    style = """
        QVBoxLayout#maintab {
            background: #2b2e2b;
        }      
        """
    app.setStyleSheet(style)
    ex = main()
    ex.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
   smain()