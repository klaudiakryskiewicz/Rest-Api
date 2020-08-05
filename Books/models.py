from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)


class Category(models.Model):
    name = models.CharField(max_length=300)


class Book(models.Model):
    title = models.CharField(max_length=120)
    authors = models.ManyToManyField(Author)
    published_date = models.IntegerField()
    categories = models.ManyToManyField(Category)
    average_rating = models.IntegerField(null=True)
    ratings_count = models.IntegerField(null=True)
    thumbnail = models.CharField(max_length=300)
