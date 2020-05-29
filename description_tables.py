# * sqlite3 albums.sqlite3
# * .schema
# * SELECT * FROM album;
# импортируем библиотеку sqlalchemy и некоторые функции из нее
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

# константа, указывающая способ соединения  с базой данных
DB_PATH = "sqlite:///albums.sqlite3"

# базовый класс моделей таблиц
Base = declarative_base()

class Albums(Base):
    """
        Описывает структуру таблицы album для хранения записей музыкальной библиотеки

        album
        (
            "id" integer primary key autoincrement, - идентификатор альбома, первичный ключ
            "year" integer, - год выхода альбома
            "artist" text, - имя исполнителя или название группы
            "genre" text, - жанр альбома
            "album" text - название альбома
        )
    """
    # задаем название таблицы
    __tablename__ = "album"

    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)

    class AlbumExists(Exception):
        """
            Используется для идентификации одинаковых записей в базу данных
        """
        pass

    class AlbumYearInt(Exception):
        """
            Используется для идентификации правельнои записи даты
        """
        pass
