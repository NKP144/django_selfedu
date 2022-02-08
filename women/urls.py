from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home_page'),             # http://127.0.0.1:8000/
    # path('cats/<int:catid>/', categories),              # http://127.0.0.1:8000/cats/1/
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive)   # Функция для обработки пути с помощью регулярного выражения
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]
