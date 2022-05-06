from db import my_sqlite_engine, Book
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc


def line(char='-'):
    print(char * 50)


if __name__ == '__main__':
    # create a class (usually) called as Session
    Session = sessionmaker(bind=my_sqlite_engine)

    # an object of Session can be used for performing CRUD and QUERY operations
    session = Session()  # represents a DB connection
    book = session.query(Book).get(2)  # book whose id is 3
    print(book)

    # session.query(..) returns a sqlalchemy.orm.query.Query object
    # which as these functions:
    # get(pk)
    # all()
    # count()
    # first()
    # filter(..)
    # limit(n)
    # offset(n)
    # ... and  many more
    line()
    qry = session.query(Book)
    books = qry.all()
    for b in books:
        print(b)

    line()
    for b in qry.order_by(Book.title):
        print(b)

    line()
    cnt = qry.count()
    print(f'Total number of books we have is {cnt}')

    line()
    books = qry.filter(Book.price > 500.0)
    for b in books:
        print(b)

    line()
    for b in qry.order_by(desc(Book.price)):
        print(b)
    session.close()
