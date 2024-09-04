"""
admin/ - админка
"" - главная страница
thanks/ - страница благодарности
get_services_by_master/<int:master_id>/ - получение услуг по мастеру
visit-form/ - форма записи на услугу CreateView

----
visits/ - каталог заявок ListView
visit/1/view/  - детальное представление визита DetailView
visit/1/edit/ - редактирование визита UpdateView
visit/1/delete/ - удаление визита DeleteView
"""

from django.contrib import admin
from django.urls import path
from core.views import (
    get_services_by_master,
    MainView,
    ThanksTemplateView,
    VisitCreateView,
    VisitDetailView,
    VisitUpdateView,
    VisitDeleteView,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", MainView.as_view(), name="main"),
    path("thanks/", ThanksTemplateView.as_view(), name="thanks"),
    path(
        "get_services_by_master/<int:master_id>/",
        get_services_by_master,
        name="get_services_by_master",
    ),
    # CRUD для Visit 
    path("visit/add/", VisitCreateView.as_view(), name="visit-form"),
    # Read на DetailView
    path("visit/<int:pk>/view/", VisitDetailView.as_view(), name="visit-view"),
    # Update на UpdateView
    path("visit/<int:pk>/edit/", VisitUpdateView.as_view(), name="visit-edit"),
    # DeleteView
    path("visit/<int:pk>/delete/", VisitDeleteView.as_view(), name="visit-delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
