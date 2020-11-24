import os
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from config import settings
from vectorization.message import Message
import numpy as np


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def step1(request):
    data = {
        "userTop_obj": {
            "id": 15,
            "nickname": "top",
            "user": 2,
            "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/userTop/user1_top.jpg",
            "meta_top": None,
            "jjim": False,
        },
        "similar_things": [
            {
                "id": "150100000000_1",
                "img_url": "https://cdn-images.farfetch-contents.com/15/28/83/44/15288344_27690991_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100001651_1.jpg",
                "top": "130100001651",
            },
            {
                "id": "130100006885_1",
                "img_url": "https://cdn-images.farfetch-contents.com/14/77/23/46/14772346_23714791_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100006885_1.jpg",
                "top": "130100006885",
            },
            {
                "id": "130100007081_1",
                "img_url": "https://cdn-images.farfetch-contents.com/14/82/70/31/14827031_24333536_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100007081_1.jpg",
                "top": "130100007081",
            },
            {
                "id": "130100007256_1",
                "img_url": "https://cdn-images.farfetch-contents.com/14/76/66/49/14766649_23901152_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100007256_1.jpg",
                "top": "130100007256",
            },
            {
                "id": "130100008482_1",
                "img_url": "https://cdn-images.farfetch-contents.com/14/44/26/64/14442664_21283558_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100008482_1.jpg",
                "top": "130100008482",
            },
            {
                "id": "130100008570_1",
                "img_url": "https://cdn-images.farfetch-contents.com/14/40/06/23/14400623_21520430_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100008570_1.jpg",
                "top": "130100008570",
            },
            {
                "id": "130100010183_1",
                "img_url": "https://cdn-images.farfetch-contents.com/14/02/42/27/14024227_18198755_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100010183_1.jpg",
                "top": "130100010183",
            },
            {
                "id": "130100010191_1",
                "img_url": "https://cdn-images.farfetch-contents.com/13/43/61/13/13436113_16034944_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100010191_1.jpg",
                "top": "130100010191",
            },
            {
                "id": "130100010386_1",
                "img_url": "https://cdn-images.farfetch-contents.com/15/28/38/01/15283801_27726381_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100010386_1.jpg",
                "top": "130100010386",
            },
            {
                "id": "130100010671_1",
                "img_url": "https://cdn-images.farfetch-contents.com/13/43/94/78/13439478_15437259_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100010671_1.jpg",
                "top": "130100010671",
            },
            {
                "id": "130100010676_1",
                "img_url": "https://cdn-images.farfetch-contents.com/13/43/60/94/13436094_15426271_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100010676_1.jpg",
                "top": "130100010676",
            },
            {
                "id": "130100011179_1",
                "img_url": "https://cdn-images.farfetch-contents.com/15/42/40/03/15424003_27240006_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100011179_1.jpg",
                "top": "130100011179",
            },
            {
                "id": "130100011207_1",
                "img_url": "https://cdn-images.farfetch-contents.com/15/41/92/69/15419269_27345858_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100011207_1.jpg",
                "top": "130100011207",
            },
            {
                "id": "130100011698_1",
                "img_url": "https://cdn-images.farfetch-contents.com/15/28/21/61/15282161_27256415_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100011698_1.jpg",
                "top": "130100011698",
            },
            {
                "id": "130100011706_1",
                "img_url": "https://cdn-images.farfetch-contents.com/15/28/21/50/15282150_27357491_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100011706_1.jpg",
                "top": "130100011706",
            },
            {
                "id": "130100012558_1",
                "img_url": "https://cdn-images.farfetch-contents.com/15/21/25/70/15212570_26696881_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100012558_1.jpg",
                "top": "130100012558",
            },
            {
                "id": "130100012675_1",
                "img_url": "https://cdn-images.farfetch-contents.com/15/13/89/37/15138937_26102529_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100012675_1.jpg",
                "top": "130100012675",
            },
            {
                "id": "130100013465_1",
                "img_url": "https://cdn-images.farfetch-contents.com/14/95/04/42/14950442_24610311_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100013465_1.jpg",
                "top": "130100013465",
            },
            {
                "id": "130100014165_1",
                "img_url": "https://cdn-images.farfetch-contents.com/14/94/13/89/14941389_26629861_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100014165_1.jpg",
                "top": "130100014165",
            },
            {
                "id": "130100015180_1",
                "img_url": "https://cdn-images.farfetch-contents.com/14/42/55/23/14425523_21185433_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/130100015180_1.jpg",
                "top": "130100015180",
            },
        ],
    }

    return JsonResponse(data, safe=False, json_dumps_params={"ensure_ascii": False})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def step2(request):
    pass


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def step2(request):
    data = {
        "userTop_obj": {
            "id": 15,
            "nickname": "top",
            "user": 2,
            "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/userTop/user1_top.jpg",
            "meta_top": None,
            "jjim": False,
        },
        "similar_things": [
            {
                "id": "200100000001_1",
                "img_url": "https://cdn-images.farfetch-contents.com/15/28/83/44/15288344_27690991_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/200100000001_1.jpg",
                "top": "200100000001",
            },
            {
                "id": "200100000002_1",
                "img_url": "https://cdn-images.farfetch-contents.com/14/77/23/46/14772346_23714791_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/200100000002_1.jpg",
                "top": "200100000002",
            },
            {
                "id": "200100000003_1",
                "img_url": "https://cdn-images.farfetch-contents.com/14/82/70/31/14827031_24333536_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/200100000003_1.jpg",
                "top": "200100000003",
            },
            {
                "id": "200100000004_1",
                "img_url": "https://cdn-images.farfetch-contents.com/14/76/66/49/14766649_23901152_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/200100000004_1.jpg",
                "top": "200100000004",
            },
            {
                "id": "200100000005_1",
                "img_url": "https://cdn-images.farfetch-contents.com/14/44/26/64/14442664_21283558_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/200100000005_1.jpg",
                "top": "200100000005",
            },
            {
                "id": "200100000006_1",
                "img_url": "https://cdn-images.farfetch-contents.com/14/40/06/23/14400623_21520430_1000.jpg",
                "img": "https://dressroom-base-data.s3.ap-northeast-2.amazonaws.com/top/200100000006_1.jpg",
                "top": "200100000006",
            },
        ],
    }

    return JsonResponse(data, safe=False, json_dumps_params={"ensure_ascii": False})
