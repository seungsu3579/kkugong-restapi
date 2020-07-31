from django.urls import path
from . import views
from pants import views as pants_views
from shoes import views as shoes_views
from tops import views as tops_views

app_name = "users"

urlpatterns = [
    path("", views.create_account),
    path("my/", views.UserMyView.as_view()),
    path("login/", views.login),
    path("my/tops/", tops_views.UserTopsView.as_view()),
    path("my/pants/", pants_views.UserPantsView.as_view()),
    path("my/shoes/", shoes_views.UserShoesView.as_view()),
]
