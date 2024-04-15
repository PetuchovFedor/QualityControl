import jsonschema.exceptions
from Controller import Controller
import unittest
import jsonschema
import json
import os

class TestController(unittest.TestCase):
    def setUp(self):
        with open('test-data/test_data.json') as f:
            self._test_data = json.load(f)
        with open('conf/products_schema.json') as f:
            self._products_schema = json.load(f)
        with open('conf/add_update_product_schema.json') as f:
            self._product_schema = json.load(f)    
        self._tmp_products = []
        self._controller = Controller()

    def tearDown(self):
        for tmp in self._tmp_products:
            self._controller.delete(tmp['id'])

    def test_get_all(self):
        items = self._controller.get_all()
        self.assertTrue(self._check_valid_json(items, self._products_schema), 'error with products')

    def test_add_valid_product(self):
        item = self._test_data['valid']
        self.assertTrue(self._check_valid_json(item, self._product_schema), 'error with add valid product')
        response = self._controller.create(item)
        item['id'] = response['id']
        self._tmp_products.append(item)    
        self.assertTrue(self._check_availability_by_id(item['id']), msg='error with adding item to list')  
        self.assertEqual(response['status'], 1, 'error with response status')

    def test_add_valid_product_with_lower_bound(self):
        item = self._test_data['valid_with_lower_bound']
        self.assertTrue(self._check_valid_json(item, self._product_schema), 'error with add valid_with_lower_bound product')
        response = self._controller.create(item)
        item['id'] = response['id']
        self._tmp_products.append(item)     
        self.assertTrue(self._check_availability_by_id(item['id']), msg='error with adding item to list')     
        self.assertEqual(response['status'], 1, 'error with response status')
    
    def test_add_valid_product_with_higher_bound(self):
        item = self._test_data['valid_with_higher_bound']
        self.assertTrue(self._check_valid_json(item, self._product_schema), 'error with add valid_with_higher_bound product')
        response = self._controller.create(item)
        item['id'] = response['id']
        self._tmp_products.append(item) 
        self.assertEqual(response['status'], 1, 'error with response status')
    
    def test_add_valid_product_with_alias(self):
        item = self._test_data['valid_with_alias']
        self.assertTrue(self._check_valid_json(item, self._product_schema), 'error with add valid_with_alias product')
        response = self._controller.create(item)
        item['id'] = response['id']
        self._tmp_products.append(item)
        self.assertTrue(self._check_availability_by_id(item['id']), msg='error with adding item to list')            
        self.assertEqual(response['status'], 1, 'error with response status')       
    
    def test_add_valid_product_with_negative_price(self):
        item = self._test_data['valid_with_negative_price']
        self.assertTrue(self._check_valid_json(item, self._product_schema), 'error with add valid_with_negative_price product')
        response = self._controller.create(item)
        item['id'] = response['id']
        self._tmp_products.append(item)
        self.assertTrue(self._check_availability_by_id(item['id']), msg='error with adding item to list')    
        self.assertEqual(response['status'], 1, 'error with response status')  

    def test_add_null_product(self):
        item = self._test_data['null']
        self.assertFalse(self._check_valid_json(item, self._product_schema), 'error with add invalid product')
        response = self._controller.create(item)  
        self.assertEqual(response, None, 'error with response status') 
    
    def test_add_product_with_invalid_category_id(self):
        item = self._test_data['invalid_category_id']
        self.assertFalse(self._check_valid_json(item, self._product_schema), 'error with add invalid product')
        response = self._controller.create(item) 
        self.assertEqual(response, None, 'error with response status') 
    
    def test_add_product_with_invalid_price(self):
        item = self._test_data['invalid_price']
        self.assertFalse(self._check_valid_json(item, self._product_schema), 'error with not add invalid product')
        response = self._controller.create(item)  
        self.assertEqual(response, None, 'error with response status') 

    def test_add_product_with_invalid_status(self):
        item = self._test_data['invalid_status']
        self.assertFalse(self._check_valid_json(item, self._product_schema), 'error with not add invalid product')
        response = self._controller.create(item)            
        self.assertEqual(response, None, 'error with response status') 
    
    def test_add_product_with_invalid_hit(self):
        item = self._test_data['invalid_status']
        self.assertFalse(self._check_valid_json(item, self._product_schema), 'error with not add invalid product')
        response = self._controller.create(item)         
        self.assertEqual(response, None, 'error with response status') 

    def test_success_edit_product(self):
        item = self._test_data['valid']
        response = self._controller.create(item)
        item['id'] = response['id']
        self._tmp_products.append(item)
        item['content'] = '124sdsafasf'
        item['keywords'] = '3000'
        item['price'] = 142
        response = self._controller.edit(item)
        tmp = self._get_by_id(item['id'])
        self.assertEqual(item['content'], tmp['content'], msg='error with editing')
        self.assertEqual(item['keywords'], tmp['keywords'], msg='error with editing')
        self.assertEqual(str(item['price']), str(tmp['price']), msg='error with editing')

    def test_edit_product_invalid_values(self):
        item = self._test_data['valid']
        response = self._controller.create(item)
        item['id'] = response['id']
        self._tmp_products.append(item)
        item['content'] = None
        item['keywords'] = '3000'
        item['price'] = 'asdsaf'
        response = self._controller.edit(item)
        self.assertEqual(response, None, 'error with response status') 

    def test_delete_existing_product(self):
        item = self._test_data['valid']
        response = self._controller.create(item)
        item['id'] = response['id']
        self._tmp_products.append(item)
        self._controller.delete(item['id'])
        self.assertFalse(self._check_availability_by_id(item['id']), msg='error with delete')
    
    def test_delete_non_existing_product(self):
        self._controller.delete(89421984721)
        self.assertFalse(self._check_availability_by_id(89421984721), msg='error with delete')

    def _check_valid_json(self, json, schema):
        try:
            jsonschema.validate(json, schema)
        except jsonschema.exceptions.ValidationError as error:
            # print(error)
            return False    
        return True
    
    def _check_availability_by_id(self, id):
        all = self._controller.get_all()
        for tmp in all:
            if tmp['id'] == str(id):
                return True
        return False
    
    def _get_by_id(self, id):
        all = self._controller.get_all()
        for tmp in all:
            if tmp['id'] == str(id):
                return tmp
        return None 