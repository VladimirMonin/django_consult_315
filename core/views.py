from django.shortcuts import render, redirect
from .models import Visit
from .validators import super_validator
from .forms import VisitForm


def main(request):
    if request.method == 'POST':
        # Создаем экземпляр формы
        form = VisitForm(request.POST)

        # Проверяем, что форма валидна
        if form.is_valid():
            # Создаем новую запись посещения в базе данных
            visit = Visit(
                # cleaned_data - словарь с очищенными данными из формы, после валидации
                name=form.cleaned_data["name"],
                phone=form.cleaned_data["phone"],
                comment=form.cleaned_data["comment"],
            )
            visit.save()
            # Перенаправляем на страницу благодарности после успешного создания записи
            return redirect('thanks')
    
        else:
            # Если форма не валидна, передаем ее в контекст шаблона
            return render(request, "main.html", {"form": form})
    
    else:
        # Обработка GET-запроса или других типов запросов
        return render(request, "main.html", {"form": VisitForm()})


def thanks(request):
    return render(request, 'thanks.html')