import dicttoxml2


if __name__ == '__main__':
    data = [
        {'name': 'Vinod', 'email': 'vinod@vinod.co', 'age': 48},
        {'name': 'Shyam', 'email': 'shyam@xmpl.com', 'age': 49},
        {'name': 'John', 'email': 'john@xmpl.com', 'age': 44}
    ]

    xml_data = dicttoxml2.dicttoxml(data, attr_type=False, custom_root='people', item_func=lambda x: 'person')
    print(xml_data.decode('utf-8'))
