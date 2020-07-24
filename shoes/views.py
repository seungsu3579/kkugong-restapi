from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ShoesSerializer
from .models import Shoes


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def detail_shoes(self, request, _id):
    try:
        shoes = Shoes.objects.get(_id=_id)
        return Response(data=ShoesSerializer(shoes).data)
    except Shoes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
