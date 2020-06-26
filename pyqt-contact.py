from PyQt5.QtWidgets import QAbstractScrollArea, QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QTabWidget, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QToolBar, QAction
from PyQt5.QtGui import QIcon
import sys
from PyQt5 import QtGui


class myApp(QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.mainUI()
        self.mainLayout()
        self.setCentralWidget(self.mainWidget)
        self.menuBars()
        self.setMenuBar(self.menu)
        self.setFixedSize(350, 300)
        self.toolBars()
        self.addToolBar(self.toolBar)

    def mainUI(self):
        self.firstTab = firstTab()
        self.secondTab = secondTab()
        self.thirdTab = thirdTab()
        self.tabs = QTabWidget()
        self.tabs.addTab(self.firstTab, "Contact")
        self.tabs.addTab(self.secondTab, "Favorite")
        self.tabs.addTab(self.thirdTab, "Add Contact")

    def toolBars(self):
        self.toolBar = QToolBar()
        button_toolBar = QAction(QIcon("icon/add.png"), "test", self)
        self.toolBar.addAction(button_toolBar)
        button_toolBar.triggered.connect(self.toolPrint)

    def toolPrint(self):
        print("clicked!")

    def menuBars(self):
        self.menu = self.menuBar()
        test = self.menu.addMenu("About")
        test.addAction("help")
        test.setToolTip("this is help")

    def mainLayout(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabs)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.layout)


class firstTab(QWidget):
    def __init__(self):
        super(firstTab, self).__init__()
        self.mainUI()
        # self.setLayout(self.layout)

    def mainUI(self):
        # self.pButton = QPushButton("first tab button")
        # self.pButton2 = QPushButton("first tab button")
        # self.pButton3 = QPushButton("first tab button")
        # self.pButton4 = QPushButton("first tab button")

        # self.layout = QVBoxLayout()
        # self.layout.addWidget(self.pButton)
        # self.layout.addWidget(self.pButton2)
        # self.layout.addWidget(self.pButton3)
        # self.layout.addWidget(self.pButton4)
        self.listContact()
        self.button = QPushButton("Add To Favorite")
        self.resize(400, 200)

    def setWidget(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.button)

    def listContact(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Name"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Phone No"))

        self.tableWidget.setItem(1, 0, QTableWidgetItem("Parwiz"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("845845845"))
        self.tableWidget.setColumnWidth(1, 200)

        self.tableWidget.setItem(2, 0, QTableWidgetItem("Ahmad"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("2232324"))

        self.tableWidget.setItem(3, 0, QTableWidgetItem("John"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("2236786782324"))

        self.tableWidget.setItem(4, 0, QTableWidgetItem("Doe"))
        self.tableWidget.setItem(4, 1, QTableWidgetItem("12343445"))

        self.button = QPushButton("Add To Favorite")

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.vBoxLayout.addWidget(self.button)
        self.setLayout(self.vBoxLayout)


class secondTab(QWidget):
    def __init__(self):
        super(secondTab, self).__init__()
        self.mainUI()

    def mainUI(self):
        # self.pButton = QPushButton("first tab button")
        # self.pButton2 = QPushButton("first tab button")
        # self.pButton3 = QPushButton("first tab button")
        # self.pButton4 = QPushButton("first tab button")

        # self.layout = QVBoxLayout()
        # self.layout.addWidget(self.pButton)
        # self.layout.addWidget(self.pButton2)
        # self.layout.addWidget(self.pButton3)
        # self.layout.addWidget(self.pButton4)
        self.listContact()
        self.button = QPushButton("Add To Favorite")

    def listContact(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Name"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Phone No"))

        self.tableWidget.setItem(1, 0, QTableWidgetItem("Parwiz"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("845845845"))
        self.tableWidget.setColumnWidth(1, 200)

        self.tableWidget.setItem(2, 0, QTableWidgetItem("Ahmad"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("2232324"))

        self.tableWidget.setItem(3, 0, QTableWidgetItem("John"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("2236786782324"))

        self.tableWidget.setItem(4, 0, QTableWidgetItem("Doe"))
        self.tableWidget.setItem(4, 1, QTableWidgetItem("12343445"))

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)


class thirdTab(QWidget):
    def __init__(self):
        super(thirdTab, self).__init__()


if __name__ == "__main__":
    app = QApplication([])
    window = myApp()
    window.show()
    sys.exit(app.exec_())
