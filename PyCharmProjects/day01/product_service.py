"""
This service should represent an endpoint for a resource called "/api/products".
Following HTTP methods should be allowed:
1. GET
2. POST
3. PUT
4. PATCH
5. DELETE

Should allow content negotiation for XML and JSON content

Should allow pagination using _page and _limit query string parameters.
Should enable CORS - Cross Origin Resource Sharing
Should allow security via JWT
"""
from flask import Flask, Response, request
import json
import dicttoxml2
import xmltodict


app = Flask(__name__)
products = []


def create_json_response(data, status=200):
    return Response(json.dumps(data), status=status, mimetype='application/json')


def create_xml_response(data, status=200, root_elem='root', elem_name='elem'):
    xml_data = dicttoxml2.dicttoxml(data, custom_root=root_elem, item_func=lambda x: elem_name, attr_type=False)
    return Response(xml_data, status=status, mimetype='application/xml')


def create_response(data, status=200, root_elem='root', elem_name='elem'):
    if request.headers['Accept'] == 'application/xml':
        return create_xml_response(data, status, root_elem, elem_name)

    # assumption: request accept header == 'application/json'
    return create_json_response(data, status)


def get_request_body():
    if request.headers['Content-Type'] == 'application/xml':
        data = xmltodict.parse(request.get_data(as_text=True))
        data = json.loads(json.dumps(data))['product']
        return data

    # assumption: request content-type header == 'application/json'
    return request.get_json()


@app.route('/api/products', methods=['POST'])
def add_new_product():
    req_body = get_request_body()
    # generate new id as the max id present + 1
    ids = [p['_id'] for p in products]
    new_product_id = max(ids) + 1
    req_body['_id'] = new_product_id
    products.append(req_body)  # if you want this to be permanent, then save it to the "products_array_data.json"
    with open('products_array_data.json', 'w') as f1:
        json.dump(products, f1)
    return create_response(req_body)


@app.route('/api/products', methods=['GET'])
def get_all_products():
    data = products
    if 'brand' in request.args:
        data = [p for p in products if p['brand'] == request.args['brand']]
    elif 'category' in request.args:
        data = [p for p in products if p['category'] == request.args['category']]

    return create_response(data, root_elem='products', elem_name='product')


@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    result = [p for p in products if p['_id'] == product_id]
    if len(result) == 0:
        return create_response({'message': 'No data found'}, status=404, root_elem='error')
    else:
        return create_response(result[0], root_elem='product')


if __name__ == '__main__':
    # load the content of 'products_array_data.json' into the global variable 'products'
    filename = 'products_array_data.json'
    try:
        with open(filename) as file:
            products = json.load(file)
        app.run(port=8080, debug=True)
    except FileNotFoundError:
        print(f"Couldn't load the file {filename}")

