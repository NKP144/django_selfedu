from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)  # blank - поле м.б. пустым
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")     # Хранит путь к файлу
    time_create = models.DateTimeField(auto_now_add=True)   # Фиксирует текущее время в момент добавления записи и менятся не будет
    time_update = models.DateTimeField(auto_now=True)   # Время будет меняться каждый раз, когда происходит обновление записи
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title