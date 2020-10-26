import os
from PIL import Image
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShoesSerializer, UserShoesSerializer, ShoesImageSerializer
from .models import Shoes, UserShoes, ShoesImage
from .form import ShoesUploadFileForm
from config import settings
from vectorization.message import Message


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def detail_shoes(request, id):
    try:
        shoes = Shoes.objects.get(id=id)
        return Response(data=ShoesSerializer(shoes).data)
    except Shoes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def detail_userTops(request, id):
    try:
        shoes = UserShoes.objects.get(id=id)
        return Response(data=UserShoesSerializer(shoes).data)
    except Shoes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def recognition(request):
    user = request.user
    form = ShoesUploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        shoes_obj = form.save()
        img_dir = str(shoes_obj.img)
        # img_dir = settings.MEDIA_ROOT + "/" + str(shoes_obj.img)
        if img_dir[-3:] != "jpg":
            tmp_img = Image.open(img_dir).convert("RGB")
            img_extension = img_dir[-3:]

            img_dir = img_dir[:-3] + "jpg"
            tmp_img.save(img_dir)
            os.remove(img_dir[:-3] + img_extension)
            shoes_obj.img = str(shoes_obj.img)[:-3] + "jpg"

        # set shoes recognition server
        vector_ms = Message(
            settings.SHOES_VECTORIZATION_HOST, settings.SHOES_VECTORIZATION_PORT
        )
        bit_vector = vector_ms.imgToBit(img_dir)

        if bit_vector == b"":
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            recommand_ms = Message(
                settings.SHOES_RECOGNITION_HOST, settings.SHOES_RECOGNITION_PORT
            )
            recommands = recommand_ms.recommand(bit_vector)

            items = ShoesImage.objects.filter(id__in=recommands)

        shoesImage_serializer = ShoesImageSerializer(items, many=True)

        shoes_obj.user = user
        shoes_obj.vector = bit_vector
        shoes_obj.save()

        userShoes_serializer = UserShoesSerializer(shoes_obj)

        new_dict = {
            "userShoes_obj": userShoes_serializer.data,
            "similar_things": shoesImage_serializer.data,
        }

        return Response(new_dict)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class UserShoesView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserShoesSerializer(user.userShoes.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        # request : {
        #     "userShoes_obj" : { return of id user shoes obj },
        #     "save_img" : { image that show on the app },
        #     "save_vector" : { image that representative vector },
        # }

        userShoes_id = request.data.get("userShoes_obj")
        userShoes = UserShoes.objects.get(id=userShoes_id)
        userShoes.img = request.data.get("save_img")
        userShoes.nickname = request.data.get("cloth_nickname")

        save_vector = request.data.get("save_vector")
        if userShoes is not None:
            if save_vector is None:
                pass
            else:
                similar_img = ShoesImage.objects.get(id=save_vector)
                userShoes.meta_shoes = similar_img.shoes
                userShoes.vector = similar_img.vector
            userShoes.save()
            serializer = UserShoesSerializer(userShoes)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        user = request.user
        data_id = request.data.get("id")
        if data_id is not None:
            try:
                shoes = UserShoes.objects.get(id=data_id)
                if shoes in user.userShoes.all():
                    user.userShoes.remove(shoes)
                else:
                    user.userShoes.add(shoes)
                return Response(status=status.HTTP_200_OK)
            except UserShoes.DoesNotExist:
                pass
        return Response(status=status.HTTP_404_NOT_FOUND)
