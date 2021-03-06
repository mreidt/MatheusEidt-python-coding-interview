from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    birth_date = models.DateTimeField(auto_now=True)

    objects = UserManager()

    unique_fields = (email,)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_full_name(self):
        return f"{self.name} {self.last_name}"

    def __str__(self):
        return self.email

    @property
    def age(self):
        today = datetime.today()

        age = today.year - self.birth_date.year
        has_completed_birthday = (today.month, today.day) < (
            self.birth_date.month,
            self.birth_date.day,
        )
        return age - has_completed_birthday
