from django.contrib import admin
from . import models


@admin.register(models.Pants)
class PantsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Custom Profile", {"fields": ("_id", "brand", "product", "item_url",)},),
    )

