# Rest-Api
Na podstawie danych znajdującej się na stronie https://www.googleapis.com/books/v1/volumes?q=Hobbit zaprojektować i stworzyć aplikację w wybranym przez siebie frameworku, która będzie posiadała proste REST API:

GET /books - lista wszystkich książek (widok powinien pozwalać na filtrowanie i sortowanie po roku przykład : /books?published_date=1995, /books?sort=-published_date)
GET /books?author="Jan Kowalski"&author="Anna Kowalska" - lista książek zadanych autorów
GET /books/<bookId> - wybrana książka 
{
    "title": "Hobbit czyli Tam i z powrotem",
    "authors": ["J. R. R. Tolkien"],
    "published_date": "2004",
    "categories": [
        "Baggins, Bilbo (Fictitious character)"
      ],
    "average_rating": 5,
    "ratings_count": 2,
    "thumbnail": "http://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
}

POST /db z body {"q": "war"}
ściągnąć data set z https://www.googleapis.com/books/v1/volumes?q=war
wrzucić do bazy danych wpisy (aktualizując już istniejące)


Wysyłając zgłoszenie prześlij nam:
repozytorium z kodem twojego rozwiązania (github, gitlab, bitbucket, …)
link do działającej aplikacji (pythonanywhere, heroku, …)
Oceniając zgłoszenia zwracamy przede wszystkim uwagę na dobre praktyki związane w web developmentem w Pythonie oraz znajomość zastosowanych bibliotek. Wizualne elementy frontendu (jeśli takowy jest elementem rozwiązania) nie są oceniane.
