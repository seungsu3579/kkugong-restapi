from django.shortcuts import render
from rest_framework.decorators import api_view

import base64
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from config import settings
from users.models import User
from tops.models import UserTops, Tops, TopsImage
from pants.models import UserPants, Pants, PantsImage
from shoes.models import UserShoes, Shoes, ShoesImage
from cody.models import Cody

from cody.serializers import CodySerializer, CodyRecommendSerializer
from tops.serializers import UserTopsSerializer, TopsSerializer
from pants.serializers import UserPantsSerializer, PantsSerializer
from shoes.serializers import UserShoesSerializer, ShoesImageSerializer

from vectorization.message import Message

# Create your views here.
@api_view(["GET"])
def recommend_item(request):
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

    item_recommend_ms = Message(
        settings.ITEM_RECOMMENDER_HOST, settings.ITEM_RECOMMENDER_PORT
    )
    recommend_items = item_recommend_ms.recommend_item(
        json.dumps(user_dict).encode("utf-8")
    )

    recommend_item_infos = []
    for item in recommend_items:
        tmp = dict()
        obj = None
        if item[0][3] == "1":
            tmp["img"] = TopsImage.objects.get(id=item[0])
            obj = Tops.objects.get(id=tmp["img"].top_id)
        elif item[0][3] == "2":
            tmp["img"] = PantsImage.objects.get(id=item[0])
            obj = Pants.objects.get(id=tmp["img"].pants_id)
        elif item[0][3] == "3":
            tmp["img"] = ShoesImage.objects.get(id=item[0])
            obj = Shoes.objects.get(id=tmp["img"].shoes_id)

        tmp["img"] = tmp["img"].img.url
        tmp["id"] = obj.id
        tmp["brand"] = obj.brand
        tmp["product"] = obj.product
        tmp["category"] = obj.category
        tmp["shop"] = obj.shop
        tmp["item_url"] = obj.item_url

        tmp["item_cody"] = []
        for cody_id in item[1]:
            cody = Cody.objects.get(id=int(cody_id))
            tmp["item_cody"].append(cody.img.url)

        recommend_item_infos.append(tmp)

    return JsonResponse(
        recommend_item_infos, safe=False, json_dumps_params={"ensure_ascii": False}
    )
    # except:
    #     pass
    # return Response(status=status.HTTP_400_BAD_REQUEST)

