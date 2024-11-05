import re
import time
from time import sleep
import os

import requests
from bs4 import BeautifulSoup

# Получаем путь до директории, где находится текущий файл
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

cognak_url = 'https://winestory.com.ua/ru/konjak.html'

cognak_list = []
def download_cognak_url(url):
    photo_url = requests.get(url, stream=True)
    # Строим относительный путь до папки "media/parse/image/cognak"
    image_path = os.path.join(BASE_DIR, 'media', 'parse', 'image', 'cognak', url.split('/')[-1])
    directory = os.path.dirname(image_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    r = open(image_path, 'wb')
    for value in photo_url.iter_content(1024*1024):
        r.write(value)
    r.close()

def get_cognak_url():
    response = requests.get(cognak_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find_all('a', class_='product-item-photo', limit=26)
    for x in data:
        card_url = x['href']
        yield card_url


def cognak_array():
    for card_url in get_cognak_url():
        response = requests.get(card_url, headers=headers)
        sleep(3)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('table', id='product-attribute-specs-table')

        name = soup.find('span', attrs={'data-ui-id':'page-title-wrapper'}).text
        price = soup.find('span', class_='price').text
        code = data.find('th', string='Код товара:').find_next_sibling('td').text
        category = data.find('th', string='Категория').find_next_sibling('td').text
        volume = data.find('th', string='Объем').find_next_sibling('td').text
        try:
            brand = data.find('th', string='Бренд').find_next_sibling('td').text
        except AttributeError:
            brand = ''
        country = data.find('th', string='Страна').find_next_sibling('td').text
        strength = data.find('th', string='Крепость').find_next_sibling('td').text
        try:
            excerpt = data.find('th', string='Выдержка').find_next_sibling('td').text
        except AttributeError:
            excerpt = ''
        try:
            production_area = data.find('th', string='Зона производства').find_next_sibling('td').text
        except AttributeError:
            production_area = ''
        try:
            serving_temperature = data.find('th', string='Температура сервировки').find_next_sibling('td').text
        except AttributeError:
            serving_temperature = ''
        try:
            favor = data.find('th', string='Аромат').find_next_sibling('td').text
        except AttributeError:
            favor = ''
        try:
            taste = data.find('th', string='Вкус').find_next_sibling('td').text
        except AttributeError:
            taste = ''
        try:
            gastronomic_combination = data.find('th', string='Гастрономическое сочетание').find_next_sibling('td').text
        except AttributeError:
            gastronomic_combination = ''
        try:
            features_of_the_technology = data.find('th', string='Особенности технологии').find_next_sibling('td').text
        except AttributeError:
            features_of_the_technology = ''
        try:
            sort = data.find('th', string='Сорт винограда').find_next_sibling('td').text
        except AttributeError:
            sort = ''
        image_url = soup.find('div', class_='product-image-wrap').find('img')['src']
        download_cognak_url(image_url)

        image_url_edited = image_url.split('/')[-1] + '.png'

        def str_to_float_number(val):
            if val:
                number = ''
                for x in val:
                    if x.isdigit() or x == '.':
                        number += x
                return float(number) if '.' in number else int(number)
            return None

        cognak_list.append([name, str_to_float_number(price), code, str_to_float_number(volume), brand.lstrip(), country.lstrip(), str_to_float_number(strength), excerpt.lstrip(), production_area.lstrip(), str_to_float_number(serving_temperature), favor.lstrip(), taste.lstrip(), gastronomic_combination.lstrip(), features_of_the_technology.lstrip(), sort.lstrip(), f"parse/image/cognak/{image_url_edited}"])
        print(image_url, '\n', name, '\n', price, '\n', code, '\n', category, '\n', volume, '\n', brand, '\n', country, '\n', strength, '\n', excerpt, '\n', production_area, '\n', serving_temperature, '\n', favor, '\n', taste, '\n', gastronomic_combination, '\n', features_of_the_technology, '\n', sort, '\n\n')

# cognak_array()

# Добавляем в базу данных данные через консоль shell
# from main.models import Cognak_characters
# from main.parse.cognak import cognak_parse
#
# cognak_parse.cognak_array()
# for x in cognak_parse.cognak_list:
#     Cognak_characters.objects.create(name = x[0], price = x[1], code = x[2], volume = x[3], brand = x[4], country = x[5], strength = x[6], excerpt = x[7], production_area = x[8], serving_temperature = x[9], favor = x[10], taste = x[11], gastronomic_combination = x[12], features_of_the_technology = x[13], sort = x[14], image =x[15])


# Также добавляем категорию для каждой записи
# from main.models import Category
#
# cognak = Category.objects.get(name='Коньяк')
# for x in Cognak_characters.objects.all():
#     x.category = cognak
#     x.save()