from db import my_sqlite_engine, Book
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # create a class (usually) called as Session
    Session = sessionmaker(bind=my_sqlite_engine)

    # an object of Session can be used for performing CRUD and QUERY operations
    with Session() as session:  # represents a DB connection
        book_id = int(input('Enter the book id to delete: '))
        book_to_delete = session.query(Book).get(book_id)
        if book_to_delete is None:
            print(f'No book with id {book_id} found!')
        else:
            session.delete(book_to_delete)
            session.commit()
            print(f'Deleted the book - {book_to_delete}')
