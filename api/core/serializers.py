from rest_framework import serializers

from .helper.helper_serializers import get_genre_list, get_country_list
from .models import Movie, AgeLimit, Genre, Country, TVSeries, SeasonTVSeries, SeriesTVSeries, Person


class AgeLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeLimit
        fields = ("title",)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("title",)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("title",)


# ===========
# ПЕРСОНЫ
# ===========
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("id", "lastname", "username", "pastname", "image")


# ===========
# ФИЛЬМЫ
# ===========


class MovieSerializer(serializers.ModelSerializer):
    ageLimit = serializers.SlugRelatedField(slug_field="title", queryset=AgeLimit.objects.all())
    genres = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ("id", "title", "title_image", "description", "year", "genres", "country", "ageLimit")

    @staticmethod
    def get_genres(instance):
        return get_genre_list(instance)

    @staticmethod
    def get_country(instance):
        return get_country_list(instance)


class MiniMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "rating", "poster_horizontal_with_text")


class DetailMovieSerializer(serializers.ModelSerializer):
    ageLimit = serializers.SlugRelatedField(slug_field="title", queryset=AgeLimit.objects.all())
    genres = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    directors = PersonSerializer(read_only=True, many=True)
    actors = PersonSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = (
            "id", "title", "title_image", "description", "genres", "country", "ageLimit", "directors", "actors"
        )

    @staticmethod
    def get_genres(instance):
        return get_genre_list(instance)

    @staticmethod
    def get_country(instance):
        return get_country_list(instance)


# ===========
# СЕРИИ
# ===========
class SeriesTVSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesTVSeries
        fields = ("id", "number", "title", "description", "timeline", "date_publish")


# ===========
# СЕРИАЛЫ
# ===========

class TVSeriesSerializer(serializers.ModelSerializer):
    ageLimit = serializers.SlugRelatedField(slug_field="title", queryset=AgeLimit.objects.all())
    genres = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()

    class Meta:
        model = TVSeries
        fields = ("id", "title", "title_image", "description", "genres", "country", "ageLimit")

    @staticmethod
    def get_genres(instance):
        return get_genre_list(instance)

    @staticmethod
    def get_country(instance):
        return get_country_list(instance)


class MiniTVSeriesSerializer(serializers.ModelSerializer):
    count_seasons = serializers.SerializerMethodField()

    class Meta:
        model = TVSeries
        fields = ("id", "title", "rating", "poster_horizontal_with_text", "count_seasons")

    @staticmethod
    def get_count_seasons(instance):
        return len(SeasonTVSeries.objects.filter(tvseries=instance))


class DetailTVSeriesSerializer(serializers.ModelSerializer):
    ageLimit = serializers.SlugRelatedField(slug_field="title", queryset=AgeLimit.objects.all())
    genres = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    seasons = serializers.SerializerMethodField()
    directors = PersonSerializer(read_only=True, many=True)
    actors = PersonSerializer(read_only=True, many=True)

    class Meta:
        model = TVSeries
        fields = (
            "id", "title", "title_image", "description", "genres", "country", "ageLimit", "seasons", "directors", "actors"
        )

    @staticmethod
    def get_genres(instance):
        return get_genre_list(instance)

    @staticmethod
    def get_country(instance):
        return get_country_list(instance)

    @staticmethod
    def get_seasons(instance):
        seasons = {}
        for season in SeasonTVSeries.objects.filter(tvseries=instance):
            seasons[season.number] = SeriesTVSeriesSerializer(
                SeriesTVSeries.objects.filter(season_tvseries=season), many=True).data
        return seasons
