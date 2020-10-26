from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def recommend_item(request):
    # 추천 아이템

    pass
