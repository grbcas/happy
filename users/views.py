from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'pk',
            'password',
            'birthday',
        )
