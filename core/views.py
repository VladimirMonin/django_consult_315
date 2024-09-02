from django.shortcuts import render, redirect
from .forms import VisitModelForm
from .models import Visit, Master, Service
from django.http import JsonResponse
from django.views.generic import View, TemplateView

MENU = [
        {'title': 'Главная', 'url': '/', 'active': True},
        {'title': 'Мастера', 'url': '#masters', 'active': True},
        {'title': 'Услуги', 'url': '#services', 'active': True},
        {'title': 'Отзывы', 'url': '#reviews', 'active': True},
        {'title': 'Запись на стрижку', 'url': '#orderForm', 'active': True},
    ]

def get_menu_context(menu: list[dict] = MENU):
    return {"menu": menu}



class MainView(View):
    """
    Метод get - отвечает за запросы GET
    Есть еще и другие методы, например post, put, delete и т.д.
    """
    
    def get(self, request):
        menu = get_menu_context()
        form = VisitModelForm()
        masters = Master.objects.all()

        return render(request, "main.html", {"form": form, "masters": masters, **menu})
    

    def post(self, request):
        form = VisitModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thanks")

        # Отдаем заполненную форму с ошибку
        if form.errors:
            return render(
                request,
                "main.html",
                {"form": form, "masters": Master.objects.all(), **get_menu_context()},
            )


class ThanksView(View):
    """
    Метод get - отвечает за запросы GET
    Есть еще и другие методы, например post, put, delete и т.д.
    """
    
    def get(self, request):
        return render(request, "thanks.html", get_menu_context())


def get_services_by_master(request, master_id):
    services = Master.objects.get(id=master_id).services.all()
    services_data = [{'id': service.id, 'name': service.name} for service in services]
    return JsonResponse({'services': services_data})


class ThanksTemplateView(TemplateView):
    template_name = "thanks.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_menu_context())
        return context
