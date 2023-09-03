# Readme файл для описания и запуска "phone_book"

## Установка:
    1. откройте терминал и перейдите в папку для проекта: cd <название директории в которой будет проект>
    2. скачайте проект с github: git clone https://github.com/sebastianfym/phone_book.git
    3. перейдите в папку проекта: cd phone_book
    (Дальше подразумевается, что у Вас уже установлен Docker и docker-compose)
    4. соберите билд командой: docker-compose build
        -если Вы запускаете с Linux(и т.п.), то может потребовать права доступа.
        -в таком случае: sudo docker-compose build (следом ввести пароль)
    5. поднимите собранный контейнер: docker-compose up
    (Миграции применятся сами)
    6. Вы запустили проект. Можете переходить к тестам!

## Postman приложение:
Специально для тестов я приготовил приложение со всеми запросами в Postman:

https://www.postman.com/aviation-candidate-67374819/workspace/hammer-postman/collection/21641966-80f99a7e-ad58-4f72-86e4-90d2cd4fdbb7?action=share&creator=21641966
    
Перейдите по этой ссылке и Вам будут доступны и расписаны все методы и возможности приложения.
    Так же Вы сможете посмотреть в моках варианты примеров.

    
## Адреса и запросы:
### Авторизация и регистрация:
-http://127.0.0.1:8000/user/auth/registration/ --- регистрация
    
    Тело запроса для регистрации: 
    {
        "email": "bogdan@mail.ru",
        "password": "password",
        "first_name": "Bogdan",
        "last_name": "Velikorodov"
    }
-http://127.0.0.1:8000/user/auth/auth/ --- авторизация

    Тело запроса для авторизации:
    {
    "email": "bogdan@mail.ru",
    "password": "password"
    }

### CRUD операции с контактами
Все последующие запросы необходимо делать от авторизированного пользователя.

Авторизация происходит через JWT и передается в headers.

Если Вы тестируете через Postman, то полученный после авторизации токен скопируйте и вставьте
используя следующий путь: 

Auth -> (Будет надпись "Type" и под ним выпадающий список) Bearer token 
-> в правом окне вставляете свой токен в поле "Token"

Так же вы можете посмотреть всю документацию API по ссылке:
http://127.0.0.1:8000/redoc/

-http://127.0.0.1:8000/phonebook/contact/ --- список всех контактов пользователя

-http://127.0.0.1:8000/phonebook/contact/ --- создание контакта
    
    Тело запроса для создания контакта:
    {
    "first_name": "Игорь",
    "last_name": "Харченко",
    "email": "ighmail.ru",
    "phone": "+330003234"
    }

-http://127.0.0.1:8000/phonebook/contact/1/ --- получение контакта по id

http://127.0.0.1:8000/phonebook/contact/1/ --- изменение конкретного контакта по id

    Тело запроса для обновления контакта:
    любое поле из следующих вариантов:
    {
    "first_name": "Игорь",
    "last_name": "Харченко",
    "email": "ighmail.ru",
    "phone": "+330003234"
    }

-http://127.0.0.1:8000/phonebook/contact/1/ --- удаление контакта по id


## Пагинация, поиск и стек технологий:
Пагинация настроена на 10 объектов на странице.

Поиск происходит после добавление параметра search=<значение> в строку запроса.

Пример: http://127.0.0.1:8000/phonebook/contact/?search=Кири. Тут бы нам поиск выдал контакт, который содержит "Кири".

Поиск настроен по всем полям контакта

Инструменты: 
    
    -Django
    -Drf 
    -Postgres
    -drf-yasg (документация API)
    -Docker
    -docker-compose
    -djangorestframework-simplejwt
    -Markdown (оформление Readme)

Приятного использования.

