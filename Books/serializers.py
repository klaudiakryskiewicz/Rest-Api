from rest_framework import serializers

from .models import Book, Author, Category


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model
    """

    def to_representation(self, value):
        return value.name

    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model
    """

    def to_representation(self, value):
        return value.name

    class Meta:
        model = Category
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model, used in a detail view
    """
    categories = CategorySerializer(many=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('title', 'authors', 'published_date', 'categories', 'average_rating', 'ratings_count', 'thumbnail')


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model, used in a list view
    """

    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('title', 'authors', 'published_date')
