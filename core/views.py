from django.shortcuts import render, redirect
from .forms import VisitModelForm
from .models import Visit, Master, Service
from django.http import JsonResponse
from django.views.generic import View # Импорт базового View класса


def main(request):
    # Мастера для карусели фоточек (в форму данные берутся и по мастерам и по услугам автоматически)
    masters = Master.objects.all()
    
    if request.method == 'POST':
        form = VisitModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
        
        # Отдаем заполненную форму с ошибку
        if form.errors:
            return render(request, "main.html", {"form": form, 'masters': masters})

    else:
        form = VisitModelForm()

    
    return render(request, 'main.html', {'form': form, 'masters': masters})


class ThanksView(View):
    """
    Метод get - отвечает за запросы GET
    Есть еще и другие методы, например post, put, delete и т.д.
    """
    def get(self, request):
        return render(request, "thanks.html")


def get_services_by_master(request, master_id):
    services = Master.objects.get(id=master_id).services.all()
    services_data = [{'id': service.id, 'name': service.name} for service in services]
    return JsonResponse({'services': services_data})

