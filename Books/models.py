from django.db import models


class Author(models.Model):
    """
    Model for an author
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Model for a category
    """
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model for a book
    """
    title = models.CharField(max_length=120)
    authors = models.ManyToManyField(Author)
    published_date = models.IntegerField()
    categories = models.ManyToManyField(Category)
    average_rating = models.FloatField(null=True)
    ratings_count = models.IntegerField(null=True)
    thumbnail = models.URLField(max_length=300)

    def __str__(self):
        return self.title
