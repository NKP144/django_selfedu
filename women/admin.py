from django.contrib import admin

from .models import *


class WomenAdmin(admin.ModelAdmin):
    """Класс-редактор для задания параметров представления модели"""
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')  # Поля, которые выводятся в списке записей
    list_display_links = ('id', 'title')                 # Поля, которые преобразуются в гиперссылки для правки записей
    search_fields = ('title', 'content')                 # Поля для поиска
    list_editable = ('is_published',)                    # Список редактируемых полей
    list_filter = ('is_published', 'time_create')        # Поля для фильтрации


class CategoryAdmin(admin.ModelAdmin):
    """Класс-редактор для задания параметров представления модели"""
    list_display = ('id', 'name')  # Поля, которые выводятся в списке записей
    list_display_links = ('id', 'name')                 # Поля, которые преобразуются в гиперссылки для правки записей
    search_fields = ('name',)                 # Поля для фильтрации


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
