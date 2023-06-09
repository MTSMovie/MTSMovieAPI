from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .error.error_views import MovieError, TVSeriesError
from .models import Movie, TVSeries, SeasonTVSeries, SeriesTVSeries
from .serializers import MovieSerializer, TVSeriesSerializer, MiniMovieSerializer, MiniTVSeriesSerializer, \
    DetailMovieSerializer, DetailTVSeriesSerializer, PlayerTVSeriesSerializer, PlayerMovieSerializer


# ===========
# ФИЛЬМЫ
# ===========
class MovieView(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [permissions.AllowAny]
    error_helper = MovieError()

    @action(methods=['get'], detail=False)
    def get_detail_movie(self, request, pk):
        qs = self.queryset.filter(pk=pk)
        if len(qs) == 0:
            return self.error_helper.is_not_found()
        return Response(
            self.serializer_class(qs[0]).data,
            status=status.HTTP_200_OK,
        )


class PlayerMovieView(viewsets.ModelViewSet):
    serializer_class = PlayerMovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [permissions.AllowAny]
    error_helper = MovieError()

    @action(methods=['get'], detail=False)
    def get_player_movie(self, request, pk):
        qs = self.queryset.filter(pk=pk)
        if len(qs) == 0:
            return self.error_helper.is_not_found()
        return Response(
            self.serializer_class(qs[0]).data,
            status=status.HTTP_200_OK,
        )


class DetailMovieView(viewsets.ModelViewSet):
    serializer_class = DetailMovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [permissions.AllowAny]
    error_helper = MovieError()

    @action(methods=['get'], detail=False)
    def get_detail_movie(self, request, pk):
        qs = self.queryset.filter(pk=pk)
        if len(qs) == 0:
            return self.error_helper.is_not_found()
        return Response(
            self.serializer_class(qs[0]).data,
            status=status.HTTP_200_OK,
        )


class MiniMovieView(viewsets.ModelViewSet):
    serializer_class = MiniMovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [permissions.AllowAny]

    @action(methods=['get'], detail=False)
    def get_movies(self, request):
        return Response(
            self.serializer_class(self.queryset, many=True).data,
            status=status.HTTP_200_OK,
        )


# ===========
# СЕРИАЛЫ
# ===========
class TVSeriesView(viewsets.ModelViewSet):
    serializer_class = TVSeriesSerializer
    queryset = TVSeries.objects.all()
    permission_classes = [permissions.AllowAny]
    error_helper = TVSeriesError()

    @action(methods=['get'], detail=False)
    def get_detail_tvseries(self, request, pk):
        qs = self.queryset.filter(pk=pk)
        if len(qs) == 0:
            return self.error_helper.is_not_found()
        return Response(
            self.serializer_class(qs[0]).data,
            status=status.HTTP_200_OK,
        )


class PlayerTVSeriesView(viewsets.ModelViewSet):
    serializer_class = PlayerTVSeriesSerializer
    queryset = TVSeries.objects.all()
    permission_classes = [permissions.AllowAny]
    error_helper = TVSeriesError()

    @action(methods=['get'], detail=False)
    def get_player_tvseries(self, request, pk, number_season, number_series):
        qs = self.queryset.filter(pk=pk)
        if len(qs) == 0:
            return self.error_helper.is_not_found()

        season_qs = SeasonTVSeries.objects.filter(tvseries=qs[0], number=number_season)
        if len(season_qs) == 0:
            return self.error_helper.season_not_found()

        series_qs = SeriesTVSeries.objects.filter(season_tvseries=season_qs[0], number=number_series)
        if len(series_qs) == 0:
            return self.error_helper.series_not_found()

        return Response(
            self.serializer_class(qs[0], context={'series': series_qs[0]}).data,
            status=status.HTTP_200_OK,
        )


class DetailTVSeriesView(viewsets.ModelViewSet):
    serializer_class = DetailTVSeriesSerializer
    queryset = TVSeries.objects.all()
    permission_classes = [permissions.AllowAny]
    error_helper = TVSeriesError()

    @action(methods=['get'], detail=False)
    def get_detail_tvseries(self, request, pk):
        qs = self.queryset.filter(pk=pk)
        if len(qs) == 0:
            return self.error_helper.is_not_found()
        return Response(
            self.serializer_class(qs[0]).data,
            status=status.HTTP_200_OK,
        )


class MiniTVSeriesView(viewsets.ModelViewSet):
    serializer_class = MiniTVSeriesSerializer
    queryset = TVSeries.objects.all()
    permission_classes = [permissions.AllowAny]

    @action(methods=['get'], detail=False)
    def get_movies(self, request):
        return Response(
            self.serializer_class(self.queryset, many=True).data,
            status=status.HTTP_200_OK,
        )
