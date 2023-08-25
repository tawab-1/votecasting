from rest_framework.viewsets import ModelViewSet
from users.api.v1.serializers import UserSerializer, UserRegistrationSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from users.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

class UserRegistrationView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class LoginViewSet(ViewSet):
    serializer_class = LoginSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_serializer = UserSerializer(user)
        return Response({"user": user_serializer.data}, status=status.HTTP_201_CREATED)