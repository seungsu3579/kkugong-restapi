from django.urls import path, include
from . import views as scenraio_views

app_name = "scenario"

urlpatterns = [
    path("step1/", scenraio_views.step1),
    path("step2/", scenraio_views.step2),
]
