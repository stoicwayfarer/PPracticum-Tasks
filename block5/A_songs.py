"""
"Тройная связь данных"
Artist.Name -> Artist.ArtistId 
-> Album.ArtistId -> Album.AlbumId
-> Track.AlbumId -> Track.Name
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtSql
from UI.songs_ui import Ui_Form


class Music(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('block5/music.sqlite')
        if not self.db.open(): return

        self.query = QtSql.QSqlQuery()
        self.query.exec_("SELECT Name FROM Artist")
        while self.query.next(): # пока есть следующая запись в столбце, т.е. перебор всех исполнителей
            artist_name = self.query.value(0) # name - это столбец с индексом 0
            self.comboBox.addItem(artist_name)

        self.comboBox.currentIndexChanged.connect(self.display_tracks)

    def display_tracks(self):
        artist_name = self.comboBox.currentText()
        self.query.exec_(f"""
            SELECT DISTINCT Track.Name
            FROM Artist
            JOIN Album ON Artist.ArtistId = Album.ArtistId
            JOIN Track ON Album.AlbumId = Track.AlbumId
            WHERE Artist.Name = '{artist_name}'
            ORDER BY Track.Name
        """)
        self.listWidget.clear()
        while self.query.next(): # перебор всех треков в столбце
            track_name = self.query.value(0)
            self.listWidget.addItem(track_name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Music()
    window.show()
    sys.exit(app.exec_())