from db import my_sqlite_engine, Book
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # create a class (usually) called as Session
    Session = sessionmaker(bind=my_sqlite_engine)

    # an object of Session can be used for performing CRUD and QUERY operations
    session = Session()  # represents a DB connection

    while True:
        title = input('Enter book title: ')
        author = input('Enter book author/s: ')
        price = float(input('Enter book price: '))
        book = Book(title=title, author=author, price=price)
        session.add(book)  # this generates an SQL INSERT command to be executed on the db engine during COMMIT

        choice = input('Wish to add another? (yes/no): (yes) ')
        if choice.lower() in ['no', 'n']:
            break
        print()

    session.commit()  # All SQL DML (INSERT/UPDATE/DELETE) statements will be executed
    session.close()  # closing a DB connection
