# import json
#
# from django.core.management.base import BaseCommand
#
#
# import urllib.request
#
# from Books.models import Book, Author, Category
#
#
# class Command(BaseCommand):
#     """
#     store movies data from provided dump
#     """
#     def handle(self, *args, **options):
#         with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=Hobbit") as url:
#             data = json.loads(url.read().decode())
#             print(data)
#             k = {}
#             for book_item in data['items']:
#                 k['title'] = book_item.get('title')
#                 k['published_date'] = book_item['volumeInfo'].get('published_date')
#                 k['average_rating'] = book_item['volumeInfo'].get('average_rating')
#                 k['ratings_count'] = book_item['volumeInfo'].get('ratings_count')
#                 k['thumbnail'] = book_item['imageLinks'].get('thumbnail')
#                 book, created = Book.objects.get_or_create(**k)
#                 author_list = book_item['volumeInfo'].get('authors')
#                 category_list = book_item['volumeInfo'].get('categories')
#
#                 for name in author_list:
#                     name = name.strip()
#                     author, created = Author.objects.get_or_create(name=name)
#                     book.authors.add(author)
#                 for name in category_list:
#                     name = name.strip()
#                     category, created = Category.objects.get_or_create(name=name)
#                     book.categories.add(category)
#                 book.save()
#                 print(book)
