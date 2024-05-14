# Skymarket

Проект представляет собой backend-часть к готовой frontend-части для сайта объявлений.

Бэкенд-часть проекта предполагает реализацию следующего функционала:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту (не обязательно).
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.

Установка и использование

- Клонируем репозиторий
- Устанавливаем виртуальное окружение
- Устанавливаем библиотеки 'pip install -r requirements.txt'
- Вводим данные в env.sample, переименовать на .env
- Создаем базу данных
- Выполнить миграции
- python manage.py makemigrations
- python manage.py migrate

Инструкция по запуску приложения Dockcer

Развертывание контейнеров с помощью Docker Compose

!!!Предварительно установите Docker!!!

Загрузите проект с репозитория

Из консоли зайдите в директорию проекта

Делаем сборку проекта - docker compose build

Запускаем контейнеры - docker compose up

Запускаем браузер, переходим по ссылке http://127.0.0.1:3000/

Дополнительная документация:
- http://127.0.0.1:8001/api/redoc-tasks/
- http://127.0.0.1:8001/api/swagger/
