import sys
import sqlite3
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Main(QMainWindow):
    def __init__(self):
        self.con = sqlite3.connect("coffee.sqlite")
        super().__init__()
        # self.setupUi(self)
        uic.loadUi("main.ui", self)
        self.initUI()
        self.init_data_base()

    def initUI(self):
        self.setWindowTitle("CoffeeBook")

    def init_data_base(self):
        cur = self.con.cursor()
        result = cur.execute("""SELECT * FROM coffee""").fetchall()
        header = [x for x, *_ in cur.description]
        self.tableWidget.setColumnCount(len(header))
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.setRowCount(len(result))
        for i, row in enumerate(result):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
