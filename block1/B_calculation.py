import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout


class Calculation(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Вычисление выражений')
        self.setGeometry(500, 200, 300, 50)

        self.expression_txt_field = QLineEdit()
        self.expression_txt_field.setFixedSize(120, 30)
        self.result_txt_field = QLineEdit()
        self.result_txt_field.setFixedSize(120, 30)

        self.calculate_btn = QPushButton('->', self)
        self.calculate_btn.setFixedSize(40, 20)
        self.calculate_btn.clicked.connect(self.calculate)

        layout = QHBoxLayout()
        layout.addWidget(self.expression_txt_field)
        layout.addWidget(self.calculate_btn)
        layout.addWidget(self.result_txt_field)

        self.setLayout(layout)

    def calculate(self):
        expression = self.expression_txt_field.text()
        try:
            result = eval(expression)
            self.result_txt_field.setText(str(result))
        except:
            self.result_txt_field.setText('Ошибка ввода')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculation()
    window.show()
    sys.exit(app.exec())