import re
import time
from time import sleep


import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

vodka_url = 'https://rumka.online/vodka/'
vodka_url_general = 'https://rumka.online'

vodka_list = []
def download_vodka_url(url):
    photo_url = requests.get(url, stream=True)
    r = open("C:\\Users\\Game-On-Dp\\Desktop\\my-projects\\Django+React\\backend\\media\\parse\\image\\vodka\\" + url.split('/')[-1] + '.png', 'wb')
    for value in photo_url.iter_content(1024*1024):
        r.write(value)
    r.close()

def get_vodka_url():
    for x in range(1,4):
        response = requests.get(f"{vodka_url}page={x}/", headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('div', class_='col-lg-4 col-6 col-sm-6 mb--40 mb-md--30')

        for i in data:
            card_url = vodka_url_general + i.find('a').get('href')
            yield card_url

def vodka_array():
    for card_url in get_vodka_url():
            response = requests.get(card_url, headers=headers)
            sleep(3)
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.find('div', id='nav-characteristics')

            name = soup.find('h1', class_='product-title').text
            price = soup.find('span', class_='money').text
            brand = data.find('table', class_='characteristics').find('td', string=re.compile('Бренд')).find_next_sibling().text

            try:
                country = data.find('table', class_='characteristics').find('td', string=re.compile('Країна-виробник товару')).find_next_sibling().text
            except AttributeError:
                country = ''
            try:
                volume = data.find('table', class_='characteristics').find('td', string=re.compile("Об'єм")).find_next_sibling().text
            except AttributeError:
                volume = ''
            try:
                amount_in_box = data.find('table', class_='characteristics').find('td', string=re.compile('Штук в ящику')).find_next_sibling().text
            except AttributeError:
                amount_in_box = ''
            try:
                vid = data.find('table', class_='characteristics').find('td', string=re.compile('Вид')).find_next_sibling().text
            except AttributeError:
                vid = ''
            try:
                strength = data.find('table', class_='characteristics').find('td', string=re.compile('Міцність')).find_next_sibling().text
            except AttributeError:
                strength = ''
            try:
                excerpt = data.find('table', class_='characteristics').find('td', string=re.compile('Витримка')).find_next_sibling().text
            except AttributeError:
                excerpt = ''
            try:
                supply_temperature = data.find('table', class_='characteristics').find('td', string=re.compile('Температура подачі')).find_next_sibling().text
            except AttributeError:
                supply_temperature = ''
            try:
                taste = data.find('table', class_='characteristics').find('td', string=re.compile('Смак')).find_next_sibling().text
            except AttributeError:
                taste = ''
            try:
                color = data.find('table', class_='characteristics').find('td', string=re.compile('Колір')).find_next_sibling().text
            except AttributeError:
                color = ''
            try:
                coctails = data.find('table', class_='characteristics').find('td', string=re.compile('Коктейлі')).find_next_sibling().text
            except AttributeError:
                coctails = ''
            try:
                gastronomic_compatibility = data.find('table', class_='characteristics').find('td', string=re.compile('Гастрономічна сполучуваність')).find_next_sibling().text
            except AttributeError:
                gastronomic_compatibility = ''
            try:
                sizes = data.find('table', class_='characteristics').find('td', string=re.compile('Розміри, см')).find_next_sibling().text
            except AttributeError:
                sizes = ''
            try:
                weight = data.find('table', class_='characteristics').find('td', string=re.compile('Вага, кг')).find_next_sibling().text
            except AttributeError:
                weight = ''

            description = soup.find('div', class_='product-description').text

            image_url = vodka_url_general + soup.find('img', class_='lazy')['src']
            download_vodka_url(image_url)
            image_url_edited = image_url.split('/')[-1] + '.png'

            def str_to_float_number(val):
                if val:
                    number = ''
                    for x in val:
                        if x.isdigit() or x in ['.', ',']:
                            if x == ',':
                                x = '.'
                            number += x
                    return float(number) if '.' in number else int(number)
                return None

            vodka_list.append([name, str_to_float_number(price), brand.lstrip(), country.lstrip(), str_to_float_number(volume), str_to_float_number(amount_in_box), vid.lstrip(), str_to_float_number(strength), excerpt.lstrip(), supply_temperature, taste.lstrip(), color.lstrip(), coctails.lstrip(), gastronomic_compatibility.lstrip(), sizes.lstrip(), weight.lstrip(), description.lstrip().replace('\n', '').replace('\t', '').replace('  ', ''), f"parse/image/vodka/{image_url_edited}"])
            print(name, '\n',image_url, '\n', price, '\n', brand, '\n', country, '\n', volume, '\n', amount_in_box, '\n', vid, '\n', strength, '\n', excerpt, '\n', supply_temperature, '\n', taste, '\n', color, '\n', coctails, '\n', gastronomic_compatibility, '\n', sizes, '\n', weight, '\n', description, '\n\n')

# vodka_array()

# Добавляем в базу данных данные через консоль shell
# from main.models import Vodka_characters
# from main.parse.vodka import vodka_parse
#
# vodka_parse.vodka_array()
# for x in vodka_parse.vodka_list:
#     Vodka_characters.objects.create(name=x[0], price=x[1], brand=x[2], country=x[3], volume=x[4], amount_in_box=x[5], vid=x[6], strength=x[7], excerpt=x[8], supply_temperature=x[9], taste=x[10], color=x[11], coctails=x[12], gastronomic_compatibility=x[13], sizes=x[14], weight=x[15], description=x[16], image=x[17])


# Также добавляем категорию для каждой записи
# from main.models import Category
#
# vodka = Category.objects.get(name='Водка')
# for x in Vodka_characters.objects.all():
#     x.category = vodka
#     x.save()

