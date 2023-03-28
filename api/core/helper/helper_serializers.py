def get_genre_list(instance):
    return [genre.title for genre in instance.genres.get_queryset()]


def get_country_list(instance):
    return [country.title for country in instance.country.get_queryset()]
