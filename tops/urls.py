from django.urls import path, include
from . import views as tops_views

urlpatterns = [
    path("<int:_id>", tops_views.detail_tops),
]
