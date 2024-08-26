from django.shortcuts import render, redirect
from .models import Visit
from .validators import super_validator


def main(request):
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment', '')

        # Валидация данных
        if super_validator(name) and super_validator(phone):
            # Данные валидны, продолжаем обработку
            
        
            # Создаем новую запись посещения в базе данных
            Visit.objects.create(
                name=name,
                phone=phone,
                comment=comment,

            )
            
            # Перенаправляем на страницу благодарности после успешного создания записи
            return redirect('thanks')
    
        else:
            # Данные не валидны, выводим сообщение об ошибке
            error_message = "Пожалуйста, заполните все поля корректно."
            # Возвращаем ошибку в шаблон (на уровне шаблона нужна првоерка if)
            return render(request, "main.html", {"error_message": error_message})
    
    
    # Обработка GET-запроса или других типов запросов
    return render(request, 'main.html')


def thanks(request):
    return render(request, 'thanks.html')