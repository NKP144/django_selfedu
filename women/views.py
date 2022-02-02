from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request): #HttpRequest
    return HttpResponse("Страница приложения women.")

def categories(request, catid):
    if(request.GET):        ## Парамтры GET-запроса
        print(request.GET)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        ##raise Http404()                       ## Генерирование страницы с ошибкой 404
        return redirect('home_page', permanent=True)    ## Гененирование ответа 300 или 301
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(reques, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
