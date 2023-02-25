from bs4 import BeautifulSoup
import requests as rq

def get_currency_value(value, cur_from, cur_to):
    url = f'https://www.xe.com/currencyconverter/convert/?Amount={value}&From={cur_from}&To={cur_to}'
    content = rq.get(url).text

    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find('p', class_='result__BigRate-sc-1bsijpp-1 iGrAod').get_text()
    
    if ',' in rate:
        rate = rate.replace(',', '')
        rate = float(rate.split(' ')[0][:-4])
        return rate

    else:
        rate = float(rate.split(' ')[0][:-4])
        return rate

if __name__ == '__main__':
    value = input('Enter the amount of currency:\n')
    cur_from = input('Enter the name of the currency from which you want to convert:\n')
    cur_to = input('Enter the name of the currency to which you want to convert:\n')
    print(f'{value} {cur_from} is {get_currency_value(value, cur_from, cur_to)} {cur_to}')
    input('Press Enter for exit')

    
