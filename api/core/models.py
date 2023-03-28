from datetime import datetime as dt, date

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# ======{ Профиль }======

class Profile(models.Model):
    user = models.OneToOneField(verbose_name="Пользователь", to=User, on_delete=models.CASCADE)
    image = models.ImageField("Аватар", null=True, blank=True, default=None, upload_to="users/")

    class Meta:
        verbose_name = "Расширенный пользователь"
        verbose_name_plural = "Расширенные пользователи"

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user).save()


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
        return f"{self.title}+"


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
    title_image = models.ImageField("Название изображением", blank=True, null=True, default=None,
                                    upload_to="movies/title-images/")
    tagline = models.CharField("Слоган", max_length=100, default='', blank=True)
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


# ======{ Сериал }======

class TVSeries(models.Model):
    title = models.CharField("Название", max_length=100, unique=True)
    title_image = models.ImageField("Название изображением", blank=True, null=True, default=None,
                                    upload_to="tvseries/title-images/")
    tagline = models.CharField("Слоган", max_length=100, default='', blank=True)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="tvseries/images/")

    directors = models.ManyToManyField(Person, verbose_name="Режиссер", related_name="tvseries_director")
    actors = models.ManyToManyField(Person, verbose_name="Актеры", related_name="tvseries_actor")

    genres = models.ManyToManyField(Genre, verbose_name="Жанры", related_name="tvseries_genre")
    country = models.ManyToManyField(Country, verbose_name="Страны", related_name="tvseries_country")
    ageLimit = models.ForeignKey(to=AgeLimit, on_delete=models.SET_NULL, null=True,
                                 verbose_name="Возрастное ограничение")
    rating = models.FloatField("Рейтинг")

    poster_horizontal_with_text = models.ImageField("Горизонтальный постер с названием", upload_to="tvseries/images/")
    poster_horizontal_without_text = models.ImageField("Горизонтальный постер без названия",
                                                       upload_to="tvseries/images/")

    class Meta:
        verbose_name = "Сериал"
        verbose_name_plural = "Сериалы"

    def __str__(self):
        return self.title


class SeasonTVSeries(models.Model):
    tvseries = models.ForeignKey(to=TVSeries, on_delete=models.CASCADE, verbose_name="Сериал")
    number = models.IntegerField("Номер сезона", unique=True)
    year = models.PositiveSmallIntegerField("Дата выхода", default=dt.now().year)

    class Meta:
        verbose_name = "Сезон сериала"
        verbose_name_plural = "Сезоны сериала"

    def __str__(self):
        return f"{self.tvseries} - {self.number}"


class SeriesTVSeries(models.Model):
    season_tvseries = models.ForeignKey(to=SeasonTVSeries, on_delete=models.CASCADE, verbose_name="Сезон сериала")
    number = models.IntegerField("Номер серии", unique=True)
    title = models.CharField("Название", max_length=100, blank=True, null=True, default=None)
    description = models.TextField("Описание")
    timeline = models.IntegerField("Продолжительность", help_text="Указывать продолжительность в минутах")
    series = models.FileField("Файл серии", upload_to="tvseries/tvseries/")
    date_publish = models.DateField("Дата выхода", default=date.today)

    class Meta:
        verbose_name = "Серия сериала"
        verbose_name_plural = "Серии сериала"

    def __str__(self):
        return f"{self.season_tvseries} - {self.number}"
