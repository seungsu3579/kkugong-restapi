from django.urls import path, include
from . import views as pants_views

app_name = "pants"

urlpatterns = [
    path("<int:id>", pants_views.detail_pants),
    path("recognition/", pants_views.recognition),
]
