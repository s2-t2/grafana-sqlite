from db.models import Book
from sqlalchemy import create_engine

engine = create_engine("sqlite:///coolbooks.db")


def createbook(book):
    # create sqlite connection
    connection = engine.connect()

    insertQuery = """
    INSERT INTO book (id, title, author, description) 
    VALUES( "{}", "{}", "{}", "{}") """.format(
        book.id, book.title, book.author, book.description
    )

    insertedBook = connection.execute(insertQuery)
    print(insertedBook)
    print(connection.lastInsertId())

    # connection.commit()

    connection.close()

    return insertedBook
