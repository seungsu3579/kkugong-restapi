from django.contrib import admin
from . import models


@admin.register(models.Tops)
class TopsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Custom Profile", {"fields": ("_id", "brand", "product", "item_url",)},),
    )

