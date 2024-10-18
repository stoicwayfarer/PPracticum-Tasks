from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(868, 653)
        self.genres_combobox = QtWidgets.QComboBox(Form)
        self.genres_combobox.setGeometry(QtCore.QRect(10, 20, 151, 31))
        self.genres_combobox.setObjectName("genres_combobox")
        self.select_genres_button = QtWidgets.QPushButton(Form)
        self.select_genres_button.setGeometry(QtCore.QRect(170, 20, 151, 31))
        self.select_genres_button.setObjectName("select_genres_button")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 65, 511, 581))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.show_list_button = QtWidgets.QPushButton(Form)
        self.show_list_button.setGeometry(QtCore.QRect(710, 20, 151, 31))
        self.show_list_button.setObjectName("show_list_button")
        self.select_task_combobox = QtWidgets.QComboBox(Form)
        self.select_task_combobox.setGeometry(QtCore.QRect(550, 20, 151, 31))
        self.select_task_combobox.setObjectName("select_task_combobox")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(519, 70, 41, 571))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(550, 70, 311, 571))
        self.listWidget.setObjectName("listWidget")

        self.select_task_combobox.addItem("A. Новые фильмы")
        self.select_task_combobox.addItem("B. Знак на конце")
        self.select_task_combobox.addItem("C. Уникальные года")
        self.select_task_combobox.addItem("D. Старые детективы")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.select_genres_button.setText(_translate("Form", "Выбрать"))
        self.show_list_button.setText(_translate("Form", "Отобразить список"))
