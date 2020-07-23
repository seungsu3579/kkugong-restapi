from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib.auth import authenticate
from .serializers import UserSerializer
import jwt


class UserMyView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(instance=request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # authenticate user
    user = authenticate(username=username, password=password)

    if user is not None:
        user_info = {
            "pk": user.pk,
        }
        encoded_jwt = jwt.encode(user_info, settings.SECRET_KEY, algorithm="HS256")
        return Response(data={"token": encoded_jwt})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

