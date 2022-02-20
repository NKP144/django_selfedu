from django.db.models import Count
from django.core.cache import cache

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
       ]


class DataMinix:
    """ Класс-миксин для добавления в классы представлений """
    paginate_by = 3     # Пагинатор, для постраничного вывода списка
    def get_user_context(self, **kwargs):
        context = kwargs
        # cats = Category.objects.all()
        # cats = cache.get('cats')    # Проверяем, есть ли категории в кэше
        # if not cats:                # Если нет, то считываем и заносим в кэш
        #     cats = Category.objects.annotate(Count('women'))  # В объекте cats теперь есть и кол-во постов
        #     cache.set('cats', cats, 60)
        cats = Category.objects.annotate(Count('women'))  # В объекте cats теперь есть и кол-во постов

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

