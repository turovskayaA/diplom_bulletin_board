from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class UserManager(BaseUserManager):
    """
    Кастомный менеджер
    """

    def create_user(
        self, email, first_name, last_name, phone, password=None, **extra_fields
    ):
        """
        Функция создания пользователя — в нее мы передаем обязательные поля
        """
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role="user",
            **extra_fields,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self, email, first_name, last_name, password=None, **extra_fields
    ):
        """
         Функция для создания суперпользователя — с ее помощью мы создаем администратора
        это можно сделать с помощью команды createsuperuser
        """

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            role="admin",
            **extra_fields,
        )
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserRoles(models.TextChoices):
    USER = "user"
    ADMIN = "admin"


class User(AbstractBaseUser):

    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    avatar = models.ImageField(upload_to="users/", verbose_name="Аватар", **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name="Телефон")
    role = models.CharField(
        max_length=50,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name="Роль",
        **NULLABLE,
    )
    is_active = models.BooleanField(default=True, verbose_name="Активно", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone", "role"]

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
