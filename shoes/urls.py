from django.urls import path, include
from . import views as shoes_views

app_name = "shoes"

urlpatterns = [
    path("<int:_id>", shoes_views.detail_shoes),
    path("similarity/", shoes_views.similarity),
]
