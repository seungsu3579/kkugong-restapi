from django.urls import path
from . import views
from . import closet_views

app_name = "users"

urlpatterns = [
    path("", views.create_account),
    path("my/", views.UserMyView.as_view()),
    path("login/", views.login),
    path("my/tops/", closet_views.UserTopsView.as_view()),
    path("my/pants/", closet_views.UserPantsView.as_view()),
    path("my/shoes/", closet_views.UserShoesView.as_view()),
]
