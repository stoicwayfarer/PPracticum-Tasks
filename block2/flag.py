import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup, QPushButton, QLabel
from UI.flag_ui import Ui_Form


class Flag(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(549, 415)
        self.setWindowTitle('Флаг')
        # создание групп кнопок чтобы только одну можно было нажать в группе из 3-х
        self.button_group1 = QButtonGroup(self)
        self.button_group1.addButton(self.button_blue1)
        self.button_group1.addButton(self.button_green1)
        self.button_group1.addButton(self.button_red1)
        self.button_group2 = QButtonGroup(self)
        self.button_group2.addButton(self.button_blue2)
        self.button_group2.addButton(self.button_green2)
        self.button_group2.addButton(self.button_red2)
        self.button_group3 = QButtonGroup(self)
        self.button_group3.addButton(self.button_blue3)
        self.button_group3.addButton(self.button_green3)
        self.button_group3.addButton(self.button_red3)

        self.makeflag_button.clicked.connect(self.makeflag_pushed)

    def makeflag_pushed(self):
        self.output_text = []
        for group in [self.button_group1, self.button_group2, self.button_group3]:
            for button in group.buttons():
                if button.isChecked():
                    self.output_text.append(button.text())
                    break
        self.output()

    def output(self):
        self.and_placement = len(self.output_text) - 1
        if self.and_placement > 0:
            self.output_text.insert(self.and_placement, 'и')
        self.result_label.setText(" ".join(self.output_text))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Flag()
    window.show()
    sys.exit(app.exec_())