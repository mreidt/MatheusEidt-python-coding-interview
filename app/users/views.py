from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from app.users.serializers import UserSerializer


class ListUsers(APIView):
    serializer_class = UserSerializer
    model = get_user_model()

    def get(self, request):
        serializer = self.serializer_class(self.model.objects.all(), many=True)
        return Response(data=serializer.data)
