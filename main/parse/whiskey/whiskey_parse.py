import re
import time
from time import sleep


import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}


whiskey_url = 'https://varus.ua/ru/alkogol/micni-napoi/viski'
whiskey_url_general = 'https://varus.ua'

whiskey_list = []

def download_whiskey_url(url):
    photo_url = requests.get(url, stream=True)
    r = open("C:\\Users\\Game-On-Dp\\Desktop\\my-projects\\Django+React\\backend\\media\\parse\\image\\whiskey\\" + url.split('/')[-1] + '.png', 'wb')
    for value in photo_url.iter_content(1024*1024):
        r.write(value)
    r.close()

def get_whiskey_url():
    for x in range(1,3):
        response = requests.get(f"{whiskey_url}?page={x}", headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('div', class_='sf-product-card__wrapper m-category-list__item')

        for i in data:
            card_url = whiskey_url_general + i.find('a', class_='sf-link sf-product-card__link').get('href')
            yield card_url

def whiskey_array():
    for card_url in get_whiskey_url():
            response = requests.get(card_url, headers=headers)
            sleep(3)
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.find('div', class_='m-product-tab-content__left')

            name = soup.find('h1', class_='sf-heading__title').text
            try:
                price = (soup.find('div', class_='sf-price').find('del') or soup.find('div', class_='sf-price').find('span')).text
            except AttributeError:
                price = ''
            try:
                brand = data.find('div', string=re.compile('Бренд')).find_next_sibling('div').text
            except AttributeError:
                brand = ''
            try:
                country = data.find('div', string=re.compile('Страна производства')).find_next_sibling('div').text
            except AttributeError:
                country = ''
            try:
                vid = data.find('div', string=re.compile('Вид напитка')).find_next_sibling('div').text
            except AttributeError:
                vid = ''
            try:
                taste = data.find('div', string=re.compile('Вкус')).find_next_sibling('div').text
            except AttributeError:
                taste = ''
            try:
                favor = data.find('div', string=re.compile('Аромат')).find_next_sibling('div').text
            except AttributeError:
                favor = ''
            try:
                excerpt = data.find('div', string=re.compile('Выдержка')).find_next_sibling('div').text
            except AttributeError:
                excerpt = ''
            try:
                volume = data.find('div', string=re.compile('Объем')).find_next_sibling('div').text
            except AttributeError:
                volume = ''
            try:
                strength = data.find('div', string=re.compile('Крепость')).find_next_sibling('div').text
            except AttributeError:
                strength = ''
            try:
                fats = data.find('div', string=re.compile('Жиры')).find_next_sibling('div').text
            except AttributeError:
                fats = ''
            try:
                carbohydrates = data.find('div', string=re.compile('Углеводы')).find_next_sibling('div').text
            except AttributeError:
                carbohydrates = ''
            try:
                proteins = data.find('div', string=re.compile('Белки')).find_next_sibling('div').text
            except AttributeError:
                proteins = ''
            try:
                calorie_content_kcal = data.find('div', string=re.compile('Калорийность ккал')).find_next_sibling('div').text
            except AttributeError:
                calorie_content_kcal = ''
            try:
                humidity = data.find('div', string=re.compile('Влажность')).find_next_sibling('div').text
            except AttributeError:
                humidity = ''
            try:
                storage_temperature = data.find('div', string=re.compile('Температура хранения')).find_next_sibling('div').text
            except AttributeError:
                storage_temperature = ''
            try:
                expiration_date = data.find('div', string=re.compile('Срок годности')).find_next_sibling('div').text
            except AttributeError:
                expiration_date = ''
            try:
                storage_conditions = data.find('div', string=re.compile('Условия хранения')).find_next_sibling('div').text
            except AttributeError:
                storage_conditions = ''
            try:
                description = data.find('section').text
            except AttributeError:
                description = ''

            image_url = soup.find_all('img')[2]['src']
            download_whiskey_url(image_url)
            image_url_edited = image_url.split('/')[-1] + '.png'

            def str_to_float_number(val):
                if val:
                    number = ''
                    for x in val:
                        if x.isdigit() or x == '.':
                            number += x
                    return float(number) if '.' in number else int(number)
                return None

            whiskey_list.append([name.lstrip(), str_to_float_number(price), brand, country, vid, taste, favor, excerpt, str_to_float_number(volume), str_to_float_number(strength), fats, carbohydrates, proteins, calorie_content_kcal, humidity, storage_temperature, expiration_date, storage_conditions, description, f"parse/image/whiskey/{image_url_edited}"])
            print(name, '\n', image_url, '\n', price, '\n', brand, '\n', country, '\n', vid, '\n', taste, '\n', favor, '\n', excerpt, '\n', volume, '\n', strength, '\n', fats, '\n', carbohydrates, '\n', proteins, '\n', calorie_content_kcal, '\n', humidity, '\n', storage_temperature, '\n', expiration_date, '\n', storage_conditions, '\n', description, '\n\n')

# whiskey_array()


# Добавляем в базу данных данные через консоль shell
# from main.models import Whiskey_characters
# from main.parse.whiskey import whiskey_parse
#
# whiskey_parse.whiskey_array()
# for x in whiskey_parse.whiskey_list:
#     Whiskey_characters.objects.create(name=x[0], price=x[1], brand=x[2], country=x[3], vid=x[4], taste=x[5], favor=x[6], excerpt=x[7], volume=x[8], strength=x[9], fats=x[10], carbohydrates=x[11], proteins=x[12], calorie_content_kcal=x[13], humidity=x[14], storage_temperature=x[15], expiration_date=x[16], storage_conditions=x[17], description=x[18], image=x[19])



# Также добавляем категорию для каждой записи
# from main.models import Category
#
# whiskey = Category.objects.get(name='Виски')
# for x in Whiskey_characters.objects.all():
#     x.category = whiskey
#     x.save()