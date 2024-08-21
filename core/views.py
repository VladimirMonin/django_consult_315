from django.shortcuts import render, redirect
from .forms import VisitForm
from .models import Visit, Master


def main(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            # Создание и сохранение записи в модели Visit
            Visit.objects.create(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                comment=form.cleaned_data.get('comment', '')
            )
            # Перенаправляем пользователя на страницу с благодарностью после успешного сохранения
            return redirect('thanks')
    else:
        form = VisitForm()

    # Получение всех мастеров из базы данных
    masters = Master.objects.all()
    return render(request, 'main.html', {'form': form, 'masters': masters})


def thanks(request):
    return render(request, 'thanks.html')