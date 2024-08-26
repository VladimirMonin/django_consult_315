from django.shortcuts import render, redirect
from .models import Visit


def main(request):
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment', '')

        
        # Создаем новую запись посещения в базе данных
        Visit.objects.create(
            name=name,
            phone=phone,
            comment=comment,

        )
        
        # Перенаправляем на страницу благодарности после успешного создания записи
        return redirect('thanks')
    
    # Обработка GET-запроса или других типов запросов
    return render(request, 'main.html')


def thanks(request):
    return render(request, 'thanks.html')