from django.urls import path, include
from . import views as shoes_views

urlpatterns = [
    path("<int:_id>", shoes_views.detail_shoes),
]
