import csv
from django.core.management.base import BaseCommand

from main.models import Cognak_characters
from main.parse.cognak import cognak_parse


class Command(BaseCommand):
    help = 'Export products data to a CSV file'

    def handle(self, *args, **kwargs):
        cognak_parse.cognak_array()
        for x in cognak_parse.cognak_list:
            Cognak_characters.objects.create(name = x[0],
                                             price = x[1],
                                             code = x[2],
                                             volume = x[3],
                                             brand = x[4],
                                             country = x[5],
                                             strength = x[6],
                                             excerpt = x[7],
                                             production_area = x[8],
                                             serving_temperature = x[9],
                                             favor = x[10],
                                             taste = x[11],
                                             gastronomic_combination = x[12],
                                             features_of_the_technology = x[13],
                                             sort = x[14],
                                             image =x[15])

        # Открываем файл для записи данных
        with open('cognac_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            # Записываем заголовки
            writer.writerow(['name',
                             'price',
                             'code',
                             'volume',
                             'brand',
                             'country',
                             'strength',
                             'excerpt',
                             'production_area',
                             'serving_temperature',
                             'favor',
                             'taste',
                             'gastronomic_combination',
                             'features_of_the_technology',
                             'sort',
                             'image',
                             ])

            cognacs = Cognak_characters.objects.all().values_list('name',
                                                                  'price',
                                                                  'code',
                                                                  'volume',
                                                                  'brand',
                                                                  'country',
                                                                  'strength',
                                                                  'excerpt',
                                                                  'production_area',
                                                                  'serving_temperature',
                                                                  'favor',
                                                                  'taste',
                                                                  'gastronomic_combination',
                                                                  'features_of_the_technology',
                                                                  'sort',
                                                                  'image',)

            # Записываем каждую запись в файл
            for cognac in cognacs:
                writer.writerow(cognac)

        self.stdout.write(self.style.SUCCESS('Data exported successfully'))