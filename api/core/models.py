from datetime import date, datetime as dt

from django.contrib.auth.models import User
from django.db import models


# ======{ Профиль }======
class Profile(models.Model):
    user = models.OneToOneField(verbose_name="Пользователь", to=User, on_delete=models.CASCADE)
    image = models.ImageField("Аватар", null=True, blank=True, default=None, upload_to="users/")

    class Meta:
        verbose_name = "Расширенный пользователь"
        verbose_name_plural = "Расширенные пользователи"

    def __str__(self):
        return self.user.username


# ======{ Персона (Актер, Режиссер...) }======

class Career(models.Model):
    title = models.CharField("Название", max_length=32, unique=True)

    class Meta:
        verbose_name = "Карьера"
        verbose_name_plural = "Виды карьер"

    def __str__(self):
        return self.title


class Person(models.Model):
    lastname = models.CharField("Фамилия", max_length=32, blank=True, null=True, default=None)
    username = models.CharField("Имя", max_length=32)
    pastname = models.CharField("Отчество", max_length=32, blank=True, null=True, default=None)
    image = models.ImageField("Аватар", null=True, blank=True, default=None, upload_to="persons/")
    career = models.ManyToManyField(to=Career, verbose_name="Карьера", related_name="person_career")

    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"

    def __str__(self):
        name = self.username
        if self.lastname is not None:
            name = f"{self.lastname} {name}"
        if self.pastname is not None:
            name = f"{name} {self.pastname}"
        return name


# ======{ Фильм }======

class AgeLimit(models.Model):
    title = models.CharField("Ограничение", max_length=2, unique=True)

    class Meta:
        verbose_name = "Возрастное ограничение"
        verbose_name_plural = "Возрастное ограничение"

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField("Название", max_length=32, unique=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанр"

    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField("Название", max_length=32, unique=True)

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страна"

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField("Название", max_length=100, unique=True)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="movies/images/")

    directors = models.ManyToManyField(Person, verbose_name="Режиссер", related_name="movie_director")
    actors = models.ManyToManyField(Person, verbose_name="Актеры", related_name="movie_actor")

    genres = models.ManyToManyField(Genre, verbose_name="Жанры", related_name="movie_genre")
    country = models.ManyToManyField(Country, verbose_name="Страны", related_name="movie_country")

    year = models.PositiveSmallIntegerField("Дата выхода", default=dt.now().year)
    ageLimit = models.ForeignKey(to=AgeLimit, on_delete=models.SET_NULL, null=True,
                                 verbose_name="Возрастное ограничение")
    rating = models.FloatField("Рейтинг")
    timeline = models.IntegerField("Продолжительность", help_text="Указывать продолжительность в минутах")

    poster_horizontal_with_text = models.ImageField("Горизонтальный постер с названием", upload_to="movies/images/")
    poster_horizontal_without_text = models.ImageField("Горизонтальный постер без названия", upload_to="movies/images/")

    movie = models.FileField("Файл фильма", upload_to="movies/movies/")


    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.title
