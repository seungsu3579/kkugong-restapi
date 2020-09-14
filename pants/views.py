import os
from PIL import Image
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import PantsSerializer, UserPantsSerializer, PantsImageSerializer
from .models import Pants, UserPants, PantsImage
from .form import PantsUploadFileForm
from config import settings
from vectorization.message import Message


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def detail_pants(request, id):
    try:
        pants = Pants.objects.get(id=id)
        return Response(data=PantsSerializer(pants).data)
    except Pants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def detail_userTops(request, id):
    try:
        pants = UserPants.objects.get(id=id)
        return Response(data=UserPantsSerializer(pants).data)
    except Pants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def recognition(request):
    user = request.user
    form = PantsUploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        pants_obj = form.save()
        img_dir = settings.MEDIA_ROOT + "/" + str(pants_obj.img)
        if img_dir[-3:] != "jpg":

            tmp_img = Image.open(img_dir).convert("RGB")
            img_extension = img_dir[-3:]

            img_dir = img_dir[:-3] + "jpg"
            tmp_img.save(img_dir)
            os.remove(img_dir[:-3] + img_extension)
            pants_obj.img = img_dir
        print(pants_obj.img)
        print(vars(pants_obj))

        # set pants recognition server
        vector_ms = Message(
            settings.PANTS_VECTORIZATION_HOST, settings.PANTS_VECTORIZATION_PORT
        )
        bit_vector = vector_ms.topToBit(img_dir)
        #

        if bit_vector == b"":
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            recommand_ms = Message(
                settings.PANTS_RECOGNITION_HOST, settings.PANTS_RECOGNITION_PORT
            )
            recommands = recommand_ms.recommand(bit_vector)

            items = PantsImage.objects.filter(id__in=recommands)

        serializer = PantsImageSerializer(items, many=True)

    return Response(serializer.data)


class UserPantsView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = PantsSerializer(user.userPants.all(), many=True)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        data_id = request.data.get("id")
        if data_id is not None:
            try:
                pants = UserPants.objects.get(id=data_id)
                if pants in user.userPants.all():
                    user.userPants.remove(pants)
                else:
                    user.userPants.add(pants)
                return Response()
            except Pants.DoesNotExist:
                pass
        return Response(status=status.HTTP_404_NOT_FOUND)
