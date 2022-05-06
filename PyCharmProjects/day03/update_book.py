from db import my_sqlite_engine, Book
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # create a class (usually) called as Session
    Session = sessionmaker(bind=my_sqlite_engine)

    # an object of Session can be used for performing CRUD and QUERY operations
    session = Session()  # represents a DB connection

    book_id = int(input('Enter book id to search: '))
    qry = session.query(Book)
    book = qry.get(book_id)

    if book is None:
        print(f'No book found with id {book_id}')
        exit(0)

    print(book)
    new_price = float(input('Enter new price for the book: '))

    qry.filter(Book.id == book_id).update({'price': new_price})
    session.commit()
    session.close()