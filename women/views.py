from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]


def index(request):  # HttpRequest
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):  # HttpRequest
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, catid):
    if(request.GET):        # Парамтры GET-запроса
        print(request.GET)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        # raise Http404()                       # Генерирование страницы с ошибкой 404
        return redirect("home_page", permanent=True)    # Гененирование ответа 300 или 301
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def show_category(request, cat_id):
    context = {
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(reques, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
