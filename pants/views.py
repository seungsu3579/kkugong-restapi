from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import PantsSerializer
from .models import Pants


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def detail_pants(self, request, _id):
    try:
        pants = Pants.objects.get(_id=_id)
        return Response(data=PantsSerializer(pants).data)
    except Pants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
