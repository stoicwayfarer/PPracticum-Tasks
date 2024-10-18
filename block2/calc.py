import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI.calc_ui import Ui_Form


class Calculator(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(421, 587)
        self.setWindowTitle('Калькулятор')
        self.expression = ""
        self.current_number = ""
        self.last_operator = ""
        # использую лямбда функции чтобы не создавать много мелких отдельных функций
        self.button_1.clicked.connect(lambda: self.append_to_expression("1"))
        self.button_2.clicked.connect(lambda: self.append_to_expression("2"))
        self.button_3.clicked.connect(lambda: self.append_to_expression("3"))
        self.button_4.clicked.connect(lambda: self.append_to_expression("4"))
        self.button_5.clicked.connect(lambda: self.append_to_expression("5"))
        self.button_6.clicked.connect(lambda: self.append_to_expression("6"))
        self.button_7.clicked.connect(lambda: self.append_to_expression("7"))
        self.button_8.clicked.connect(lambda: self.append_to_expression("8"))
        self.button_9.clicked.connect(lambda: self.append_to_expression("9"))
        self.button_0.clicked.connect(lambda: self.append_to_expression("0"))
        self.button_plus.clicked.connect(lambda: self.append_operator("+"))
        self.button_minus.clicked.connect(lambda: self.append_operator("-"))
        self.button_mult.clicked.connect(lambda: self.append_operator("*"))
        self.button_divide.clicked.connect(lambda: self.append_operator("/"))
        self.button_dot.clicked.connect(lambda: self.append_to_expression("."))
        self.button_power.clicked.connect(lambda: self.append_operator("**"))
        self.button_sqrt.clicked.connect(self.calculate_sqrt)
        self.button_factorial.clicked.connect(self.calculate_factorial)
        self.button_equals.clicked.connect(self.calculate_result)
        self.button_clear.clicked.connect(self.clear_expression)

    def append_to_expression(self, value):
        self.current_number += value
        self.calc_field.setText(self.current_number)

    def append_operator(self, operator):
        if self.current_number:
            self.expression += self.current_number + operator
            self.current_number = ""
            self.last_operator = operator
        elif self.last_operator:
            self.expression = self.expression[:-len(self.last_operator)] + operator
            self.last_operator = operator

    def calculate_sqrt(self):
        try:
            num = float(self.current_number)
            result = num ** 0.5
            self.current_number = self.format_number(result)
            self.calc_field.setText(self.current_number)
        except ValueError:
            self.calc_field.setText("Error")
            self.current_number = ""

    def calculate_factorial(self):
        try:
            num = int(self.current_number)
            if num < 0:
                raise ValueError
            result = self.factorial(num)
            self.current_number = self.format_number(result)
            self.calc_field.setText(self.current_number)
        except ValueError:
            self.calc_field.setText("Error")
            self.current_number = ""

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    def calculate_result(self):
        try:
            if self.current_number:
                self.expression += self.current_number
                result = eval(self.expression)
                self.current_number = self.format_number(result)
                self.calc_field.setText(self.current_number)
                self.expression = ""
        except Exception:
            self.calc_field.setText("Error")
            self.current_number = ""
            self.expression = ""

    def clear_expression(self):
        self.expression = ""
        self.current_number = ""
        self.last_operator = ""
        self.calc_field.setText("")

    # чтобы не возникало вывода целочисленных с ".0"
    def format_number(self, number):
        # isinstance проверяет является ли объект (число) экземляром класса, типа данных
        if isinstance(number, float) and number.is_integer():
            return str(int(number))
        else:
            return str(number)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())