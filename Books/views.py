import json
import urllib.request

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from Books.models import Book, Author, Category
from Books.serializers import BookSerializer, BookDetailSerializer, DatabaseSerializer


class BookListView(generics.ListAPIView):
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

    def get(self, request, id):
        book = get_object_or_404(Book, pk=id)
        serializer = BookDetailSerializer(book)

        return Response(serializer.data)


class DatabaseImport(APIView):

    def post(self, request):
        serializer = DatabaseSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        query = serializer.data["q"]

        with urllib.request.urlopen(f"https://www.googleapis.com/books/v1/volumes?q={query}") as url:
            data = json.loads(url.read().decode())
            print(data)
            for book, book_item in zip(Book.objects.all(), data['items']):
                book.title = book_item['volumeInfo'].get('title')
                book.published_date = int(book_item['volumeInfo'].get('publishedDate')[:4])
                book.average_rating = book_item['volumeInfo'].get('averageRating', None)
                book.ratings_count = book_item['volumeInfo'].get('ratingsCount', None)
                book.thumbnail = book_item['volumeInfo']['imageLinks'].get('thumbnail')
                author_list = book_item['volumeInfo'].get('authors')
                category_list = book_item['volumeInfo'].get('categories')
                book.categories.clear()
                book.authors.clear()

                for name in author_list:
                    name = name.strip()
                    author, created = Author.objects.get_or_create(name=name)
                    book.authors.add(author)
                if category_list:
                    for name in category_list:
                        name = name.strip()
                        category, created = Category.objects.get_or_create(name=name)
                        book.categories.add(category)
                book.save()
        return Response("Database updated")
