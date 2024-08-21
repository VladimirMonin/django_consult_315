from tabnanny import verbose
from django.db import models


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
        return f'{self.name} - {self.phone}'
    
        
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


# Класс для мастеров
class Master(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=255, verbose_name='Домашний адрес')
    photo = models.ImageField(upload_to='masters/photos/', blank=True, null=True, verbose_name='Фотография')

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.phone}'
    
    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"

# Класс для услуг
class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    masters = models.ManyToManyField(Master, related_name='services', verbose_name='Мастера')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"