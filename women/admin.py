from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class WomenAdmin(admin.ModelAdmin):
    """Класс-редактор для задания параметров представления модели"""
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')  # Поля, которые выводятся в списке записей
    list_display_links = ('id', 'title')                 # Поля, которые преобразуются в гиперссылки для правки записей
    search_fields = ('title', 'content')                 # Поля для поиска
    list_editable = ('is_published',)                    # Список редактируемых полей
    list_filter = ('is_published', 'time_create')        # Поля для фильтрации
    prepopulated_fields = {"slug": ("title",)}           # Автоматически заполнять поле slug на основе поля title
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')   # Редактируемые поля
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')    # Нередактируемые поля. Обязательно указывать,
                                                        # для отображения в редактируемых полях
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")    # marj_safe - не экранировать тэги

    get_html_photo.short_description = "Фото"

class CategoryAdmin(admin.ModelAdmin):
    """Класс-редактор для задания параметров представления модели"""
    list_display = ('id', 'name')              # Поля, которые выводятся в списке записей
    list_display_links = ('id', 'name')        # Поля, которые преобразуются в гиперссылки для правки записей
    search_fields = ('name',)                  # Поля для фильтрации
    prepopulated_fields = {"slug": ("name",)}  # Автоматически заполнять поле slug на основе поля name

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админ-панель сайто о женщинах'     # Имзменяет название сайте
admin.site.site_header = 'Админ-панель сайто о женщинах'    # Изменяет заголовок сайта

# Register your models here.
