# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(411, 417)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 380, 401, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.delete_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.accept_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.accept_button.setObjectName("accept_button")
        self.horizontalLayout.addWidget(self.accept_button)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(3, 3, 401, 371))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.sort_name = QtWidgets.QLineEdit(self.widget)
        self.sort_name.setObjectName("sort_name")
        self.gridLayout.addWidget(self.sort_name, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.roast_rate = QtWidgets.QSpinBox(self.widget)
        self.roast_rate.setMinimum(1)
        self.roast_rate.setMaximum(5)
        self.roast_rate.setObjectName("roast_rate")
        self.gridLayout.addWidget(self.roast_rate, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.grains_type = QtWidgets.QComboBox(self.widget)
        self.grains_type.setObjectName("grains_type")
        self.grains_type.addItem("")
        self.grains_type.addItem("")
        self.gridLayout.addWidget(self.grains_type, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.description = QtWidgets.QTextEdit(self.widget)
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.cost = QtWidgets.QSpinBox(self.widget)
        self.cost.setMinimum(1)
        self.cost.setMaximum(100000)
        self.cost.setDisplayIntegerBase(10)
        self.cost.setObjectName("cost")
        self.gridLayout.addWidget(self.cost, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.volume = QtWidgets.QSpinBox(self.widget)
        self.volume.setMinimum(1)
        self.volume.setMaximum(100000)
        self.volume.setDisplayIntegerBase(10)
        self.volume.setObjectName("volume")
        self.gridLayout.addWidget(self.volume, 5, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cancel_button.setText(_translate("Form", "Отменить"))
        self.delete_button.setText(_translate("Form", "Удалить"))
        self.accept_button.setText(_translate("Form", "Принять"))
        self.label.setText(_translate("Form", "Название сорта"))
        self.label_2.setText(_translate("Form", "Степень обжарки"))
        self.label_3.setText(_translate("Form", "Тип зёрен"))
        self.grains_type.setItemText(0, _translate("Form", "Молотый"))
        self.grains_type.setItemText(1, _translate("Form", "В зёрнах"))
        self.label_4.setText(_translate("Form", "Описание вкуса"))
        self.label_5.setText(_translate("Form", "Цена"))
        self.label_6.setText(_translate("Form", "Объем упаковки"))
