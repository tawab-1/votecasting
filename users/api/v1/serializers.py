from rest_framework import serializers
from users.models import User
from django.db.models import Q
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'identity_card', 'area_code', 'password', 'role',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'area_code', 'identity_card', 'role']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username:
            obj = User.objects.filter(Q(email=username) | Q(identity_card=username) | Q(area_code=username)).first()
            if obj:
                username = obj.username
        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = 'unable to login with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')

            attrs['user'] = user
            return attrs

