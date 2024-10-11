import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

beer_url = "https://hophey.ua/ru/od/razlivnoe/"
beer_url_general = 'https://hophey.ua'

beer_list = []

def download_beer_url(url):
    photo_url = requests.get(url, stream=True)
    r = open("C:\\Users\\Game-On-Dp\\Desktop\\my-projects\\Django+React\\backend\\media\\parse\\image\\beer\\" + url.split('/')[-1], 'wb')
    for value in photo_url.iter_content(1024*1024):
        r.write(value)
    r.close()

def get_beer_url():
    response = requests.get(beer_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('div', attrs={'data-category': 'Пиво'})

    for i in data:
        card_url = "https://hophey.ua" + i.find('a', attrs={'class': 'd-flex flex-auto product-picture'}).get('href')
        yield card_url

def beer_array():
    for card_url in get_beer_url():
        response = requests.get(card_url, headers=headers)
        sleep(3)
        soup = BeautifulSoup(response.text, 'lxml')

        data = soup.find('div', attrs={'data-category':'Пиво'})
        name = data.find('h1', class_='text-regular').text
        category = 'Пиво'
        country_color_vid = data.find('span', class_='text-dark-gray').text
        price = data.find('span', class_='text-bold').text
        strength = data.find('div', class_='product-params-item-title', string='Крепость').find_parent('div').find('span', class_='text-bold').text
        bitterness = data.find('div', class_='product-params-item-title', string='Горечь').find_parent('div').find('span', class_='text-bold').text
        density = data.find('div', class_='product-params-item-title', string='Плотность').find_parent('div').find('span', class_='text-bold').text
        image_url = 'https://hophey.ua/' + data.find('img')['_src']

        extra_data1 = soup.find('div', class_='flex-fill product-detail-description-column')
        favor = extra_data1.find('p', string='Аромат').find_next_sibling().text
        taste = extra_data1.find('p', string='Вкус').find_next_sibling().text
        aftertaste = extra_data1.find('p', string='Послевкусие').find_next_sibling().text
        composition = extra_data1.find('p', string='Состав').find_next_sibling().text
        is_combined = extra_data1.find('p', string='С чем сочетается').find_next_sibling().text

        extra_data2 = soup.find('div', class_='d-flex product-detail-description accordeon-body bg-white')
        country = extra_data2.find('p', string='Страна').find_next_sibling().text
        type = extra_data2.find('p', string='Тип').find_next_sibling().text
        vid = extra_data2.find('p', string='Вид').find_next_sibling().text
        color = extra_data2.find('p', string='Цвет').find_next_sibling().text

        correct_card_url = card_url.split('https://hophey.ua')
        response_description = requests.get(beer_url, headers=headers)
        soup_description = BeautifulSoup(response_description.text, 'lxml')
        data_description = soup_description.find('a', class_='d-flex flex-auto product-picture', attrs={'href':correct_card_url}).parent.parent.find('div', class_='product-preview-text text-ellipsis four-line-clamp').text

        download_beer_url(image_url)
        image_url_edited = image_url.split('/')[-1]
        def str_to_float_number(val):
            number = ''
            for x in val:
                if x.isdigit() or x == '.':
                    number += x
            return float(number) if '.' in number else int(number)

        beer_list.append([name, float(price), country_color_vid, str_to_float_number(strength), str_to_float_number(bitterness), str_to_float_number(density), favor, taste, aftertaste, composition, is_combined, country, type, vid, color, f"parse/image/beer/{image_url_edited}"])
        print(name + '\n' + category + '\n' + type + '\n' + price + '\n' + strength + '\n' + bitterness + '\n' + density + '\n' + image_url + '\n' , data_description)


# beer_array()

# Добавляем в базу данных данные через консоль shell
# from main.models import Beer_characters
# from main.parse.beer import beer_parse
#
# beer_parse.beer_array()
# for x in beer_parse.beer_list:
#     Beer_characters.objects.create(name=x[0], price=x[1], country_color_vid=x[2], strength=x[3], bitterness=x[4], density=x[5], favor=x[6], taste=x[7], aftertaste = x[8], composition = x[9], is_combined = x[10], country = x[11], type = x[12], vid = x[13], color = x[14], image =x[15])


# Также добавляем категорию для каждой записи
# from main.models import Category
#
# pivo = Category.objects.get(name='Пиво')
# for x in Beer_characters.objects.all():
#     x.category = pivo
#     x.save()

