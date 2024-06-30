from django.contrib import admin

from announcement.models import Adt, Review


@admin.register(Adt)
class AdtAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "price",
        "author",
        "created_at",
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "author",
        "ad",
        "created_at",
    )
