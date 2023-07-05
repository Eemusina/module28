# module28
Тестирование авторизации в ЛК "Ростелеком" https://b2c.passport.rt.ru/
Реализованы тесты к "Стандартная авторизация по логину и паролю"
Тест-кейсы доступны по ссылке https://docs.google.com/spreadsheets/d/1x-8ovnGvhLhEii6Kn1uBxqcIdRWcyrJGu_qdksWonzU/edit?usp=sharing
При создании тест-кейсов использованы техники позитивного тестирования для проверки авторизации на сайте различными способами. 
Для запуска нужно выполнить в корне проекта команду python pytest -v --driver Chrome --driver-path ~/chrome tests.py
* ~/chrome в данном примере —  загруженный и разархивированный файл Selenium WebDriver
