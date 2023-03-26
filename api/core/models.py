from django.contrib.auth.models import User
from django.db import models


# ======{ Профиль }======
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, default=None)

    def __str__(self):
        return self.user.username

