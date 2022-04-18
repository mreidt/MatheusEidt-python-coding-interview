from rest_framework.views import APIView
from app.store.models import Products
from app.store.serializers import ProductsSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class ListProducts(APIView):
    serializer_class = ProductsSerializer
    model = Products

    def get(self, request):
        serializer = self.serializer_class(self.model.objects.all())
        return Response(data=serializer.data)

    def patch(self, request, pk):
        instance = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(instance)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
