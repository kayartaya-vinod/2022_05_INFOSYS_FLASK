from sqlalchemy import create_engine, String, Integer, Float, Column
from sqlalchemy.ext.declarative import declarative_base

my_sqlite_engine = create_engine("sqlite:///book_library.sqlite3", echo=False)

# create a class called "Base" which acts as base class for your model classes
Base = declarative_base(bind=my_sqlite_engine)


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True)
    author = Column(String)
    price = Column(Float)

    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.author = kwargs.get('author')
        self.price = kwargs.get('price')

    def __repr__(self):
        return f'Book (id={self.id}, title="{self.title}", author="{self.author}", price=Rs.{self.price})'


if __name__ == '__main__':
    Base.metadata.create_all(bind=my_sqlite_engine)