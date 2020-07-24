from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import TopsSerializer
from .models import Tops


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def detail_tops(self, request, _id):
    try:
        tops = Tops.objects.get(_id=_id)
        return Response(data=TopsSerializer(tops).data)
    except Tops.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
