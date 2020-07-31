from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import TopsSerializer
from .models import Tops


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def detail_tops(request, _id):
    try:
        tops = Tops.objects.get(_id=_id)
        return Response(data=TopsSerializer(tops).data)
    except Tops.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def similarity(request):
    print("after model made")
    return Response()


class UserTopsView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = TopsSerializer(user.tops.all(), many=True)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        data_id = request.data.get("id")
        if data_id is not None:
            try:
                tops = Tops.objects.get(id=data_id)
                if tops in user.tops.all():
                    user.tops.remove(tops)
                else:
                    user.tops.add(tops)
                return Response()
            except Tops.DoesNotExist:
                pass
        return Response(status=status.HTTP_404_NOT_FOUND)
