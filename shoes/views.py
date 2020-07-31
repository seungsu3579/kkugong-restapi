from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShoesSerializer
from .models import Shoes


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def detail_shoes(request, _id):
    try:
        shoes = Shoes.objects.get(_id=_id)
        return Response(data=ShoesSerializer(shoes).data)
    except Shoes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def similarity(request):
    print("after model made")
    return Response()


class UserShoesView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = ShoesSerializer(user.shoes.all(), many=True)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        data_id = request.data.get("id")
        if data_id is not None:
            try:
                shoes = Shoes.objects.get(id=data_id)
                if shoes in user.shoes.all():
                    user.shoes.remove(shoes)
                else:
                    user.shoes.add(shoes)
                return Response()
            except Shoes.DoesNotExist:
                pass
        return Response(status=status.HTTP_404_NOT_FOUND)
