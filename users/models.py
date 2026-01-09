from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email обязателен')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, help_text="Укажите номер телефона")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, help_text="Загрузите свой аватар")
    country = models.CharField(max_length=50, blank=True, null=True, help_text="Укажите страну")

    objects = CustomUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email





