from django.urls import path, include
from . import views as tops_views

app_name = "tops"

urlpatterns = [
    path("<int:id>", tops_views.detail_tops),
    path("similarity/", tops_views.similarity),
]
