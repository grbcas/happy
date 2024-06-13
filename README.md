# Сервис оповещения о дне рождения

## Описание

Этот проект предоставляет API для управления пользователями и их профилями. 
Он позволяет регистрировать пользователей, подтверждать верификационные коды, 
управлять профилями пользователей и активировать пригласительные коды.

## Установка и запуск

1. Клонируйте репозиторий:
   ```
   git clone git@github.com:grbcas/happy_birthday.git
   ```
2. Перейдите в директорию проекта:
   ```
   cd happy_birthday
   ```
3. Создайте файл .env, используя .env.sample:

4. Запустите проект в контейнерах:
   ```
   sudo docker compose up
   ```

## Эндпоинты API

### 1. Создание пользователя и отправка верификационного кода

- **URL:** `/api/registration/`
- **Метод:** `POST`
- **Параметры запроса:**
- `email`
- `password`
- **Успешный ответ:**
- Код: 200 OK
- Тело ответа: JSON объект с данными пользователя.

### 2. Получение профиля пользователя

- **URL:** `/api/user/<pk:int>/`
- **Метод:** `GET`
- **Требуется авторизация.**
- **Успешный ответ:**
- Код: 200 OK
- Тело ответа: JSON объект с данными профиля пользователя.

### 4. Подписаться на другого пользователя

- **URL:** `/api/user/<pk:int>/`
- **Метод:** `PATCH`
- **Требуется авторизация.**
- **Параметры запроса:**
- `friend` (строка, опциональный) - пригласительный код.
- **Успешный ответ:**
- Код: 200 OK
- Тело ответа: JSON объект с сообщением.

### 5. Получение в профиле пользователя cписка пользователей на кооторых он подписан

- **URL:** `/api/user/profile/<pk:int>/`
- **Метод:** `GET`
- **Требуется авторизация.**
- **Успешный ответ:**
- Код: 200 OK
- Тело ответа: JSON объект с данными профиля пользователя.

## Интерфейс на Django Templates

Для удобства тестирования можете перейти по адресу:
```
http://localhost:8000/
```

## Интерфейс на Django admin

Для удобства тестирования можете перейти по адресу:
```
http://localhost:8000/admin/
```
## Документация API

```
**URL:** http://127.0.0.1:8000/swagger/
```