from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Tops)
class TopsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Custom Profile", {"fields": ("id", "brand", "product", "item_url",)},),
    )


@admin.register(models.UserTops)
class UserTopsAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Custom Profile",
            {"fields": ("id", "nickname", "user", "img", "meta_top", "jjim",)},
        ),
    )


@admin.register(models.TopsImage)
class TopsImageAdmin(admin.ModelAdmin):

    """Tops Image Admin Definition"""

    fieldsets = (("Custom Profile", {"fields": ("id", "img_url", "img", "top",)},),)

    # list_display = ("__str__", "get_thumbnail")

    # def get_thumbnail(self, obj):
    #     return mark_safe(f'<img src="{obj.img}" width=50>')

    # get_thumbnail.short_description = "Thumbnail"
