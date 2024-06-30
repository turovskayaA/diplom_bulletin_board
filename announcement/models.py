from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Adt(models.Model):

    title = models.CharField(max_length=55, verbose_name="Название товара")
    price = models.IntegerField(verbose_name="Цена товара")
    description = models.TextField(
        max_length=100, verbose_name="Описание товара", **NULLABLE
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        **NULLABLE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время и дата создания"
    )
    image = models.ImageField(
        upload_to="announcement/", verbose_name="Изображение", **NULLABLE
    )

    def __str__(self):
        return f"{self.title}, {self.price}, {self.description}"

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Review(models.Model):

    text = models.TextField(max_length=255, verbose_name="Текст отзыва", **NULLABLE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        **NULLABLE,
    )
    ad = models.ForeignKey(Adt, on_delete=models.CASCADE, verbose_name="Объявление")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время и дата создания"
    )

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
