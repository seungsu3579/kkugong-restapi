from django.shortcuts import render
from rest_framework.decorators import api_view
from users.models import User


@api_view(["GET"])
def cody_recommend_tops(request, id):
    # 내 옷으로 만들수 있는 코디 리스트
    print(request)
    print(dir(request))
    # return 코디이미지 url


@api_view(["GET"])
def cody_recommend_pants(request, id):
    # 내 옷으로 만들수 있는 코디 리스트
    print(request)
    print(dir(request))
    # return 코디이미지 url


@api_view(["GET"])
def cody_recommend_shoes(request, id):
    # 내 옷으로 만들수 있는 코디 리스트
    print(request)
    print(dir(request))
    # return 코디이미지 url


@api_view(["GET"])
def cody_recommend_all(request):
    # 내 옷으로 만들수 있는 코디 리스트
    print(request)
    print(dir(request))

    pass


@api_view(["GET"])
def cody_detail(request):
    # 코디 아이디를 받아 top,pants,shoes 리스트 반환
    cody_id = request.data.get("cody_id")

    pass

