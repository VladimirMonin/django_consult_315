from django.shortcuts import render, redirect
from .forms import VisitModelForm
from .models import Visit, Master, Service
from django.http import JsonResponse
from django.views.generic import (
    View,
    TemplateView,
    FormView,
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView,
)
from django.urls import reverse_lazy

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


# VisitFormView

class VisitFormView(FormView):
    template_name = "visit_form.html"
    form_class = VisitModelForm
    success_url = "/thanks/"
    context = get_menu_context()

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class VisitCreateView(CreateView):
    template_name = "visit_form.html"
    model = Visit
    # fields = ["name", "phone", "comment", "master", "services"] # Мы можем обойтись даже без формы!!!
    form_class = VisitModelForm
    # Подтянем url по псевдониму thanks\
    # Функция для поиска маршрутов по имени
    success_url = reverse_lazy("thanks")
 
    
class VisitUpdateView(UpdateView):
    template_name = "visit_form.html"
    model = Visit
    # fields = ["name", "phone", "comment", "master", "services"] # Мы можем обойтись даже без формы!!!
    form_class = VisitModelForm
    # Подтянем url по псевдониму thanks\
    # Функция для поиска маршрутов по имени
    success_url = reverse_lazy("thanks")

    
class VisitDetailView(DetailView):
    template_name = "visit_detail.html"
    model = Visit
    context_object_name = "visit"


class VisitDeleteView(DeleteView):
    template_name = "visit_confirm_delete.html"
    model = Visit
    success_url = reverse_lazy("thanks")
