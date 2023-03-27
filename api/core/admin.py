from django.contrib import admin

from .models import Profile, Person, Career, AgeLimit, Genre, Country, Movie


class ProfileAdmin(admin.ModelAdmin):
    pass


class PersonAdmin(admin.ModelAdmin):
    pass


class CareerAdmin(admin.ModelAdmin):
    pass


class AgeLimitAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


class CountryAdmin(admin.ModelAdmin):
    pass


class MovieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(AgeLimit, AgeLimitAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Movie, MovieAdmin)
