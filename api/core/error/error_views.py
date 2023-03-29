from .error import ErrorHelper


class MovieError(ErrorHelper):
    def is_not_found(self):
        return self.get_error(error="Такого фильма не существует", status=self.NOT_FOUND)


class TVSeriesError(ErrorHelper):
    def is_not_found(self):
        return self.get_error(error="Такого сериала не существует", status=self.NOT_FOUND)

    def season_not_found(self):
        return self.get_error(error="Такого сезона не существует", status=self.NOT_FOUND)

    def series_not_found(self):
        return self.get_error(error="Такой серии не существует", status=self.NOT_FOUND)
