from django.db import models
# from django.utils.text import slugify
# from .utils import from_cyrillic_to_eng
from pytils.translit import slugify


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Название города',
                            unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название города'
        verbose_name_plural = 'Название городов'

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     if self.slug is None:
    #         self.slug = from_cyrillic_to_eng(self.name)
    #     super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Язык программирования',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Заголовок вакансии')
    company = models.CharField(max_length=250, verbose_name='Компания')
    description = models.TextField(verbose_name='Описание вакансии')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 verbose_name='Язык программирования')
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
