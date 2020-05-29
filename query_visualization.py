# импортируем модуль в котором описаны таблицы базы данных
import description_tables as descr_tab
# импортируем модуль в котором происходит обработка запросоа к базе данных
import query_processing
# импортируем библиотеку bottle и некоторые функции из нее
from bottle import route
from bottle import HTTPError
from bottle import request


@route("/albums/<artist>")
def albums(artist="Beatles"):
    """
        Пример запроса для чтения из базы данных и вывотом результата в бреузер
        http://localhost:8080/albums/Beatles
    """
    albums_list = query_processing.find_artist(descr_tab.Albums, artist)
    if not albums_list:
        message = f"Альбомов {artist} не найдено"
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        result = f"Список альбомов {artist}<br>"
        result += "<br>".join(album_names)
        result += f"<br>Количества альбомов {len(albums_list)}"
    return result


@route("/albums", method="POST")
def albums():
    """
        Пример запроса для записи в базу данных с ваводом результатов в консоль.
        http -f POST http://localhost:8080/albums artist="New Artist" genre="Rock" album="Super" year=1970

        artist - имя исполнителя или название группы
        genre - жанр альбома
        album - название альбома
        year - год выхода альбома
    """

    album_dict ={
        "year": request.forms.get("year"),
        "artist": request.forms.get("artist"),
        "genre": request.forms.get("genre"),
        "album": request.forms.get("album"),
    }

    try:
        result = query_processing.write_tables(descr_tab.Albums, album_dict)
    except AssertionError as err:
        print(err)
        result = HTTPError(400, str(err))
    except descr_tab.Albums.AlbumYearInt as err:
        print(err)
        result = HTTPError(400, str(err))
    except descr_tab.Albums.AlbumExists as err:
        print(err)
        result = HTTPError(409, err.args[0])
    else:
        print("Данные сохранены")

    return result
