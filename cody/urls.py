from django.urls import path
from . import views

app_name = "cody"

urlpatterns = [
    path("recommend/all/", views.cody_recommend_all),
    path("recommend/tops/<int:id>/", views.cody_recommend_tops),
    path("recommend/pants/<int:id>/", views.cody_recommend_pants),
    path("recommend/shoes/<int:id>/", views.cody_recommend_shoes),
    path("detail", views.cody_detail),
]
