from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import \
    MiniMovieView, MovieView, DetailMovieView, \
    MiniTVSeriesView, TVSeriesView, DetailTVSeriesView

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),

    # ФИЛЬМЫ
    path("movies/", MiniMovieView.as_view({'get': 'get_movies'})),
    path("movies/<int:pk>/", MovieView.as_view({'get': 'get_detail_movie'})),
    path("movies/<int:pk>/detail/", DetailMovieView.as_view({'get': 'get_detail_movie'})),

    # СЕРИАЛЫ
    path("tvseries/", MiniTVSeriesView.as_view({'get': 'get_movies'})),
    path("tvseries/<int:pk>/", TVSeriesView.as_view({'get': 'get_detail_tvseries'})),
    path("tvseries/<int:pk>/detail/", DetailTVSeriesView.as_view({'get': 'get_detail_tvseries'})),
]
