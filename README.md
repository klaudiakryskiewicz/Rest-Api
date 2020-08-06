# Books - Rest-Api (STX Next recruitment task)
Application downloads books to the local PostgreSQL database, and creates api based on it. 

To save initial data to database run python manage.py populate_books

http://127.0.0.1:8000/books - list of all books, can be sorted by published date and filtered by published date and author name.

Examples:
* http://127.0.0.1:8000/books?sort=published_date
* http://127.0.0.1:8000/books?sort=-published_date
* http://127.0.0.1:8000/books?published_date=2012
* http://127.0.0.1:8000/books?author=Tolkien


App allows to update list of books: http://127.0.0.1:8000/db with body {"q":"<params>"}, 

* e.x. http://127.0.0.1:8000/db?{"q":"war"}


Code contains tests written with pytest. To run them, enter pytest in the terminal

