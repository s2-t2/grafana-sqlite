from db.bookstore import createbook
from db.models import Book
import uuid

def run():
    book = Book(
        id=str(uuid.uuid4()),
        title="Call of Cthulhu",
        author="Alejandro Universe",
        description="My universal struggle with Gods")

    myBook = createbook(book)

    print(myBook)
