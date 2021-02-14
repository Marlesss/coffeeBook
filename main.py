import sys
import sqlite3
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem


class AddEditCoffeeForm(QWidget):
    def __init__(self, unit_id=None, unit_row=None, parent=None):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.parent = parent
        self.unit_id = unit_id
        self.unit_row = unit_row
        self.setWindowTitle("Редактор записей")
        self.accept_button.clicked.connect(self.accept_changes)
        self.cancel_button.clicked.connect(self.cancel_changes)
        self.delete_button.clicked.connect(self.delete)
        if self.unit_id:
            self.load_data()

    def load_data(self):
        values = dict()
        for j, header in enumerate(self.parent.headers):
            values[header] = self.parent.tableWidget.item(self.unit_row, j).text()
        self.sort_name.setText(values["Название сорта"])
        self.roast_rate.setValue(int(values["Степень обжарки"]))
        self.grains_type.setCurrentText(values["Тип зёрен"])
        self.description.setText(values["Описание вкуса"])
        self.cost.setValue(int(values["Цена"]))
        self.volume.setValue(int(values["Объем упаковки"]))

    def accept_changes(self):
        data = list()
        data.append(self.sort_name.text())
        data.append(self.roast_rate.value())
        data.append(self.grains_type.currentText())
        data.append(self.description.toPlainText())
        data.append(self.cost.value())
        data.append(self.volume.value())
        if self.unit_id:
            self.parent.delete_unit(self.unit_id)
            # self.parent.con.commit()
            data.insert(0, self.unit_id)
        data = list(map(str, data))
        data = list(map(lambda elem: f'"{elem}"', data))
        request = f"""INSERT 
INTO coffee({', '.join(list(map(lambda elem: f'"{elem}"',
                                self.parent.headers[(0 if self.unit_id else 1):])))}) 
VALUES ({', '.join(data)})"""
        cur = self.parent.con.cursor()
        cur.execute(request)
        self.close()

    def cancel_changes(self):
        self.close()

    def delete(self):
        if self.unit_id:
            self.parent.delete_unit(self.unit_id)
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.parent.con.commit()
        self.parent.init_data_base()
        self.parent.show()
        super().closeEvent(a0)


class Main(QMainWindow):
    def __init__(self):
        self.con = sqlite3.connect("coffee.sqlite")
        self.child = None
        self.headers = None
        super().__init__()
        # self.setupUi(self)
        uic.loadUi("main.ui", self)
        self.initUI()
        self.init_data_base()

    def initUI(self):
        self.setWindowTitle("CoffeeBook")
        self.add_action.triggered.connect(self.add_unit)
        self.tableWidget.cellDoubleClicked.connect(self.change_unit)

    def init_data_base(self):
        cur = self.con.cursor()
        result = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.headers = [x for x, *_ in cur.description]
        self.tableWidget.setColumnCount(len(self.headers))
        self.tableWidget.setHorizontalHeaderLabels(self.headers)
        self.tableWidget.setRowCount(len(result))
        for i, row in enumerate(result):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def add_unit(self):
        self.hide()
        self.child = AddEditCoffeeForm(parent=self)
        self.child.show()

    def change_unit(self, row):
        unit_id = self.tableWidget.item(row, 0).text()
        self.hide()
        self.child = AddEditCoffeeForm(unit_id=unit_id, unit_row=row, parent=self)
        self.child.show()

    def delete_unit(self, unit_id):
        cur = self.con.cursor()
        cur.execute(f"""DELETE FROM coffee WHERE ID={unit_id}""")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
