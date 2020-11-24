from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("recommend_item/", views.recommend_item),
]
