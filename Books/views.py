from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView

from Books.models import Book
from Books.serializers import BookSerializer, BookDetailSerializer


class BookView(generics.ListAPIView):
    """
    API displaying a list of all books,
    allowing to filter and sort result by published date and filter by author name.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['published_date']
    filterset_fields = ['published_date', 'authors']


class BookDetails(APIView):
    """
    API displaying details of a single book
    """

    def get_object(self, id):
        """
        function checking if database contains book with certain id,
        and returning wanted object
        """
        try:
            return Book.objects.get(pk=id)
        except Book.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        book = self.get_object(id)
        serializer = BookDetailSerializer(book)

        return Response(serializer.data)


class DatabaseImport(APIView):
    pass
