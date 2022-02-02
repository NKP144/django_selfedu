from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('home/', index, name='home_page'),             # http://127.0.0.1:8000/women/
    path('cats/<int:catid>/', categories),              # http://127.0.0.1:8000/women/cats/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)   # Функция для обработки пути с помощью регулярного выражения
]
