from django.contrib import admin
from django.urls import path
from core.views import get_services_by_master, ThanksView, MainView, ThanksTemplateView
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
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
