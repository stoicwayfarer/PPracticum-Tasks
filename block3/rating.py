import sys
import csv
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QTableWidgetItem
from UI.rating_ui import Ui_Form


class Rating(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(621, 633)
        self.csv_data = []
        self.button_open.clicked.connect(self.open_csv)
        self.button_save.clicked.connect(self.save_csv)
        self.button_show.clicked.connect(self.filter_data)
        self.comboBox.currentIndexChanged.connect(self.update_filter_text)

    def open_csv(self):
        options = QFileDialog.Options() # опции диал. окна  по умолчанию
        # этот метод возвращает имя выбранного файла и используемый фильтр (прочерк т.к. не используем)
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть CSV", "", "CSV Files (*.csv);;All Files (*)", options=options)
                                                        # заголовок, текущий каталог, фильтр видимых файлов для пользователя
        if file_name:
            with open(file_name, newline='', encoding='utf-8') as csvfile: # открывает файл
                self.csv_data = list(csv.reader(csvfile)) 
                # csv.reader для чтение файла построчно (разделяя по запятым)
                # преобразуем строки файла в список списков (список строк csv)
                self.fill_table(self.csv_data) # функция заполняет таблицу прочтёнными данными
                self.fill_combo_box(self.csv_data) # функция заполняет опции для выбора

    def fill_table(self, data):
        self.tableWidget.setRowCount(0) # очищаем раннее добавленные строки
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setHorizontalHeaderLabels(data[0]) 
        # устанавливаем кол-во столбцов по первой строке (заголовки содержатся в этой строке)
        # перебираем все строки и вставляем сами строки, нумеруя их
        for row_number, row_data in enumerate(data[1:]):
            self.tableWidget.insertRow(row_number)
            # перебираем все элементы в текущей строке и вставляем их
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(data)
                if column_number != len(row_data) - 1: 
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                    # запрет на редактирование ячеек кроме тех, что в последнем столбце
                self.tableWidget.setItem(row_number, column_number, item)
                # заполняем ячейки соотв. значениями
        self.tableWidget.resizeColumnToContents(0)

    # отображает все доступные варианты фильтрации
    def fill_combo_box(self, data):
        self.comboBox.clear()
        self.comboBox.addItem("Все")
        filter_items = set(row[1] for row in data[1:])
        for item in filter_items:
            self.comboBox.addItem(item)

    def update_filter_text(self):
        self.filter_text = self.comboBox.currentText()

    def filter_data(self):
        if self.filter_text == "Все":
            self.fill_table(self.csv_data)
        else:
            filtered_data = [self.csv_data[0]] + [row for row in self.csv_data[1:] if row[1] == self.filter_text]
            self.fill_table(filtered_data)

    def save_csv(self):
        options = QFileDialog.Options() # опции диал. окна  по умолчанию
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить CSV", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if file_name: # если введено имя сохраняемого файла
            with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                # далее просто считываем всё, заполняем таблицу и сохраняем
                for row in range(self.tableWidget.rowCount()):
                    row_data = []
                    for column in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Rating()
    window.show()
    sys.exit(app.exec_())