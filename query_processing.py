# импортируем модуль в котором описаны таблицы базы данных
import description_tables as descr_tab
# импортируем библиотеку sqlalchemy и некоторые функции из нее
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def connect_db(DB_PATH, Base):
    """
        Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
    Base.metadata.create_all(bind=engine)
    # создаем фабрику сессию
    session = sessionmaker(bind=engine)
    # возвращаем сессию
    return session()


def find_artist(tab, artist):
    """
        Находит все альбомы в базе данных по заданному имяни исполнителя или название группы.
        artist - имя исполнителя или название группы, которых надо наити.
        tab - таблица в которой проходит поиск
    """
    # session - соединение к базе данных
    session = connect_db(DB_PATH=descr_tab.DB_PATH, Base=descr_tab.Base)
    # обработка запроса к базе данных по имя исполнителя или названию группы
    albums = session.query(tab).filter(tab.artist == artist).all()
    return albums


def find_album_artist(tab, album, artist):
    """
        Находит запись в базе данных по заданному названию альбома и исполнителя
        (название группы).
        album - названание альбома, которого надо наити.
        artist - имя исполнителя или название группы, которых надо наити.
        tab - таблица в которой проходит поиск
    """
    # session - соединение к базе данных
    session = connect_db(DB_PATH=descr_tab.DB_PATH, Base=descr_tab.Base)
    # обработка запроса к базе данных по имя исполнителя или названию группы
    artist = session.query(tab).filter(tab.album == album, tab.artist == artist).first()
    return artist

def write_tables(tab, table_item):
    """
        Производит запись в базу даных.
        tab - таблица в которою производится запись
        table_item - данные которые надо записить
    """
    #проверка аргумента table_item["year"], на то что она состойт из чисел.
    for year_char in table_item["year"]:
        if year_char not in "0123456789":
            raise tab.AlbumYearInt("Год задан некоректно.")

    #assert isinstance(int(table_item["year"]), int), "Incorrect artist"
    assert isinstance(table_item["artist"], str), "Incorrect artist"
    assert isinstance(table_item["genre"], str), "Incorrect genre"
    assert isinstance(table_item["album"], str), "Incorrect album"

    album_artist_list = find_album_artist(tab, table_item["album"], table_item["artist"])

    #Просерка в базе данныз на наличеё уже существуюшего альбома и исролнителя
    if album_artist_list is not None:
        album_str = table_item["album"]
        raise tab.AlbumExists(
            f"Искомый Альбом \'{album_str}\' c id{album_artist_list.id} уже сущёствует в базе данных. Поэтому запись в базу данных была прервана.")

    #Потготовка записи и сама запись в таблицу
    album_tb = descr_tab.Albums(
        year=int(table_item["year"]),
        artist=table_item["artist"],
        genre=table_item["genre"],
        album=table_item["album"],
        )

    session = connect_db(DB_PATH=descr_tab.DB_PATH, Base=descr_tab.Base)
    session.add(album_tb)
    session.commit()
