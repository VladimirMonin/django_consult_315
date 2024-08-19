from django.contrib import admin
from .models import Visit

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'phone', 'comment')