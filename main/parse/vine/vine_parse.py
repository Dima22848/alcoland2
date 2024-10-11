import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

vine_url = 'https://winewine.com.ua/ru/wine/'

vine_list = []
def download_vine_url(url):
    photo_url = requests.get(url, stream=True)
    r = open("C:\\Users\\Game-On-Dp\\Desktop\\my-projects\\Django+React\\backend\\media\\parse\\image\\vine\\" + url.split('/')[-1], 'wb')
    for value in photo_url.iter_content(1024*1024):
        r.write(value)
    r.close()


def get_vine_url():
    for i in range(1,4):
        response = requests.get(f'{vine_url}page/{i}/', headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        block = soup.find('ul', class_='products elementor-grid columns-4')
        data = block.find_all('a', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link')

        for x in data:
            card_url = x['href']
            yield card_url


def vine_array():
    for card_url in get_vine_url():
        sleep(3)
        print(card_url)
        response = requests.get(card_url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        name = soup.find('h1', class_='elementor-heading-title elementor-size-default').text
        price = soup.find('span', class_='woocommerce-Price-amount amount').find('bdi').text

        try:
            color = soup.find('span', string='Цвет: ').next_sibling.text
        except AttributeError:
            color = ''

        try:
            country = soup.find('span', string='Страна: ').next_sibling.text
        except AttributeError:
            country = ''

        try:
            alcgol_percentage = soup.find('span', string='Алкоголь: ').next_sibling.text
        except AttributeError:
            alcgol_percentage = ''

        try:
            type = soup.find('span', string='Тип: ').next_sibling.text
        except AttributeError:
            type = ''

        try:
            brand = soup.find('span', string='Бренд: ').next_sibling.text
        except AttributeError:
            brand = ''

        try:
            sugar = soup.find('span', string='Сахар: ').next_sibling.text
        except AttributeError:
            sugar = ''

        try:
            region = soup.find('span', string='Регион: ').next_sibling.text
        except AttributeError:
            region = ''

        try:
            style = soup.find('span', string='Стиль: ').next_sibling.text
        except AttributeError:
            style = ''

        try:
            sort = soup.find('span', string='Сорт: ').next_sibling.text
        except AttributeError:
            sort = ''

        try:
            classification = soup.find('span', string='Классификация: ').next_sibling.text
        except AttributeError:
            classification = ''

        image_url = soup.find_all('img')[2]['src']
        download_vine_url(image_url)
        image_url_edited = image_url.split('/')[-1]

        def str_to_float_number(val):
            if val:
                number = ''
                for x in val:
                    if x.isdigit() or x == '.':
                        number += x
                return float(number) if '.' in number else int(number)
            return None

        vine_list.append([name, str_to_float_number(price), color, country, str_to_float_number(alcgol_percentage), type, brand, sugar, region, style, sort, classification, f"parse/image/vine/{image_url_edited}"])
        # print(name, '\n', image_url, '\n', price, '\n', color , '\n' , country , '\n' , alcgol_percentage , '\n' , type , '\n' , brand, '\n' , sugar, '\n', region, '\n', style, '\n', sort, '\n', classification, '\n\n')

# vine_array()

# Добавляем в базу данных данные через консоль shell
# from main.models import Vine_characters
# from main.parse.vine import vine_parse
#
# vine_parse.vine_array()
# for x in vine_parse.vine_list:
#     Vine_characters.objects.create(name=x[0], price=x[1], color=x[2], country=x[3], alcogol_percentage=x[4], type=x[5], brand=x[6], sugar=x[7], region=x[8], style=x[9], sort=x[10], classification=x[11], image=x[12])


# Также добавляем категорию для каждой записи
# from main.models import Category
#
# vino = Category.objects.get(name='Вино')
# for x in Vine_characters.objects.all():
#     x.category = vino
#     x.save()