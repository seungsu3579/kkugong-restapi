import numpy as np
import json
import base64

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from config import settings
from users.models import User
from tops.models import UserTops
from pants.models import UserPants
from shoes.models import UserShoes
from .models import Cody

from .serializers import CodySerializer, CodyRecommendSerializer
from tops.serializers import UserTopsSerializer
from pants.serializers import UserPantsSerializer
from shoes.serializers import UserShoesSerializer

from vectorization.message import Message


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def cody_recommend_tops(request, id):
    usertop = UserTops.objects.get(id=id)
    bit_vector = usertop.vector
    vector = np.frombuffer(bit_vector, dtype=np.float32).reshape(1, 64)
    vector_for_recommend = np.append(vector, np.float32(0)).reshape(1, 65)

    ib_cody_recommend_ms = Message(
        settings.ITEMBASE_CODY_RECOMMENDER_HOST, settings.ITEMBASE_CODY_RECOMMENDER_PORT
    )

    recommends = ib_cody_recommend_ms.recommand(vector_for_recommend.tostring())
    items = Cody.objects.filter(id__in=recommends)
    cody_serializer = CodySerializer(items, many=True)
    return Response(cody_serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def cody_recommend_pants(request, id):
    userpants = UserTops.objects.get(id=id)
    bit_vector = userpants.vector
    vector = np.frombuffer(bit_vector, dtype=np.float32).reshape(1, 64)
    vector_for_recommend = np.append(vector, np.float32(1)).reshape(1, 65)

    ib_cody_recommend_ms = Message(
        settings.ITEMBASE_CODY_RECOMMENDER_HOST, settings.ITEMBASE_CODY_RECOMMENDER_PORT
    )

    recommends = ib_cody_recommend_ms.recommand(vector_for_recommend.tostring())
    items = Cody.objects.filter(id__in=recommends)
    cody_serializer = CodySerializer(items, many=True)
    return Response(cody_serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def cody_recommend_shoes(request, id):
    usershoes = UserTops.objects.get(id=id)
    bit_vector = usershoes.vector
    vector = np.frombuffer(bit_vector, dtype=np.float32).reshape(1, 64)
    vector_for_recommend = np.append(vector, np.float32(2)).reshape(1, 65)

    ib_cody_recommend_ms = Message(
        settings.ITEMBASE_CODY_RECOMMENDER_HOST, settings.ITEMBASE_CODY_RECOMMENDER_PORT
    )

    recommends = ib_cody_recommend_ms.recommand(vector_for_recommend.tostring())
    items = Cody.objects.filter(id__in=recommends)
    cody_serializer = CodySerializer(items, many=True)
    return Response(cody_serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def cody_recommend_all(request):
    user = User.objects.get(username=request.user)
    userTops_serializer = UserTopsSerializer(user.userTops.all(), many=True)
    userPants_serializer = UserPantsSerializer(user.userPants.all(), many=True)
    userShoes_serializer = UserShoesSerializer(user.userShoes.all(), many=True)

    tops_list = list()
    for obj in userTops_serializer.data:
        sub_dict = dict()
        sub_dict["id"] = obj.get("id")
        usertops = UserTops.objects.get(id=sub_dict["id"])
        sub_dict["vector"] = base64.b64encode(usertops.vector).decode("ascii")

        # sub_dict["vector"] = np.frombuffer(usertops.vector, dtype=np.float32).reshape(
        #     1, 64
        # )
        tops_list.append(sub_dict)

    pants_list = list()
    for obj in userPants_serializer.data:
        sub_dict = dict()
        sub_dict["id"] = obj.get("id")
        userpants = UserPants.objects.get(id=sub_dict["id"])
        sub_dict["vector"] = base64.b64encode(userpants.vector).decode("ascii")

        # sub_dict["vector"] = np.frombuffer(userpants.vector, dtype=np.float32).reshape(
        #     1, 64
        # )
        pants_list.append(sub_dict)

    shoes_list = list()
    for obj in userShoes_serializer.data:
        sub_dict = dict()
        sub_dict["id"] = obj.get("id")
        usershoes = UserShoes.objects.get(id=sub_dict["id"])
        sub_dict["vector"] = base64.b64encode(usershoes.vector).decode("ascii")

        # sub_dict["vector"] = np.frombuffer(usershoes.vector, dtype=np.float32).reshape(
        #     1, 64
        # )
        shoes_list.append(sub_dict)

    user_dict = {
        "userTops": tops_list,
        "userPants": shoes_list,
        "userShoes": shoes_list,
    }

    try:

        cody_recommend_ms = Message(
            settings.CODY_RECOMMENDER_HOST, settings.CODY_RECOMMENDER_PORT
        )
        recommend_cody = cody_recommend_ms.recommend_cody(
            json.dumps(user_dict).encode("utf-8")
        )
        recommend_cody_detail = []
        for cody in recommend_cody:
            tmp = dict()
            cody_obj = Cody.objects.get(id=cody[0])
            tmp["id"] = cody_obj.id
            tmp["img"] = cody_obj.img.url
            tmp["jjim"] = cody_obj.jjim
            tmp["tops"] = UserTops.objects.get(id=cody[1]).img.url
            tmp["pants"] = UserPants.objects.get(id=cody[2]).img.url
            tmp["shoes"] = UserShoes.objects.get(id=cody[3]).img.url
            recommend_cody_detail.append(tmp)

        return JsonResponse(
            recommend_cody_detail, safe=False, json_dumps_params={"ensure_ascii": False}
        )

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)
