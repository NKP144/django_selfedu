from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")  # blank - поле м.б. пустым
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")     # Хранит путь к файлу
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")   # Фиксирует текущее время в момент добавления записи и менятся не будет
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")   # Время будет меняться каждый раз, когда происходит обновление записи
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")  # Внешний ключ на таблицу Category

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # Это функция используется в шаблоне для возврата ссылки на элемент из БАЗЫ ДАННЫХ
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Известные женщины"
        verbose_name_plural = "Известные женщины"
        ordering = ['time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']
