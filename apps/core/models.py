# from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username

    def new_user(self, first_name, last_name, username, email, password):
        pass
