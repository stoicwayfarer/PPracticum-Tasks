import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QAbstractItemView, QMenu, QAction
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from UI.task_planner_ui import Ui_Form


class TaskPlannerApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Планировщик задач')
        self.setFixedSize(705, 510)

        self.task_model = QStandardItemModel(self) # таблица для хранения задач
        self.listView.setModel(self.task_model) # связываем listview и таблицу
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers) # чтобы нельзя было редачить список напрямую
        self.listView.setContextMenuPolicy(Qt.CustomContextMenu) 
        self.listView.customContextMenuRequested.connect(self.show_context_menu)

        self.tasks = {} # ключ - дата, значение - список задач на дату
        self.calendarWidget.clicked.connect(self.update_tasks_list)
        self.pushButton.clicked.connect(self.add_task)
        self.lineEdit.setAlignment(Qt.AlignTop | Qt.AlignLeft)

    def update_tasks_list(self):
        selected_date = self.calendarWidget.selectedDate().toString("dd.MM.yyyy")
        self.label.setText(f"Задачи на {selected_date}")
        self.task_model.clear()
        if selected_date in self.tasks:
            for task in self.tasks[selected_date]:
                item = QStandardItem(task)
                self.task_model.appendRow(item) # отображаем каждую задачу как отдельную строку

        self.update_calendar_colors()

    def add_task(self):
        selected_date = self.calendarWidget.selectedDate().toString("dd.MM.yyyy")
        task_time = self.timeEdit.time().toString("hh:mm")
        task_content = self.lineEdit.text().strip()

        if not task_content:
            QMessageBox.warning(self, "Ошибка", "Содержание задачи не может быть пустым.")
            return

        if selected_date not in self.tasks:
            self.tasks[selected_date] = []

        task_entry = f"{task_time} - {task_content}" # отображаемый текст в списке
        self.tasks[selected_date].append(task_entry)
        self.tasks[selected_date].sort(key=lambda x: x.split(' - ')[0])  # сортировка по времени
        self.update_tasks_list()
        self.lineEdit.clear()

    def update_calendar_colors(self):
        default_format = self.calendarWidget.dateTextFormat(QDate.currentDate())
        default_format.setBackground(Qt.transparent)

        for date in self.tasks.keys():
            qdate = QDate.fromString(date, "dd.MM.yyyy")
            if self.tasks[date]:
                format = self.get_highlighted_format()
            else:
                format = default_format
            self.calendarWidget.setDateTextFormat(qdate, format)

    def get_highlighted_format(self):
        format = self.calendarWidget.dateTextFormat(QDate.currentDate())
        format.setBackground(Qt.lightGray)
        return format

    def show_context_menu(self, position):
        indexes = self.listView.selectedIndexes() # возвращает список индексов выбранных элементов
        if indexes:
            menu = QMenu() # контекстное меню
            delete_action = QAction("Удалить", self)
            delete_action.triggered.connect(lambda: self.delete_task(indexes[0]))
            menu.addAction(delete_action)
            menu.exec_(self.listView.viewport().mapToGlobal(position))
            # отображение контекстного меню в глобальной позиции клика, которая преобразована из локальной

    def delete_task(self, index):
        selected_date = self.calendarWidget.selectedDate().toString("dd.MM.yyyy")
        if selected_date in self.tasks:
            task_to_remove = self.task_model.itemFromIndex(index).text()
            if task_to_remove in self.tasks[selected_date]:
                self.tasks[selected_date].remove(task_to_remove)
                self.update_tasks_list()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskPlannerApp()
    window.show()
    sys.exit(app.exec_())