import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QTableWidget, QListWidgetItem
from UI.films_ui import Ui_Form


class Films(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Фильмы")
        self.setFixedSize(868, 653)
        self.conn = sqlite3.connect('Scratches/films.db')
        self.cursor = self.conn.cursor()
        self.show_list_button.clicked.connect(self.show_list)

# для задачи E (фильтрации по жанрам)
        self.load_genres()
        self.load_unfiltered_data()
        self.select_genres_button.clicked.connect(self.filter_by_genres)
        self.tableWidget.setHorizontalHeaderLabels(['Название', 'Год', 'Жанр'])
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

    def load_genres(self):
        self.genres_combobox.addItem("все жанры")
        self.cursor.execute("SELECT title FROM genres")
        genres = self.cursor.fetchall()
        genres_set = set(genre[0] for genre in genres)
        for genre in genres_set:
            self.genres_combobox.addItem(genre)

    def load_unfiltered_data(self):
        self.cursor.execute("""
            SELECT Films.title, Films.year, genres.title AS genre
            FROM Films
            JOIN genres ON Films.genre = genres.id
        """)
        self.update_table_content()

    def filter_by_genres(self):
        selected_genre = self.genres_combobox.currentText()
        if selected_genre == 'все жанры':
            self.load_unfiltered_data()
        else:
            self.cursor.execute("""
                SELECT Films.title, Films.year, genres.title AS genre
                FROM Films
                JOIN genres ON Films.genre = genres.id
                WHERE genres.title = ?
            """, (selected_genre,))
            # JOIN позволяет использовать информацию с обеих таблиц на основании "общего столбца"
            self.update_table_content()

    def update_table_content(self):
        data = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(3)
        for row_number, row_data in enumerate(data):
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

# далее - опции отображения списка для задач A-D
    def show_list(self):
        selected_option = self.select_task_combobox.currentText()
        if selected_option == "A. Новые фильмы":
            self.new_films_list()
        elif selected_option == "B. Знак на конце":
            self.sign_at_the_end_list()
        elif selected_option == "C. Уникальные года":
            self.unique_years_list()
        elif selected_option == "D. Старые детективы":
            self.old_detectives_list()

    def new_films_list(self):
        self.cursor.execute("""
            SELECT title FROM Films
            WHERE (genre = 1 OR genre = 11) AND year < 2000
        """)
        selected_titles = self.cursor.fetchall()
        self.listWidget.clear()
        for title in selected_titles:
            self.listWidget.addItem(QListWidgetItem(title[0]))

    def sign_at_the_end_list(self):
        self.cursor.execute("""
        SELECT title FROM Films
        WHERE title LIKE '%!'
        """)
        selected_titles = self.cursor.fetchall()
        self.listWidget.clear()
        for title in selected_titles:
            self.listWidget.addItem(QListWidgetItem(title[0]))

    def unique_years_list(self):
        self.cursor.execute("""
        SELECT DISTINCT year FROM Films
        WHERE title LIKE 'Х%'
        """)
        unique_years = self.cursor.fetchall()
        self.listWidget.clear()
        for year in unique_years:
            self.listWidget.addItem(QListWidgetItem(str(year[0])))  

    def old_detectives_list(self):
        self.cursor.execute("""
        SELECT title FROM Films
        WHERE genre = 4 AND year BETWEEN 1995 AND 2000
        """)
        selected_titles = self.cursor.fetchall()
        self.listWidget.clear()
        for title in selected_titles:
            self.listWidget.addItem(QListWidgetItem(title[0]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Films()
    window.show()
    sys.exit(app.exec_())