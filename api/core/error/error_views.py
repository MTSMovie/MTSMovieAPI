from .error import ErrorHelper


class MovieError(ErrorHelper):
    def is_not_found(self):
        return self.get_error(error="Такого фильма не существует", status=self.NOT_FOUND)


class TVSeriesError(ErrorHelper):
    def is_not_found(self):
        return self.get_error(error="Такого сериала не существует", status=self.NOT_FOUND)
