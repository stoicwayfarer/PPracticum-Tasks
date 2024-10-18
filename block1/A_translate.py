import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout


class NumSwap(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Перевод')
        self.setGeometry(500, 200, 300, 50)

        self.first_txt_field = QLineEdit()
        self.second_txt_field = QLineEdit()

        self.arrow = QPushButton('->', self)
        self.arrow.clicked.connect(self.pushed)
        # если кнопка стрелки нажата, вызывается метод pushed

        layout = QHBoxLayout() 
        # делает ряд (по умолчанию) виджетов, горизонтально распределяя их по мере добавления
        layout.addWidget(self.first_txt_field)
        layout.addWidget(self.arrow)
        layout.addWidget(self.second_txt_field)

        self.setLayout(layout)

    def pushed(self):
        num1 = self.first_txt_field.text()
        num2 = self.second_txt_field.text()

        self.first_txt_field.setText(num2)
        self.second_txt_field.setText(num1)

        if self.arrow.text() == '<-':
            self.arrow.setText('->')
        else:
            self.arrow.setText('<-')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NumSwap()
    window.show()
    sys.exit(app.exec())