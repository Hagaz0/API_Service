# API_Service

Для поднятия сервиса прописать `docker-compose up`

Дождаться полного развертывания БД и запуска приложения:

![img.png](screenshots/img.png)

Запросы посылать по адресу: `localhost:5000`

Реализовано 2 метода (сделано через `POST`, дабы удобнее отправлять данные через JSON):

1. /add - добавляет новый запрос клиента, выдает ID запроса
![img_1.png](screenshots/img_1.png)
2. /get - по ID запроса выдает результат рассчета (параметры + calculated)
![img_2.png](screenshots/img_2.png)

Поля для метода `/add`:

1. kad_num - кадастровый номер в формате АА:ВВ:CCCCСCC:КК
2. latitude - широта
3. longitude - долгота

В случае неверного ввода полей или отсутствия таковых, возвращается `message` с ошибкой
![img_3.png](screenshots/img_3.png)