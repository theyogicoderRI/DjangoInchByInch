from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()