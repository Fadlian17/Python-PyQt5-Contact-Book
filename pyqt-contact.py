from PyQt5.QtWidgets import QMessageBox, QLabel, QLineEdit, QAbstractScrollArea, QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QTabWidget, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QToolBar, QAction
from PyQt5.QtCore import QtMsgType, QtDebugMsg
from PyQt5.QtGui import QIcon
import sys
import json
import os


class myApp(QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.open = open("data_contact.json", "r")
        self.userContact = json.loads(self.open.read())
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
        self.toolBar2 = QToolBar()
        button_tools = QAction(QIcon("icon/contact.png"), "Help", self)
        self.toolBar.addAction(button_tools)
        button_tools.triggered.connect(self.popupHelp)
        self.toolBar2.addAction(button_tools)
        button_tools.triggered.connect(self.popupHelp)

    def popupHelp(self):
        msg_pop = "PyQT Contact Help Center!"
        QMessageBox.information(self, "Help Center", msg_pop)

    def menuBars(self):
        self.menu = self.menuBar()
        test = self.menu.addMenu("File")
        test2 = self.menu.addMenu("App")
        test.addAction("Tentang Aplikasi")
        test2.addAction("Contact Book List")

    def mainLayout(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabs)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.layout)


# Show Data Contact
class firstTab(QWidget):
    def __init__(self):
        super(firstTab, self).__init__()
        self.dataFavorite = {}
        self.open = open("data_contact.json", "r")
        self.userContact = json.loads(self.open.read())
        self.FavoriteTable()
        self.mainUI()
        self.setLayout(self.layout)

    def mainUI(self):
        self.btnAddFavorite = QPushButton("Add to favorite")
        self.btnAddFavorite.clicked.connect(self.addToFavorite)
        # set widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tablePlaces)
        self.layout.addWidget(self.btnAddFavorite)

    def addToFavorite(self):
        for i in self.userContact:
            if self.dataFavorite['nama'] == i['nama']:
                i['favorite'] = 1
        toJson = json.dumps(self.userContact, indent=4)
        fwrite = open('data_contact.json', 'w')
        fwrite.write(toJson)

    def fetchFavorite(self, row, column):
        favoriteData = []
        rwf = row
        clf = column
        for x in range(len(self.head)):
            res = self.tablePlaces.item(int(rwf), int(x)).text()
            favoriteData.append(res)
        for i in self.userContact:
            if favoriteData[0] == i['nama']:
                self.dataFavorite.update(i)

    # Logic to SecondTabs
    def FavoriteTable(self):
        self.head = ["name", "phone number"]
        row = len(list(self.userContact))
        self.tablePlaces = QTableWidget()
        self.tablePlaces.setRowCount(row)
        self.tablePlaces.setColumnCount(len(self.head))
        for row in range(len(self.userContact)):
            for col in range(len(self.head)):
                if col == 0:
                    self.tablePlaces.setItem(
                        row, col, QTableWidgetItem(self.userContact[row]["nama"]))
                elif col == 1:
                    self.tablePlaces.setItem(row, col, QTableWidgetItem(
                        self.userContact[row]["nomor_hp"]))

        self.tablePlaces.setHorizontalHeaderLabels(self.head)

        self.tablePlaces.cellClicked.connect(self.fetchFavorite)


# Add to Favorite Contact List
class secondTab(QWidget):
    def __init__(self):
        super(secondTab, self).__init__()
        self.open = open("data_contact.json", "r")
        self.userContact = json.loads(self.open.read())
        self.dataFavorite = {}
        self.createTable()
        self.mainUI()
        self.setLayout(self.layout)

    def mainUI(self):
        self.btnDeleteFavorite = QPushButton("Delete favorite Contact")
        self.btnDeleteFavorite.clicked.connect(self.deleteFromfavorite)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableFavs)
        self.layout.addWidget(self.btnDeleteFavorite)

    def createTable(self):
        self.head = ["name", "phone number"]
        self.contactFav = list(
            filter(lambda a: a["favorite"] == 1, self.userContact))
        row = len(self.contactFav)
        self.tableFavs = QTableWidget()
        self.tableFavs.setRowCount(row)
        self.tableFavs.setColumnCount(len(self.head))
        for row in range(len(self.contactFav)):
            for col in range(len(self.head)):
                if col == 0:
                    self.tableFavs.setItem(row, col, QTableWidgetItem(
                        self.contactFav[row]["nama"]))
                elif col == 1:
                    self.tableFavs.setItem(row, col, QTableWidgetItem(
                        self.contactFav[row]["nomor_hp"]))

        self.tableFavs.setHorizontalHeaderLabels(self.head)
        self.tableFavs.cellClicked.connect(self.fetchFavorite)

    def fetchFavorite(self, row, column):
        favoriteData = []
        rw = row
        cl = column
        for x in range(len(self.head)):
            res = self.tableFavs.item(int(rw), int(x)).text()
            favoriteData.append(res)
        for i in self.userContact:
            if favoriteData[0] == i['nama']:
                self.dataFavorite.update(i)

    def deleteFromfavorite(self):
        for i in self.userContact:
            if self.dataFavorite['nama'] == i['nama']:
                i['favorite'] = 0
        toJson = json.dumps(self.userContact, indent=4)
        fwrite = open('data_contact.json', 'w')
        fwrite.write(toJson)

# Add New Contact to Contact List


class thirdTab(QWidget):
    def __init__(self):
        super(thirdTab, self).__init__()
        self.mainUI()
        self.setLayout(self.layout)
        self.open = open("data_contact.json", "r")
        self.userContact = json.loads(self.open.read())

    def mainUI(self):
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Type Name")
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setPlaceholderText("Type Phone Number")
        self.buttonAdd = QPushButton("Add To Contact")
        self.buttonAdd.clicked.connect(self.addContact)
        self.lineEdit.returnPressed.connect(self.addContact)
        self.lineEdit2.returnPressed.connect(self.addContact)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.lineEdit2)
        self.layout.addWidget(self.buttonAdd)

    # logic

    def addContact(self):
        name = self.lineEdit.text()
        phone = self.lineEdit2.text()
        params = {"nama": name, "nomor_hp": phone, "favorite": 0}
        self.userContact.append(params)
        toJson = json.dumps(self.userContact, indent=4)
        fwrite = open('data_contact.json', 'w')
        fwrite.write(toJson)


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


if __name__ == "__main__":
    app = QApplication([])
    window = myApp()
    window.setWindowTitle("PyQt5 Contact")
    window.show()
    sys.exit(app.exec_())
