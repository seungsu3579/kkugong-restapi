from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("my/", views.UserMyView.as_view()),
    path("login/", views.login),
]
