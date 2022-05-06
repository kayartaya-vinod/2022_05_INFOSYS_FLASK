from db import my_sqlite_engine, Book
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # create a class (usually) called as Session
    Session = sessionmaker(bind=my_sqlite_engine)

    # an object of Session can be used for performing CRUD and QUERY operations
    session = Session()  # represents a DB connection

    all_books = session.query(Book).filter(Book.price > 500).all()
    for b in all_books:
        print(b)

    print()
    first_book = session.query(Book).filter(Book.price > 500).first()
    print(first_book)
