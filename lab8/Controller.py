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
    all = controller.get_all()
    print(all)

if __name__ == '__main__':
    main()