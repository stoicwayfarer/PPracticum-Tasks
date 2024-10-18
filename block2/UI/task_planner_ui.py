from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(705, 510)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(390, 50, 301, 441))
        self.listView.setObjectName("listView")
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(30, 460, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.timeEdit.setFont(font)
        self.timeEdit.setObjectName("timeEdit")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 20, 351, 241))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(390, 20, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 460, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 270, 351, 181))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Выберите день для просмотра задач"))
        self.pushButton.setText(_translate("Form", "Создать задачу"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Введите содержание задачи..."))
