from django.urls import path, re_path
from .views import *
from coolsite import settings
from django.urls import path, include
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path('', index, name='home_page'),             # http://127.0.0.1:8000/
    # path('cats/<int:catid>/', categories),              # http://127.0.0.1:8000/cats/1/
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive)   # Функция для обработки пути с помощью регулярного выражения
    path('', WomenHome.as_view(), name='home_page'),      # http://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    # path('category/<int:cat_id>/', show_category, name='category'),  # Отображение категорий по ID
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),  # Отображение категорий по slug
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls'))
    ] + urlpatterns
