from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PantsSerializer
from .models import Pants


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def detail_pants(request, _id):
    try:
        pants = Pants.objects.get(_id=_id)
        return Response(data=PantsSerializer(pants).data)
    except Pants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def similarity(request):
    print("after model made")
    return Response()


class UserPantsView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = PantsSerializer(user.pants.all(), many=True)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        data_id = request.data.get("id")
        if data_id is not None:
            try:
                pants = Pants.objects.get(id=data_id)
                if pants in user.pants.all():
                    user.pants.remove(pants)
                else:
                    user.pants.add(pants)
                return Response()
            except Pants.DoesNotExist:
                pass
        return Response(status=status.HTTP_404_NOT_FOUND)
