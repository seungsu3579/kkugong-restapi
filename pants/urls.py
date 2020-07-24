from django.urls import path, include
from . import views as pants_views

urlpatterns = [
    path("<int:_id>", pants_views.detail_pants),
]
