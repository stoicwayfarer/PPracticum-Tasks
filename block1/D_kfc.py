import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QCheckBox, QPushButton, QMessageBox
from UI.kfc_ui import Ui_Form

class KFC(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
        self.items = {
            "Чизбургер": {"checkbox": self.checkBox, "quantity": self.lineEdit, "price": 99},
            "Гамбургер": {"checkbox": self.checkBox_2, "quantity": self.lineEdit_2, "price": 119},
            "Кока-кола": {"checkbox": self.checkBox_3, "quantity": self.lineEdit_3, "price": 129},
            "Наггетсы": {"checkbox": self.checkBox_4, "quantity": self.lineEdit_4, "price": 49}
        }

        self.setWindowTitle('Чек из KFC')
        self.setFixedSize(280, 349)
        self.order_button.clicked.connect(self.generate_check)

    def generate_check(self):
        check_text = "Ваш заказ:\n"
        total_price = 0

        for item, details in self.items.items():
            if details["checkbox"].isChecked():
                try:
                    quantity = int(details["quantity"].text())
                    if quantity < 0:
                        raise ValueError("Количество не может быть отрицательным")
                    item_price = details["price"] * quantity
                    check_text += f"{item}----{quantity}----{item_price} рублей\n"
                    total_price += item_price
                except:
                    self.show_error_message()
                    return

        check_text += f"\nОбщая стоимость: {total_price} рублей"
        self.order_check.setText(check_text)

    def show_error_message(self):
        msg = QMessageBox()
        msg.setText("Ошибка ввода")
        msg.setWindowTitle("Ошибка ввода")
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KFC()
    window.show()
    sys.exit(app.exec())
