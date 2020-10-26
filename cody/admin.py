from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Cody)
class CodyAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Custom Profile",
            {
                "fields": (
                    "id",
                    "img",
                    "jjim",
                    "cody_top_img",
                    "cody_pants_img",
                    "cody_shoes_img",
                    "form",
                )
            },
        ),
    )
