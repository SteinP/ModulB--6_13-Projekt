"# ModulB--6_13-Projekt"

фаил запуска B6_13main.py

В этом модуле мы уделили большое внимание особенностям разработки веб-сервисов, поэтому задание будет посвящено разработке веб-приложения для ведения базы музыкальных альбомов. Вы можете переиспользовать код, приведенный в этом модуле, в своем решении, если он покажется вам подходящим. Итак, сформулируем требования к приложению:
В этом модуле мы разработаем в веб-приложении, для ведения базы музыкальных альбомов.
Итак, требования к приложению:

    Веб-сервер принимает GET-запросы по адресу /albums/<artist> и выводит на экран сообщение с количеством альбомов исполнителя artist и списком названий этих альбомов. Пример запроса http://localhost:8080/albums/Beatles.
    Веб-сервер принимает POST-запросы по адресу /albums/ и сохраняет переданные пользователем данные об альбоме.
    Данные передаются в формате веб-формы. Если пользователь пытается передать данные об альбоме, который уже есть в
    базе данных, обработчик запроса отвечает HTTP-ошибкой 409 и выводит соответствующее сообщение.
    Пример запроса http -f POST http://localhost:8080/albums artist="New Artist" genre="Rock" album="Super" year=1970.

В качестве исходной базы данных использовать файл albums.sqlite3.
