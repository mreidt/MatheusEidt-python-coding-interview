from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    age = serializers.ReadOnlyField()

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "name",
            "last_name",
            "email",
            "is_active",
            "is_staff",
            "is_superuser",
            "age",
        ]
