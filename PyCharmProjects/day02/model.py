import json


class CustomerJsonEncoder(json.JSONEncoder):
    # this is the function that is used by json.dump or json.dumps
    def default(self, o):
        if isinstance(o, Customer):
            return o.__dict__  # return a dictionary consisting of all members of "o", which is a Customer object

        return CustomerJsonEncoder(self, o)  # let JSONEncoder handle the rest of the types


class Customer:
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

    def toJSON(self):
        return json.dumps(self.__dict__)

    def __str__(self):
        return f'Customer (firstname="{self.firstname}", lastname="{self.lastname}, email="{self.email}")'
