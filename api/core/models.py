from django.contrib.auth.models import User
from django.db import models


# ======{ Профиль }======
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, default=None)

    def __str__(self):
        return self.user.username


# ======{ Персона (Актер, Режиссер...) }======

class Person(models.Model):
    lastname = models.CharField(max_length=32, blank=True, null=True, default=None)
    username = models.CharField(max_length=32)
    pastname = models.CharField(max_length=32, blank=True, null=True, default=None)
    image = models.ImageField(null=True, blank=True, default=None)

    def __str__(self):
        name = self.username
        if self.lastname is not None:
            name = f"{self.lastname} {name}"
        if self.pastname is not None:
            name = f"{name} {self.pastname}"
        return name


class Career(models.Model):
    title = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.title


class PersonToCareer(models.Model):
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)
    career = models.ForeignKey(to=Career, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person} - {self.career}"

