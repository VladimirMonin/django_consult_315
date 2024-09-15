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
#TODO - подключить статику (свои стили и скрипты)

**django: шаблоны**

### Подключение модели `Visit` к админ-панели Django

1. Зарегистрировали модель `Visit` в админ-панели Django используя класс:
```python
from .models import Visit

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'phone', 'comment')
```

2. Создали суперпользователя для доступа к админ-панели:
```bash
python manage.py createsuperuser
``` 

**django: подключение модели Visit к админ-панели Django**

### Создание простой формы не связанной с моделью

```python

from django import forms


class VisitForm(forms.Form):
    # Классы form-control, placeholder
    name = forms.CharField(label='Имя', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}))
    phone = forms.CharField(label='Телефон', max_length=20, widget=forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Номер телефона', 'class': 'form-control'}))
    comment = forms.CharField(label='Комментарий', required=False, widget=forms.Textarea(attrs={'placeholder': 'Комментарий', 'class': 'form-control'}))

```

Подключили форму во вью и шаблоне. Но пока не сделали обработку формы.

**django: создание формы VisitForm**


## Lesson 63. Django Classes-based views

### View - базовый класс для создания представлений

1. Импорт базового класса `View` из модуля `django.views.generic`:

```python
from django.views.generic import View
```

2. Создание класса `ThanksView` на основе базового класса `View`:

В котором можно описать методы по названию типа запроса:

```python
class ThanksView(View):
    """
    Метод get - отвечает за запросы GET
    Есть еще и другие методы, например post, put, delete и т.д.
    """
    def get(self, request):
        return render(request, "thanks.html")
```

3. Подключение класса `ThanksView` к URL-пути:

И вызвать там специальный метод `as_view()`, который вернет функцию-обработчик.

## Вне пар. Как работает сигнал m2m_changed в отправке сообщений в ТГ?

Конечно, давайте подробнее рассмотрим условие if action == 'post_add' and kwargs.get('pk_set') в сигнале m2m_changed.

action == 'post_add': Это условие проверяет, было ли действие, вызвавшее сигнал m2m_changed, добавлением новых связанных объектов. Сигнал m2m_changed может срабатывать при различных действиях, таких как добавление (post_add), удаление (post_remove) или очистка (post_clear) связанных объектов. В нашем случае мы хотим отправлять сообщение только при добавлении новых услуг, поэтому мы проверяем, равно ли значение action строке 'post_add'.

kwargs.get('pk_set'): Это условие проверяет, присутствует ли в словаре kwargs ключ 'pk_set' и имеет ли он истинное значение (не None, не пустой список или множество). Когда сигнал m2m_changed срабатывает, Django передает дополнительные аргументы в словаре kwargs, один из которых - 'pk_set'. Этот аргумент содержит множество первичных ключей (primary keys) связанных объектов, которые были добавлены, удалены или очищены. Проверяя наличие и истинность kwargs.get('pk_set'), мы можем определить, были ли фактически добавлены какие-либо связанные объекты.

Комбинация этих двух условий action == 'post_add' and kwargs.get('pk_set') гарантирует, что сообщение в Telegram будет отправлено только один раз после добавления всех связанных услуг. Вот как это работает:

Когда пользователь создает новую запись и выбирает несколько услуг, Django сначала сохраняет основную модель Visit, а затем добавляет связанные объекты Service через ManyToManyField.

Для каждого добавленного объекта Service сигнал m2m_changed срабатывает с действием 'post_add' и соответствующим первичным ключом в kwargs['pk_set'].

При первом срабатывании сигнала условие action == 'post_add' and kwargs.get('pk_set') будет истинным, и сообщение будет отправлено в Telegram.

При последующих срабатываниях сигнала для остальных добавленных услуг условие action == 'post_add' будет по-прежнему истинным, но kwargs['pk_set'] будет содержать только первичный ключ текущей добавленной услуги, а не всех добавленных услуг. Поэтому условие kwargs.get('pk_set') будет ложным, и сообщение не будет отправлено повторно.

Таким образом, комбинация условий action == 'post_add' and kwargs.get('pk_set') гарантирует, что сообщение будет отправлено только один раз после добавления всех услуг, избегая дублирования сообщений в Telegram.


## Lesson 66. CRUD с CreateView, UpdateView, DeleteView

### Get status display

Да, вы правильно понимаете, как работает get_status_display и что status в данном случае - это название поля модели.
get_status_display - это автоматически сгенерированный метод модели Django, который возвращает человекочитаемое значение для поля status, определенного с помощью choices.
Если бы у вас было несколько полей с choices, Django автоматически создаст методы get_<field_name>_display для каждого такого поля. Например, если бы у вас было поле category с choices, то был бы доступен метод get_category_display.
Вы правильно понимаете, что этот метод попадает в вашу модель через магию метаклассов Django. При определении модели Django использует метакласс ModelBase, который автоматически добавляет эти методы в класс модели на основе полей с choices.

### Удаление записей и шаблон подтверждения с POST-запросом


Для создания шаблона подтверждения удаления нужно выполнить следующие шаги:

Создать шаблон visit_confirm_delete.html в папке core/templates:
{% extends "base.html" %}

{% block title %}Удаление заявки{% endblock %}

{% block content %}
<div class="container py-4">
    <div class="row">
        <div class="col-md-8 offset-md-2">
            <h2 class="mb-4">Удаление заявки</h2>
            <p>Вы уверены, что хотите удалить заявку "{{ visit.name }}"?</p>
            <form method="post">
                {% csrf_token %}
                <button type="submit" class="btn btn-danger">Удалить</button>
                <a href="{% url 'visit-view' visit.pk %}" class="btn btn-secondary">Отмена</a>
            </form>
        </div>
    </div>
</div>
{% endblock %}

Copy

Apply

visit_confirm_delete.html
Указать путь к шаблону template_name в классе VisitDeleteView в файле core/views.py:
class VisitDeleteView(DeleteView):
    template_name = "visit_confirm_delete.html"
    model = Visit
    success_url = reverse_lazy("thanks")

Copy

Apply

views.py
Добавить URL для удаления в файле barbershop/urls.py:
path("visit/<int:pk>/delete/", VisitDeleteView.as_view(), name="visit-delete"),

Copy

Apply

urls.py
Теперь при переходе по URL вида /visit/1/delete/ будет отображаться страница с подтверждением удаления заявки. После подтверждения удаления пользователь будет перенаправлен на страницу "Спасибо" (thanks).

Try again with different context
Public knowledge only
Add context...
Avatar for vladimir.monin2016-nsmwj
VladimirMonin
Расскажи про запрос от кнопки подтверждения удаления. Обязательно пост? По какому маршруту идет? Какие там есть варианты?



Claude 3 Opus
Да, запрос от кнопки подтверждения удаления должен быть POST-запросом. Это связано с тем, что удаление является изменяющей операцией и не должно выполняться через GET-запрос.

В шаблоне visit_confirm_delete.html форма отправляется методом POST:

<form method="post">
    {% csrf_token %}
    <button type="submit" class="btn btn-danger">Удалить</button>
    <a href="{% url 'visit-view' visit.pk %}" class="btn btn-secondary">Отмена</a>
</form>

Copy

Apply

Маршрут для удаления заявки определен в файле barbershop/urls.py:

path("visit/<int:pk>/delete/", VisitDeleteView.as_view(), name="visit-delete"),

Copy

Apply

Этот маршрут связан с классом VisitDeleteView в файле core/views.py:

class VisitDeleteView(DeleteView):
    template_name = "visit_confirm_delete.html"
    model = Visit
    success_url = reverse_lazy("thanks")

Copy

Apply

Класс DeleteView автоматически обрабатывает POST-запрос на удаление объекта. При GET-запросе он отображает страницу подтверждения удаления, а при POST-запросе выполняет удаление объекта и перенаправляет на страницу, указанную в success_url.

Варианты настройки DeleteView:

template_name: путь к шаблону страницы подтверждения удаления.
model: модель, объект которой будет удаляться.
success_url: URL для перенаправления после успешного удаления. Можно указать строку или использовать reverse_lazy() для получения URL по имени маршрута.
context_object_name: имя переменной контекста, которая будет содержать удаляемый объект (по умолчанию object).
pk_url_kwarg: имя параметра в URL, содержащего первичный ключ удаляемого объекта (по умолчанию pk).
Таким образом, при нажатии на кнопку "Удалить" в шаблоне visit_confirm_delete.html будет отправлен POST-запрос по маршруту visit/<int:pk>/delete/, который обработает VisitDeleteView, удалит заявку и перенаправит пользователя на страницу "Спасибо".

Try again with different context
Add context...
Avatar for vladimir.monin2016-nsmwj
VladimirMonin
Что содержится в теле пост запроса, он пустой?



Claude 3 Opus
В теле POST-запроса при удалении объекта через Django DeleteView по умолчанию ничего не передается. Сам факт отправки POST-запроса уже является подтверждением удаления.

В шаблоне visit_confirm_delete.html мы видим форму:

<form method="post">
    {% csrf_token %}
    <button type="submit" class="btn btn-danger">Удалить</button>
    <a href="{% url 'visit-view' visit.pk %}" class="btn btn-secondary">Отмена</a>
</form>

Copy

Apply

Эта форма содержит только один элемент - {% csrf_token %}. Это специальный тег шаблонизатора Django, который добавляет скрытое поле с токеном CSRF (Cross-Site Request Forgery) для защиты от подделки межсайтовых запросов.

При отправке формы методом POST, в теле запроса будет передан только этот CSRF-токен. Никаких дополнительных данных в теле запроса не будет.

Django DeleteView автоматически обрабатывает POST-запрос и выполняет удаление объекта на основе переданного в URL первичного ключа (pk). Он не ожидает никаких специфических данных в теле запроса.

Таким образом, тело POST-запроса при удалении объекта через Django DeleteView будет содержать только CSRF-токен, а сам запрос будет пустым с точки зрения передаваемых данных.

## Logout методом POST

**Вариант 1: Изменение ссылки на форму в menu.html**

В этом варианте мы заменяем простую ссылку на форму с POST-запросом:

```html
<form method="post" action="{% url 'logout' %}" class="d-inline">
    {% csrf_token %}
    <button type="submit" class="btn btn-link nav-link">Выход</button>
</form>
```

Этот подход обеспечивает отправку POST-запроса при нажатии на кнопку "Выход", что соответствует ожиданиям стандартного LogoutView Django.

**Вариант 2: Настройка CustomLogoutView для обработки GET-запросов**

В этом варианте мы модифицируем CustomLogoutView в файле user/views.py:
```python
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.shortcuts import redirect

class CustomLogoutView(LogoutView):
    next_page = 'main'
    template_name = 'logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(self.get_next_page())
```

Этот подход позволяет обрабатывать GET-запросы для логаута, сохраняя при этом простую ссылку в меню:

`<a class="nav-link" href="{% url 'logout' %}">Выход</a>`

Оба варианта решают проблему с логаутом, выбор зависит от предпочтений в дизайне и безопасности.