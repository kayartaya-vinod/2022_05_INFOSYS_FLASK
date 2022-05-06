from dao import my_sqlite_engine, Customer
from sqlalchemy.orm import sessionmaker


def line(char='-'):
    print(char * 50)


if __name__ == '__main__':
    # create a class (usually) called as Session
    Session = sessionmaker(bind=my_sqlite_engine)

    # an object of Session can be used for performing CRUD and QUERY operations
    session = Session()  # represents a DB connection
    c1 = session.query(Customer).get('4a673257-7489-4062-8a29-e1931cc2f3bb')
    print(c1)