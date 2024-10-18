from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(621, 633)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 601, 541))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.button_open = QtWidgets.QPushButton(Form)
        self.button_open.setGeometry(QtCore.QRect(10, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_open.setFont(font)
        self.button_open.setObjectName("button_open")
        self.button_save = QtWidgets.QPushButton(Form)
        self.button_save.setGeometry(QtCore.QRect(160, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_save.setFont(font)
        self.button_save.setObjectName("button_save")
        self.button_show = QtWidgets.QPushButton(Form)
        self.button_show.setGeometry(QtCore.QRect(470, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_show.setFont(font)
        self.button_show.setObjectName("button_show")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(370, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Рейтинг"))
        self.button_open.setText(_translate("Form", "Открыть"))
        self.button_save.setText(_translate("Form", "Сохранить"))
        self.button_show.setText(_translate("Form", "Показать"))
        self.comboBox.setItemText(0, _translate("Form", "Все"))