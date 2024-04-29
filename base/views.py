from django.shortcuts import render

from .serializer import ContactSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


def home(request):
    return render(request, "main.html")


class ContactView(APIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        message = request.data.get('message')

        if not name or not email or not phone or not message:
            return Response({'error': 'Please fill all your details'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
