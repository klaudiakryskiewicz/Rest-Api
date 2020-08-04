from rest_framework import serializers
from .models import Book, Author, Category


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model
    """

    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model
    """

    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model
    """
    categories = CategorySerializer(many=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('title', 'authors', 'published_date', 'categories', 'average_ratign', 'ratings_count', 'thumbnail')
