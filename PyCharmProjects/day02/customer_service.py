import json
from flask import Flask, Response, request
from dao import CustomerDao
from model import CustomerJsonEncoder, Customer
from flask_cors import CORS  #, cross_origin

app = Flask(__name__)
dao = CustomerDao()
CORS(app)


def create_response(data, status=200):
    if data is None:
        status = 204
    json_data = json.dumps(data, cls=CustomerJsonEncoder)
    # return Response(json_data, status=status, mimetype='application/json', headers={'access-control-allow-origin': '*'})
    return Response(json_data, status=status, mimetype='application/json')


@app.route('/api/customers', methods=['POST'])
def handle_post_request():
    body_dict = request.get_json()
    # do some basic validations
    cust = Customer(**body_dict)
    try:
        new_cust = dao.add_customer(cust)
    except Exception as ex:
        err = {'message': str(ex)}
        return create_response(err, status=500)

    return create_response(new_cust, status=201)



# /api/customers?_page=2&_limit=10
# /api/customers?email=epashbee8@comcast.net
# /api/customers?phone=3933114624
# @cross_origin(methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
@app.route('/api/customers', methods=['GET'])
def handle_get_all_customers():

    if 'email' in request.args:
        return create_response(dao.find_by_email(request.args['email']))

    if 'phone' in request.args:
        return create_response(dao.find_by_phone(request.args['phone']))

    page_size = 10
    page_no = 1

    if '_page' in request.args:
        try:
            page_no = int(request.args['_page'])
        except ValueError:
            pass

    if '_limit' in request.args:
        try:
            page_size = int(request.args['_limit'])
        except ValueError:
            pass

    customers = dao.find_all(page_no, page_size)
    return create_response(customers)


@app.route('/api/customers/<string:customer_id>', methods=['GET'])
def handle_get_one_customer(customer_id):
    cust = dao.find_by_id(customer_id)
    if cust is None:
        err = {'message': f'No data found for customer id {customer_id}'}
        return create_response(err, 404)
    return create_response(cust)





if __name__ == '__main__':
    app.run(port=8080, debug=True)
