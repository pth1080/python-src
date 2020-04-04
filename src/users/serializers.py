from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from src.users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=User.objects.all(), message="Email existed")])
    username = serializers.CharField(trim_whitespace=True, max_length=128, required=True,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="Username existed")])
    password = serializers.CharField(trim_whitespace=True, required=True, max_length=128)

    class Meta:
        model = User
        fields = '__all__'
