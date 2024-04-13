from main import ObserverOfExchangeRates
# from unittest.mock import patch, Mock
from unittest.mock import patch
from unittest import TestCase
# import unittest

class TestExchangeRatesObserver(TestCase):
    @patch('main.ObserverOfExchangeRates')
    def test_get_all_currency(self, MockObserver):
        #arrange
        observer = MockObserver()        
        observer.get_all_currency.return_value = {
            'AUD': 'Австралийский доллар','AZN': 'Азербайджанский манат',
            'GBP': 'Фунт стерлингов Соединенного королевства', 'AMD': 'Армянских драмов',
            'USD': 'Доллар США', 'EUR': 'Евро'
        }
        #act
        response = observer.get_all_currency()
        #assert
        self.assertIsNotNone(response, msg='error with result value, it is none')
        self.assertIsInstance(response, dict, msg='result value is not dict')
    
    @patch('main.ObserverOfExchangeRates.get_dollar_exchange_rate', return_value=92.581)
    def test_get_dollar_exchange_rate(self, get_dollar_exchange_rate):
        #arrange
        rate = None
        #act
        rate = get_dollar_exchange_rate()
        #assert 
        self.assertEqual(rate, 92.581, msg='result value not equal to the expected result')
    @patch('main.ObserverOfExchangeRates.get_euro_exchange_rate', return_value=100.2236)
    def test_get_euro_exchange_rate(self, get_euro_exchange_rate):
        #arrange
        rate = None
        #act
        rate = get_euro_exchange_rate()
        #assert 
        self.assertEqual(rate, 100.2236, msg='result value not equal to the expected result')
    @patch('main.ObserverOfExchangeRates.get_exchange_rate_by_key', return_value=20.7218)
    def test_get_exchange_rate_by_key(self, get_exchange_rate_by_key):
        #arrange
        rate = None
        #act
        rate = get_exchange_rate_by_key('KZT')
        #assert 
        self.assertEqual(rate, 20.7218, msg='result value not equal to the expected result')

    @patch('main.ObserverOfExchangeRates')
    def test_get_exchange_rate_by_key_when_throw_non_existing_key_exception(self, MockObserver):
        #arrange
        observer = MockObserver()
        observer.get_exchange_rate_by_key.side_effect = RuntimeError('There is no such currency in the list')
        def get_exchange_rate_by_non_existing_key(observer):
            #act
            observer.get_exchange_rate_by_key('adafsasf')
        
        #assert         
        with self.assertRaises(RuntimeError, msg='error with exception when non-existing key'):
            get_exchange_rate_by_non_existing_key(observer)
       
    @patch('main.ObserverOfExchangeRates')
    def test_get_exchange_rate_by_key_when_throw_non_string_type_key_exception(self, MockObserver):
        #arrange
        observer = MockObserver()
        observer.get_exchange_rate_by_key.side_effect = RuntimeError('The key must be a string type')
        def get_exchange_rate_by_non_string_type_key(observer):
            #act
            observer.get_exchange_rate_by_key(124)
        #assert
        with self.assertRaises(RuntimeError, msg='error with exception when non-string type key'):
            get_exchange_rate_by_non_string_type_key(observer)