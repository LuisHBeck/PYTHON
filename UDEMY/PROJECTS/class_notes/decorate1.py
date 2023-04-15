import requests
import time

def calculate_time(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print(f'Execution time = {end - start}')
    return inner     


@calculate_time
def get_dollar_quotation():
    link = f'https://economia.awesomeapi.com.br/last/USD-BRL'
    request = requests.get(link)
    request = request.json()
    print(request['USDBRL']['bid'])


get_dollar_quotation()
