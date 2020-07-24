from django.contrib import admin
from . import models


@admin.register(models.Shoes)
class ShoesAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Custom Profile", {"fields": ("_id", "brand", "product", "item_url",)},),
    )

