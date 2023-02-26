from bs4 import BeautifulSoup
import requests as rq

def get_currency_value(value, cur_from, cur_to):
    url = f'https://www.xe.com/currencyconverter/convert/?Amount={value}&From={cur_from}&To={cur_to}'
    
    try:
        content = rq.get(url).text
        soup = BeautifulSoup(content, 'html.parser')
        rate = soup.find('p', class_='result__BigRate-sc-1bsijpp-1 iGrAod').get_text()
        
        if ',' in rate:
            rate = rate.replace(',', '')
        
    except rq.exceptions.RequestException as e:
        print(f'Error: {e}')
        rate = None
        input('Press Enter for exit')

    except AttributeError as e:
        print(f'Error: Currency conversion data not found')
        rate = None
        input('Press Enter for exit')

    except  ValueError as e:
        print(f'Error: {e}')
        rate = None
        input('Press Enter for exit')

    return float(rate.split(' ')[0])

if __name__ == '__main__':
    while True:
        value = input('Enter the amount of currency:\n')
        while not value.isnumeric():
            value = input('Please enter a numeric value:\n')
        cur_from = input('Enter the name of the currency from which you want to convert:\n').upper()
        while len(cur_from) != 3:
            cur_from = input('Please enter a 3-character currency code:\n').upper()
        cur_to = input('Enter the name of the currency to which you want to convert:\n').upper()
        while len(cur_to) != 3:
            cur_to = input('Please enter a 3-character currency code:\n').upper()
        rate = get_currency_value(value, cur_from, cur_to)
        if rate:
            print(f'{value} {cur_from} is {rate} {cur_to}')
            repeat = input('Would you like to make another conversion? (y/n):\n')
            while repeat.lower() not in ['y', 'n']:
                repeat = input('Invalid input. Please enter "y" or "n": ')
            if repeat.lower() == 'n':
                break
    print('Exiting...')