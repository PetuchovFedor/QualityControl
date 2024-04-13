import requests
# data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
# print(data)

class ObserverOfExchangeRates:    
    def __init__(self):
        self._url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    
    def get_all_currency(self):
        data = requests.get(self._url).json()
        result = dict()
        for key in data['Valute'].keys():
            result.__setitem__(key,  data['Valute'][key]['Name'])
        return result
    
    def get_dollar_exchange_rate(self):
        data = requests.get(self._url).json()
        # print(type(data['Valute']['USD']))
        return data['Valute']['USD']['Value']
    
    def get_euro_exchange_rate(self):
        data = requests.get(self._url).json()
        return data['Valute']['EUR']['Value']
    
    def get_exchange_rate_by_key(self, key):
        data = requests.get(self._url).json()
        if type(key) != str:
            raise RuntimeError('The key must be a string type')
        if not key in data['Valute']:
            raise RuntimeError('There is no such currency in the list')        
        return data['Valute'][key]['Value']
    
def main():
    observer = ObserverOfExchangeRates()
    # observer.get_dollar_exchange_rate()
    print(observer.get_exchange_rate_by_key('KZT'))    

if __name__ == '__main__':
    main()    