
# Face check

Приложение для поиска информации по фотографии

## Стэк

### Backend

1. Фреймворк: FastAPI
2. БД: Postgresql, SQLAlchemy
3. Аутентификация: JWT

### Frontend

1. VueJS
2. Tailwind

## API

### POST

/user/register - Регистрация пользователя
/user/login - Авторизация пользователя
/image/add - Добавление фотографии человека
/image/search - Поиск по фотографии

### GET

/image/{id} - Возвращает фотографию по её ID
/image/tags/{id} - Возвращает тэги фотографии по её ID


### PATCH

/image Обновление тэгов фотографии


