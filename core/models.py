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
        return f'{self.name} - {self.phone} - {self.created_at}'
    
