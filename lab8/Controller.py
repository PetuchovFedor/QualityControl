import jsonschema.exceptions
import requests
import Urls
import jsonschema
import json

class Controller:  
    def get_all(self):
        data = requests.get(Urls.BASE_URL + Urls.GET_ALL_PRODUCTS)
        return data.json()
    def create(self, product):
        data = requests.post(Urls.BASE_URL + Urls.ADD_PRODUCT, json=product)
        try:
            return data.json()
        except:
            return None
    def delete(self, id):
        data = requests.delete(Urls.BASE_URL + Urls.DELETE_PRODUCT, params={'id': id})
        return data.json()    
    def edit(self, product):
        data = requests.post(Urls.BASE_URL + Urls.EDIT_PRODUCT, json=product)
        try:
            return data.json()
        except:
            return None

def main():
    controller = Controller()
    all = controller.delete(100002324)
    # for t in all:
    # print(controller.delete('25719'))
    print(all)
    # try:
        # jsonschema.validate(all, c)
    # except jsonschema.exceptions.ValidationError as error:
        # print(error)
    # test_data_file = open('test-data/test_data.json')
    # products_schema_file = open('conf/products_schema.json')
    # product_schema_file = open('conf/add_update_product_schema.json')
    # _test_data = json.load(test_data_file)
    # _products_schema = json.load(products_schema_file)
    # _product_schema = json.load(product_schema_file)
    # print(_product_schema)
    # print(_test_data)
    # print(_products_schema)


if __name__ == '__main__':
    main()    