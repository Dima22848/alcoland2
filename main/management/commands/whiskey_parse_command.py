import csv
from django.core.management.base import BaseCommand

from main.models import Whiskey_characters
from main.parse.whiskey import whiskey_parse


class Command(BaseCommand):
    help = 'Export products data to a CSV file'

    def handle(self, *args, **kwargs):
        whiskey_parse.whiskey_array()
        print(f"Список whiskey_list содержит {len(whiskey_parse.whiskey_list)} записей.")  # Отладка
        for x in whiskey_parse.whiskey_list:
            print(x)
            Whiskey_characters.objects.create(name=x[0],
                                              price=x[1],
                                              brand=x[2],
                                              country=x[3],
                                              vid=x[4],
                                              taste=x[5],
                                              favor=x[6],
                                              excerpt=x[7],
                                              volume=x[8],
                                              strength=x[9],
                                              fats=x[10],
                                              carbohydrates=x[11],
                                              proteins=x[12],
                                              calorie_content_kcal=x[13],
                                              humidity=x[14],
                                              storage_temperature=x[15],
                                              expiration_date=x[16],
                                              storage_conditions=x[17],
                                              description=x[18],
                                              image=x[19])

        # Открываем файл для записи данных
        with open('whiskey_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            # Записываем заголовки
            writer.writerow(['name',
                             'price',
                             'brand',
                             'country',
                             'vid',
                             'taste',
                             'favor',
                             'excerpt',
                             'volume',
                             'strength',
                             'fats',
                             'carbohydrates',
                             'proteins',
                             'calorie_content_kcal',
                             'humidity',
                             'storage_temperature',
                             'expiration_date',
                             'storage_conditions',
                             'description',
                             ])

            whiskeys = Whiskey_characters.objects.all().values_list('name',
                                                                    'price',
                                                                    'brand',
                                                                    'country',
                                                                    'vid',
                                                                    'taste',
                                                                    'favor',
                                                                    'excerpt',
                                                                    'volume',
                                                                    'strength',
                                                                    'fats',
                                                                    'carbohydrates',
                                                                    'proteins',
                                                                    'calorie_content_kcal',
                                                                    'humidity',
                                                                    'storage_temperature',
                                                                    'expiration_date',
                                                                    'storage_conditions',
                                                                    'description',)

            # Записываем каждую запись в файл
            for whiskey in whiskeys:
                writer.writerow(whiskey)

        self.stdout.write(self.style.SUCCESS('Data exported successfully'))