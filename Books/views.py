import json
import urllib.request

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from Books.models import Book
from Books.serializers import BookSerializer


class BookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
