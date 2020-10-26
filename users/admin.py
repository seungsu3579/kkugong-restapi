from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {"fields": ("gender", "birthday", "name")},),
    )


# "tops",
# "pants",
# "shoes",
