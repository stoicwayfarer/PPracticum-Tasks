import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton

alphabet = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 
            'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
            'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 
            'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 
            'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
            'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 
            'y': '-.--', 'z': '--..'}


class Morze(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(570, 77)
        self.setWindowTitle('Морзе')
        step = 0
        self.txt_field = QLineEdit(self)
        self.txt_field.move(24, 32)
        self.txt_field.resize(520, 22)

        for i, added_txt in alphabet.items():
            self.btn = QPushButton(self)
            self.btn.setText(i)
            self.btn.resize(19, 19)
            self.btn.move(step, 0)
            step += 22
            self.btn.clicked.connect(self.convert)

    def convert(self):
        added_txt = alphabet.get(self.sender().text())
        # sender() возвращает обьект, который вызвал сигнал
        current_txt = self.txt_field.text()
        self.txt_field.setText(f"{current_txt}{added_txt}")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Morze()
    window.show()
    sys.exit(app.exec())