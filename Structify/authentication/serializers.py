from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from users.models import CustomUser
import re
from django.utils import timezone

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise ValidationError("Invalid user or password")
        user.last_login = timezone.now()
        user.save()

        return {
            "user":{
                "id":user.id,
                "email":user.email
            }
        }