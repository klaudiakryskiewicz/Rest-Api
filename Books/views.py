import json
import urllib.request

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView

from Books.forms import BookImportForm
from Books.models import Book, Author, Category
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

    def get(self, request):
        form = BookImportForm
        return render(request, 'import.html', {'form': form})

    def post(self, request):
        query = request.POST['query']
        for book in Book.objects.all():
            book.delete()
        with urllib.request.urlopen(f"https://www.googleapis.com/books/v1/volumes?q={query}") as url:
            data = json.loads(url.read().decode())
            print(data)
            k = {}
            for book_item in data['items']:
                k['title'] = book_item['volumeInfo'].get('title')
                k['published_date'] = int(book_item['volumeInfo'].get('publishedDate')[:4])
                k['average_rating'] = book_item['volumeInfo'].get('averageRating', None)
                k['ratings_count'] = book_item['volumeInfo'].get('ratingsCount', None)
                k['thumbnail'] = book_item['volumeInfo']['imageLinks'].get('thumbnail')
                book, created = Book.objects.get_or_create(**k)
                author_list = book_item['volumeInfo'].get('authors')
                category_list = book_item['volumeInfo'].get('categories')

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
        return redirect(reverse_lazy('list'))
