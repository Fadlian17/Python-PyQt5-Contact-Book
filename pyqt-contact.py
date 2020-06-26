from PyQt5.QtWidgets import QMessageBox, QLabel, QLineEdit, QAbstractScrollArea, QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QTabWidget, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QToolBar, QAction
from PyQt5.QtGui import QIcon
import sys
from PyQt5 import QtGui
import json

datac = open('data_contact.json')
dataco = json.load(datac)


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
        button_tools = QAction(QIcon("icon/contact.png"), "Help", self)
        self.toolBar.addAction(button_tools)
        button_tools.triggered.connect(self.popupHelp)

    def popupHelp(self):
        msg_pop = "PyQT Contact Help Center!"
        QMessageBox.information(self, "Help Center", msg_pop)

    def menuBars(self):
        self.menu = self.menuBar()
        test = self.menu.addMenu("File")
        test2 = self.menu.addMenu("App")
        test.addAction("Tentang Aplikasi")

    def mainLayout(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabs)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.layout)


# Show Data Contact
class firstTab(QWidget):
    def __init__(self):
        super(firstTab, self).__init__()
        self.open = open("data_contact.json", "r")
        self.userContact = json.loads(self.open.read())
        self.mainUI()
        self.setLayout(self.layout)
        # self.setLayout(self.layout)

    def mainUI(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.userContact))
        self.tableWidget.setColumnCount(2)
        for row in range(len(self.userContact)):
            for col in range(2):
                if col == 0:
                    self.tableWidget.setItem(
                        row, col, QTableWidgetItem(self.userContact[row]["nama"]))
                else:
                    self.tableWidget.setItem(row, col, QTableWidgetItem(
                        self.userContact[row]["nomor_hp"]))
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Phone Number"])
        self.tableWidget.cellClicked.connect(self.addFavoriteContact)

        self.button = QPushButton("Add To Favorite")
        self.button.clicked.connect(self.addFavoriteContact)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.button)

    def addFavoriteContact(self):
        pass


# Add to Favorite Contact List
class secondTab(QWidget):
    def __init__(self):
        super(secondTab, self).__init__()
        self.mainUI()

    def mainUI(self):
        self.favoriteData()

    def favoriteData(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents)
        favorites = list(filter(lambda x: x["favorite"] == 1, dataco))
        self.tableWidget.setRowCount(len(dataco))
        self.tableWidget.setColumnCount(2)

        if favorites:
            for row in range(len(favorites)):
                for col in range(2):
                    if col == 0:
                        self.tableWidget.setItem(
                            row, col, QTableWidgetItem(favorites[row]['nama']))
                    else:
                        self.tableWidget.setItem(
                            row, col, QTableWidgetItem(favorites[row]['nomor_hp']))
        else:
            pass
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Phone Number"])

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)

# Add New Contact


class thirdTab(QWidget):
    def __init__(self):
        super(thirdTab, self).__init__()
        self.mainUI()

    def mainUI(self):
        self.addContact()

    def addContact(self):
        self.name = QLabel(self)
        self.name.setText('Name:')
        self.contact = QLabel(self)
        self.contact.setText('Contact:')
        self.line = QLineEdit(self)
        self.buttonAdd = QPushButton("Add To Contact")

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.name)
        self.vBoxLayout.addWidget(self.line)
        self.vBoxLayout.addWidget(self.contact)
        self.vBoxLayout.addWidget(self.buttonAdd)


if __name__ == "__main__":
    app = QApplication([])
    window = myApp()
    window.setWindowTitle("PyQt5 Contact")
    window.show()
    sys.exit(app.exec_())
