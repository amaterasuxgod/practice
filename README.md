Система управления установками вентиляции Comforta.

Ссылка на документацию:https://web.postman.co/workspace/3f30e5a1-105a-4f36-8d0a-3a73d6bcece4/documentation/13666818-d155912b-8629-4ff8-976f-9297eb49302a

Ссылка на развернутое приложение:https://young-plains-26409.herokuapp.com/

В api реализованы следующие функции:
Модуль пользователей:
- регистрация пользователя
- авторизация пользователя
- удаление пользователя(для админа)
- просмотр списка пользователей(для админа)

Модуль установок:
- создание установки(для админа)
- удаление установки(для админа)
- обновление установки(для админа)
- просмотр списка установок(для админа)
- просмотр текущей установки пользователя
- назначение пользователем установки на свой аккаунт
- обновление текущей для пользователя установки

Модуль логов:
- создание лога
- просмотр логов(для админа-любой установки, для пользователя - только текущей)
- удаление логов(для админа)

Приложение было развернуто на Heroku.

Инструкция по развертыванию приложения:

1. Скачиваем и устанавливаем Heroku CLI
2. Активируем виртуальное окружение, далее выполняем команду pip install django_heroku whitenoise gunicorn dj-database-url

3. Заходим в settings.py, импортируем туда следующие библиотеки:

import os
import django_heroku
import dj_database_url

4. Так же в settings.py переменную Debug меняем на False, для переменной ALLOWED_HOSTS назначаем следующее значение:

ALLOWED_HOSTS = ['localhost', '127.0.0.1','[::1]', 'young-plains-26409.herokuapp.com']

5. Переменную DATABASES можно закомментировать, она примет следующее значение:

DATABASES = {
    'default': dj_database_url.config()
}

6. Так же в settings.py добавляем следующие переменные: 

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

7. Далее, в директории, в которой находится файл manage.py создаем папку с названием static,в этой папке создаем любой файл, для того, что при создании git репозитория он инициализировал данную папку.

8. В директории с файлом manage.py создаем файл Procfile, туда добавляем следующую строку:

web: gunicorn comforta.wsgi --log-file -

9. В той же директории создаем файл runtime.txt, туда записываем следующее:

python-3.9.0

10. Создаем файл requirements.txt, для этого используем команду pip freeze > requirements.txt

11. Открываем новую командную строку(не активируем виртуальное окружение). Заходим в папку с файлом manage.py. Здесь пишем следующие команды:

heroku login(Необходимо быть зарегистрированным на heroku)

heroku create или heroлu create <имя приложения>

После выполнения последней команды вы получите вот такой аутпут https://young-plains-26409.herokuapp.com/ | https://git.heroku.com/young-plains-26409.git

Копируем 2 ссылку

12.Инициализируем в текущей папке git репозиторий, используя команду git init

13. Добавляем изменения с помощью команду git add .

14.Коммитим изменения с помощью комманды git commit -m "asdf"

15. Создаем ссылку на удаленный репозиторий с помощью команды git remote add heroku <ссылка, скопированная ранее>

16. Пушим репозиторий на heroku с помощью команды git push heroku master

17. Создаем в heroku бд с помощью команды:

heroku addons:create heroku-postgresql:hobby-dev

18. Выполняем миграции с помощью команды:

heroku run python manage.py migrate

Поздравляю!Если вы сделали все правильно, то ваше приложение развернуто.










