from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class Welcome(APIView):

    def get(self, request):
        response = {
            'message': 'Welcome to the BEON Python/Django Challenge'
        }
        return Response(response, status=status.HTTP_200_OK)
