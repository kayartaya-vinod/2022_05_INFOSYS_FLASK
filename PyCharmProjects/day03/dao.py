from sqlalchemy import create_engine, String, Integer, Float, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlite3 import connect
import uuid
import json

my_sqlite_engine = create_engine("sqlite:///mydb.sqlite3", echo=False)

# create a class called "Base" which acts as base class for your model classes
Base = declarative_base(bind=my_sqlite_engine)
Session = sessionmaker(bind=my_sqlite_engine)


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(String, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    gender = Column(String, default='Male')
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    avatar = Column(String)

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.firstname = kwargs.get('firstname')
        self.lastname = kwargs.get('lastname')
        self.gender = kwargs.get('gender')
        self.email = kwargs.get('email')
        self.phone = kwargs.get('phone')
        self.address = kwargs.get('address')
        self.city = kwargs.get('city')
        self.state = kwargs.get('state')
        self.country = kwargs.get('country')
        self.avatar = kwargs.get('avatar')

    def as_tuple(self):
        return (self.id, self.firstname, self.lastname, self.gender,
                self.email, self.phone, self.address, self.city,
                self.state, self.country, self.avatar)

    @staticmethod
    def from_tuple(data):
        d = dict(zip(
            ['id', 'firstname', 'lastname', 'gender', 'email', 'phone', 'address', 'city', 'state', 'country', 'avatar'],
            data))
        return Customer(**d)

    def update_from(self, data):
        self.__dict__.update(data)

    def __str__(self):
        return f'Customer (firstname="{self.firstname}", lastname="{self.lastname}, email="{self.email}")'


class CustomerJsonEncoder(json.JSONEncoder):
    # this is the function that is used by json.dump or json.dumps
    def default(self, o):
        if isinstance(o, Customer):
            cust_dict = o.__dict__  # return a dictionary consisting of all members of "o", which is a Customer object
            cust_dict.pop('_sa_instance_state')
            return cust_dict
        return CustomerJsonEncoder(self, o)  # let JSONEncoder handle the rest of the types


class CustomerDao:

    def get_connection(self):
        return connect('mydb.sqlite3')

    def find_by_id(self, customer_id):
        with Session() as session:
            return session.query(Customer).get(customer_id)

    def add_customer(self, customer):
        customer.id = str(uuid.uuid4())
        with Session() as session:
            session.add(customer)
            session.commit()
        return customer

    def update_customer(self, customer):
        cust_dict = customer.__dict__
        if '_sa_instance_state' in cust_dict:
            cust_dict.pop('_sa_instance_state')
        with Session() as session:
            session.query(Customer).filter(Customer.id == customer.id).update(cust_dict)
            session.commit()
        return customer

    def delete_by_id(self, customer_id):
        pass

    def find_all(self, page_no=1, page_size=10):
        pass


    def find_by_email(self, email):
        pass

    def find_by_phone(self, phone):
        pass

    def find_by_city(self, city, page_no=1, page_size=10):
        pass

