import os
from PIL import Image
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import TopsSerializer, UserTopsSerializer, TopImageSerializer
from .models import Tops, UserTops, TopsImage
from .form import TopUploadFileForm
from config import settings
from vectorization.message import Message
import numpy as np


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def detail_tops(request, id):
    try:
        tops = Tops.objects.get(id=id)
        return Response(data=TopsSerializer(tops).data)
    except Tops.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def detail_userTops(request, id):
    try:
        tops = UserTops.objects.get(id=id)
        return Response(data=UserTopsSerializer(tops).data)
    except Tops.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def recognition(request):
    user = request.user
    form = TopUploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        top_obj = form.save()
        img_dir = str(top_obj.img)
        # img_dir = settings.MEDIA_ROOT + "/" + str(top_obj.img)
        # change image file format
        if img_dir[-3:] != "jpg":
            tmp_img = Image.open(img_dir).convert("RGB")
            img_extension = img_dir[-3:]

            img_dir = img_dir[:-3] + "jpg"
            tmp_img.save(img_dir)
            os.remove(img_dir[:-3] + img_extension)
            top_obj.img = str(top_obj.img)[:-3] + "jpg"

        vector_ms = Message(
            settings.TOP_VECTORIZATION_HOST, settings.TOP_VECTORIZATION_PORT
        )
        bit_vector = vector_ms.imgToBit(img_dir)

        vector_for_recommend = vector_ms.bitToVector(bit_vector)
        vector_for_recommend = np.append(vector_for_recommend, np.float32(0)).reshape(
            1, 65
        )

        if bit_vector == b"":
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            recommand_ms = Message(settings.RECOGNITION_HOST, settings.RECOGNITION_PORT)
            recommands = recommand_ms.recommand(vector_for_recommend.tostring())

            items = TopsImage.objects.filter(id__in=recommands)

        topImage_serializer = TopImageSerializer(items, many=True)

        top_obj.user = user
        top_obj.vector = bit_vector
        top_obj.save()

        userTop_serializer = UserTopsSerializer(top_obj)

        new_dict = {
            "userTop_obj": userTop_serializer.data,
            "similar_things": topImage_serializer.data,
        }

        return Response(new_dict)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class UserTopsView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserTopsSerializer(user.userTops.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        # request : {
        #     "userTop_obj" : { return of id user top obj },
        #     "save_img" : { image that show on the app },
        #     "save_vector" : { image that representative vector },
        # }

        userTop_id = request.data.get("userTop_obj")
        userTop = UserTops.objects.get(id=userTop_id)
        userTop.img = request.data.get("save_img")
        userTop.nickname = request.data.get("cloth_nickname")

        save_vector = request.data.get("save_vector")
        if userTop is not None:
            if save_vector is None:
                pass
            else:
                similar_img = TopsImage.objects.get(id=save_vector)
                userTop.meta_top = similar_img.top
                userTop.vector = similar_img.vector
            userTop.save()
            serializer = UserTopsSerializer(userTop)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        user = request.user
        data_id = request.data.get("id")
        if data_id is not None:
            try:
                tops = UserTops.objects.get(id=data_id)
                if tops in user.userTops.all():
                    user.userTops.remove(tops)
                else:
                    user.userTops.add(tops)
                return Response(status=status.HTTP_200_OK)
            except UserTops.DoesNotExist:
                pass
        return Response(status=status.HTTP_404_NOT_FOUND)
