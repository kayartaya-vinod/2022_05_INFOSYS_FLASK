import uuid
from sqlite3 import connect
# from mysql.connector import connect
from model import Customer


class CustomerDao:

    def get_connection(self):
        return connect('mydb.sqlite3')

    def find_by_id(self, customer_id):
        with self.get_connection() as conn:
            print('got connection', conn)
            cmd = 'select * from customers where id = ?'  # use %s in place of ? while using MySQL
            cur = conn.cursor() # with mysql, you may use context manager (with block)
            cur.execute(cmd, [customer_id])
            row = cur.fetchone()
            cur.close()

            if row is None:
                return None
            return Customer.from_tuple(row)

    def add_customer(self, customer):
        customer.id = str(uuid.uuid4())
        cmd = 'insert into customers values (?,?,?,?,?,?,?,?,?,?,?)'
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(cmd, customer.as_tuple())
            conn.commit()
            cur.close()
            return customer

    def update_customer(self, customer):
        cmd = 'update customers set firstname=?, lastname=?, gender=?, email=?, phone=?, address=?, ' \
              'city=?, state=?, country=?, avatar=? where id=?'
        params = customer.as_tuple()
        params = params[1:]+(params[0], )  # rotate such that first element becomes the last element
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(cmd, params)
            conn.commit()
            cur.close()
            return customer

    def delete_by_id(self, customer_id):
        cmd = 'delete from customers where id = ?'  # hard delete;
        # soft delete -> 'update customers set is_active=0 where id=?'
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(cmd, [customer_id])
            conn.commit()
            cur.close()

    def find_all(self, page_no=1, page_size=10):
        cmd = 'select * from customers limit ? offset ?'
        skip = (page_no-1) * page_size
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(cmd, [page_size, skip])
            rows = cur.fetchall()
            cur.close()
            return [Customer.from_tuple(row) for row in rows]

    def __find_one_by_field(self, field, value):
        cmd = f'select * from customers where {field}=?'
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(cmd, [value])
            row = cur.fetchone()
            if row is None:
                return None
            return Customer.from_tuple(row)

    def find_by_email(self, email):
        return self.__find_one_by_field('email', email)

    def find_by_phone(self, phone):
        return self.__find_one_by_field('phone', phone)

    def find_by_city(self, city, page_no=1, page_size=10):
        pass


if __name__ == '__main__':
    dao = CustomerDao()
    customers = dao.find_all(page_no=2)
    for c in customers:
        print(c)
