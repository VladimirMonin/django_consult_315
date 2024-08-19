# Проект Python Telegram Bot с бэкэндом на Django
## Описание проекта
Этот проект представляет собой веб-сайт с визиткой и формой записи на консультацию, разработанный с использованием `Django` и библиотеки `Python Telegram Bot`.

Веб-сайт включает функционал для записи пользователей на консультации, а также возможностью управления записями через личный кабинет (планируется добавить в будущем). Проект использует базу данных `SQLite`, `Django` и `Bootstrap 5` для стилизации. Также используются `Django сигналы` для обработки событий в приложении.


## Технологии

- **Django**: основной фреймворк для веб-приложения. `pip install django`
- **SQLite**: база данных для хранения информации о пользователях и записях на консультацию. 
- **CrispyForm**: библиотека для улучшенного рендеринга Django форм. `pip install django-crispy-forms`
- **Bootstrap 5**: CSS-фреймворк для стилизации. 
- **Python Telegram Bot**: библиотека для взаимодействия с Telegram API. `pip install python-telegram-bot`
- **Django сигналы**: для обработки событий и взаимодействия между компонентами приложения.

## Установка и запуск проекта

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # для Windows: venv\Scripts\activate
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Скопируйте файл `.env.example` и переименуйте его в `.env`:
    ```bash
    cp .env.example .env
    ```

5. Откройте файл `.env` и заполните следующие переменные окружения:
    - `DJANGO_SECRET_KEY`: секретный ключ Django.
    - `TELEGRAM_BOT_API_KEY`: API-ключ вашего Telegram-бота.

6. Примените миграции:
    ```bash
    python manage.py migrate
    ```

7. Создайте суперпользователя для доступа к админ-панели Django:
    ```bash
    python manage.py createsuperuser
    ```

8. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```


---
## Процесс разработки

### Узнать свой Chat ID в Telegram

Чтобы узнать свой chat ID в Telegram, можно использовать Telegram-бота `@getmyid_bot`


### Получение API-ключа Telegram Bot

Чтобы получить токен для нового бота в Telegram, необходимо выполнить следующие шаги:

1. Найдите в мессенджере бота @BotFather. 25 Это официальный бот для управления другими ботами в Telegram.
2. Отправьте команду «/start» для начала работы. @BotFather предоставит список доступных команд. 
3. Отправьте команду «/newbot» для создания нового бота. Следуйте инструкциям, чтобы задать имя и юзернейм для вашего бота. Имя бота может быть произвольным, но юзернейм должен быть уникальным и заканчиваться на «bot». 
4. После создания бота @BotFather предоставит вам токен. Этот токен необходим для аутентификации вашего бота при взаимодействии с Telegram API. 

Храните токен в защищённом месте и никому не показывайте, иначе к вашему боту могут подключиться злоумышленники и использовать его в своих целях.

### Создание Django проекта и первоначальная настройка

1. Создайте новый Django проект:
```bash
django-admin startproject barbershop .
```

2. Создайте новое Django приложение:
```bash
python manage.py startapp core
```

**django: создание приложения и первоначальная настройка**

### Создание первой модели (простая версия приложения)

1. Создали модель `Visit` для записи на стрижку:

```python
# Класс для записи на стрижку
class Visit(models.Model):
    
    # Статусы записи: по умолчанию - не подтверждена, 1 - подтверждена, 2 - отменена, 3 - выполнена
    STATUS_CHOICES = [
        (0, 'Не подтверждена'),
        (1, 'Подтверждена'),
        (2, 'Отменена'),
        (3, 'Выполнена'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name='Статус')

    def __str__(self):
        return f'{self.name} - {self.phone} - {self.created_at}'
```

2. Выполнили миграции и применили их к базе данных:
```bash
python manage.py makemigrations && python manage.py migrate
```

**django: создание модели Visit**


### Шаблоны

Мы сделали 3 шаблона:

- `base.html` - базовый шаблон, который содержит общую структуру сайта.
- `main.html` - главная страница сайта.
- `thanks.html` - страница благодарности за запись на консультацию.

Подключили BS5 и сделали следующие блоки в базовом шаблоне:

1. `title` - заголовок страницы
2. `header` - шапка сайта
3. `content` - основное содержимое
4. `footer` - подвал сайта

#TODO - добавить sticky header (проверить и мобильную версию)
#TODO - сделать контейнер, заготовку для полос и колонок (сетка BS5)
#TODO - подключить статику (свои стили и скриты)

**django: шаблоны**