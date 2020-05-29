# * sqlite3 albums.sqlite3
# * .schema
# * SELECT * FROM album;

# импортируем модуль в котором описаны таблицы базы данных
import description_tables as descr_tab
# импортируем модуль в котором происходит обработка запросоа к базе данных
import query_processing
# импортируем модуль в котором происходит обработка запросоа к базе данных
import query_visualization as qv
# импортируем библиотеку bottle и некоторые функции из нее
from bottle import run



def main():
    run(host="localhost", port=8080, debug=True)
    """
        Пример запроса для чтения из базы данных и вывотом результата в бреузер
        http://localhost:8080/albums/Beatles
    """
    """
        Пример запроса для записи в базу данных с ваводом результатов в консоль.
        http -f POST http://localhost:8080/albums artist="New Artist" genre="Rock" album="Super" year=1970
    """

if __name__ == "__main__":
    main()
