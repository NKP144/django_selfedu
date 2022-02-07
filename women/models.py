from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)  # blank - поле м.б. пустым
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")     # Хранит путь к файлу
    time_create = models.DateTimeField(auto_now_add=True)   # Фиксирует текущее время в момент добавления записи и менятся не будет
    time_update = models.DateTimeField(auto_now=True)   # Время будет меняться каждый раз, когда происходит обновление записи
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)  # Внешний ключ на таблицу Category

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # Это функция используется в шаблоне для возврата ссылки на элемент из БАЗЫ ДАННЫХ
        return reverse('post', kwargs={'post_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
