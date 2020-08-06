import pytest

from Books.models import Author, Category, Book
from faker import Faker

faker = Faker("pl_PL")


@pytest.mark.django_db
def test_book_create():
    Book.objects.get_or_create(
        title=faker.file_name(),
        published_date=faker.year(),
        average_rating=faker.pyfloat(),
        ratings_count=faker.pyint(),
        thumbnail=faker.url(),
    )
    assert Book.objects.count() == 1


@pytest.mark.django_db
def test_author_create():
    Author.objects.get_or_create(name=faker.name())
    assert Author.objects.count() == 1


@pytest.mark.django_db
def test_category_create():
    Category.objects.get_or_create(name=faker.file_name())
    assert Category.objects.count() == 1
