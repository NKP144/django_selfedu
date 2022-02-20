from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]


class WomenHome(DataMinix, ListView):  # Класс-представление
    model = Women           # Связь с моделью
    template_name = 'women/index.html'
    context_object_name = 'posts'   # Имя генерируемого списка элементов. По дефолту object_list
#   extra_context = {'title': 'Главная страница'}  # Передача статических, неизменяемых параметров. Поле menu так передать нельзя

    def get_context_data(self, *, object_list=None, **kwargs): # Функция для передачи и статического и динамического контекста
        context = super().get_context_data(**kwargs)  # Взять уже существующий контекст
        # context['menu'] = menu
        # context['title'] = 'Главная страница'
        # context['cat_selected'] = 0
        c_def = self.get_user_context(title="Главная страница")  # Формируем доп. контекс в функции из класса DataMixin
        return dict(list(context.items()) + list(c_def.items()))
        # return context.update(c_def)
        # return context|c_def

    def get_queryset(self):  # Метод для выбора из модели только необходимых записей
        return Women.objects.filter(is_published=True).select_related('cat')


# def index(request):  # HttpRequest
#     context = {
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'women/index.html', context=context)

#@login_required  # Декоратор функций-представлений (не классов, в классах используется миксин LoginRequiredMixin) для проверки авторизации пользователя
def about(request):  # HttpRequest
    # contact_list = Women.objects.all()
    # paginator = Paginator(contact_list, 3)
    #
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # return render(request, 'women/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'О сайте'})
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


class AddPage(LoginRequiredMixin, DataMinix, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home_page')
    login_url = reverse_lazy('home_page') #  Фукнция позволят использовать имена URL путей из urls.py
    raise_exception = True #  Для генерации страницы 403 - Доступ запрещён, если пользователь не авторизован

    def get_context_data(self, *, object_list=None, **kwargs): # Функция для передачи и статического и динамического контекста
        context = super().get_context_data(**kwargs)  # Взять уже существующий контекст
        c_def = self.get_user_context(title="Добавление статьи")  # Формируем доп. контекс в функции из класса DataMixin
        return dict(list(context.items()) + list(c_def.items()))  # Возвраст словаря с контекстом


# def addpage(request):
#     if request.method == 'POST':            # Проверка метода запроса. Если ответ из формы, то метод будет POST
#         form = AddPostForm(request.POST, request.FILES)        # Заполняем форму данными из запроса и файлами
#         if form.is_valid():                     # Проверка валидности данных формы
#             # ----------------------------------------------------------------------------------------------------------
#             # Проверка на ошибки не требуется т.к. методо form.save() делает это самостоятельно
#             # print(form.cleaned_data)            # Если валидные данные, то отобразить данные в консоле
#             # try:
#             #    # Women.objects.create(**form.cleaned_data)  # Добавляем в базу данных запись. Для формы не связанной с моделью
#             #    form.save()  # хранение данных формы в базу данных. Для формы связанной с моделью
#             #    return redirect('home_page')               # Возврат на главную страницу
#             # except:
#             #    form.add_error(None, 'Ошибка добавления поста')  # Добавили общую ошибка для отображения формы
#             # ----------------------------------------------------------------------------------------------------------
#             form.save()
#             return redirect('home_page')
#     else:                                   # Если первая отправка формы на страницу (в запросе метод = None)
#         form = AddPostForm()                # Взять чистую форму
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


# def contact(request):
#     return HttpResponse("Обратная связь")


class ContactFormView(DataMinix, FormView):
    form_class = ContactForm
    template_name = 'women/contact.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, *, object_list=None, **kwargs): # Функция для передачи и статического и динамического контекста
        context = super().get_context_data(**kwargs)  # Взять уже существующий контекст
        c_def = self.get_user_context(title='Обратная связь')  # Формируем доп. контекс в функции из класса DataMixin
        return dict(list(context.items()) + list(c_def.items()))  # Возвраст словаря с контекстом

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home_page')


def logout_user(request):
    logout(request)
    return redirect('login')


class ShowPost(DataMinix, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs): # Функция для передачи и статического и динамического контекста
        context = super().get_context_data(**kwargs)  # Взять уже существующий контекст
        c_def = self.get_user_context(title=context['post'])  # Формируем доп. контекс в функции из класса DataMixin
        return dict(list(context.items()) + list(c_def.items()))  # Возвраст словаря с контекстом


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)  # Функция возвращает запись из таблицы или генерирует исключение 404 при отсутствии
#     return render(request, 'women/post.html', context=context)


class WomenCategory(DataMinix, ListView):  # Класс-представление
    model = Women           # Связь с моделью
    template_name = 'women/index.html'
    context_object_name = 'posts'   # Имя генерируемого списка элементов. По дефолту object_list
    allow_empty = False     # Если получился пустой список, то сгенерировать страницу 404

    def get_context_data(self, *, object_list=None, **kwargs): # Функция для передачи и статического и динамического контекста
        context = super().get_context_data(**kwargs)  # Взять уже существующий контекст
        c_def = self.get_user_context(title='Категоря - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)  # Формируем доп. контекс в функции из класса DataMixin
        return dict(list(context.items()) + list(c_def.items()))  # Возвраст словаря с контекстом

    def get_queryset(self):  # Метод для выбора из модели только необходимых записей
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')  # cat__slug - ображение к полю slug модели Category связанной с Women


# def show_category(request, cat_slug):
#     cat = get_object_or_404(Category, slug=cat_slug)  # Функция возвращает запись из таблицы или генерирует исключение 404 при отсутствии
#     return render(request, 'women/index.html', context=context)

class RegisterUser (DataMinix, CreateView):
    """ Класс-представления для регистрации пользователя """
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs): # Функция для передачи и статического и динамического контекста
        context = super().get_context_data(**kwargs)  # Взять уже существующий контекст
        c_def = self.get_user_context(title='Регистрация')  # Формируем доп. контекс в функции из класса DataMixin
        return dict(list(context.items()) + list(c_def.items()))  # Возвраст словаря с контекстом

    def form_valid(self, form):
        user = form.save()  # Сохранили пользователя в БД
        login(self.request, user)  # Авторизация пользователя
        return redirect('home_page')


class LoginUser(DataMinix, LoginView):
    """ Класс-представление для авторизации пользователя в системе """
    form_class = LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):  # Функция для передачи и статического и динамического контекста
        context = super().get_context_data(**kwargs)  # Взять уже существующий контекст
        c_def = self.get_user_context(title='Авторизация')  # Формируем доп. контекс в функции из класса DataMixin
        return dict(list(context.items()) + list(c_def.items()))  # Возвраст словаря с контекстом

    def get_success_url(self):
        return reverse_lazy('home_page')


def pageNotFound(reques, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
