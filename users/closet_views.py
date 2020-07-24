from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from .serializers import UserSerializer
from tops.serializers import TopsSerializer
from pants.serializers import PantsSerializer
from shoes.serializers import ShoesSerializer

from .models import User
from tops.models import Tops
from pants.models import Pants
from shoes.models import Shoes


class UserTopsView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass

    def post(self, request):
        pass

    def delete(self, request):
        pass


class UserPantsView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass

    def post(self, request):
        pass

    def delete(self, request):
        pass


class UserShoesView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass

    def post(self, request):
        pass

    def delete(self, request):
        pass
