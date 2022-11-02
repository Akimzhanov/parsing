from bs4 import BeautifulSoup as BS
import requests
import csv

from url import URL


res = requests.get(URL)

def get_html_card():
    html = requests.get(URL)
    soup = BS(html.text, 'lxml')
    cards = soup.find('div', class_='row product-listing')
    cards2 = cards.find_all('div', class_='product-layout')
    return cards2

def parse_card(cards2):
    obj_list = []
    # try: 
    for i in cards2:
        # print(i.find('div', class_='caption').find('a').text)
        obj = {
            'title': i.find('div', class_='caption').find('a').text,
            'price': i.find('p', class_='price').find('span', class_='price-new').text,
            'image': i.find('div', class_='image hover_fade_in_back').find('img').get('src')
        }

        # print(obj)
        obj_list.append(obj)  
    # except AttributeError:
    #     return 'ошибка.'

    with open('csvTABLE.csv', 'w') as file:
        fieldnames = obj_list[0].keys()
        csv_writer = csv.DictWriter(file, fieldnames = fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(obj_list)

cards = get_html_card()
# print(cards)
parse_card(cards)








