from django.shortcuts import render, redirect
from .models import Visit
from .validators import super_validator
from .forms import VisitForm, VisitModelForm


def main(request):
    if request.method == 'POST':
        # Создаем экземпляр формы
        form = VisitModelForm(request.POST)

        # Проверяем, что форма валидна
        if form.is_valid():
            # Теперь сохранение будет быстрее. Просто сохраняем данные
            form.save()
            
            # Перенаправляем на страницу благодарности после успешного создания записи
            return redirect('thanks')
    
        else:
            # Если форма не валидна, передаем ее в контекст шаблона
            return render(request, "main.html", {"form": form})
    
    else:
        # Обработка GET-запроса или других типов запросов
        return render(request, "main.html", {"form": VisitModelForm()})


def thanks(request):
    return render(request, 'thanks.html')