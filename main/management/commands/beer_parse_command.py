import csv
from django.core.management.base import BaseCommand

from main.models import Beer_characters
from main.parse.beer import beer_parse


class Command(BaseCommand):
    help = 'Export products data to a CSV file'

    def handle(self, *args, **kwargs):
        beer_parse.beer_array()
        for x in beer_parse.beer_list:
            Beer_characters.objects.create(name=x[0],
                                           price=x[1],
                                           country_color_vid=x[2],
                                           strength=x[3],
                                           bitterness=x[4],
                                           density=x[5],
                                           favor=x[6],
                                           taste=x[7],
                                           aftertaste=x[8],
                                           composition=x[9],
                                           is_combined=x[10],
                                           country=x[11],
                                           type=x[12],
                                           vid=x[13],
                                           color=x[14],
                                           image=x[15])

        # Открываем файл для записи данных
        with open('beer_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            # Записываем заголовки
            writer.writerow(['name',
                             'price',
                             'country_color_vid',
                             'strength',
                             'bitterness',
                             'density',
                             'favor',
                             'taste',
                             'aftertaste',
                             'composition',
                             'is_combined',
                             'country',
                             'type',
                             'vid',
                             'color'])

            beers = Beer_characters.objects.all().values_list('name',
                                                              'price',
                                                              'country_color_vid',
                                                              'strength',
                                                              'bitterness',
                                                              'density',
                                                              'favor',
                                                              'taste',
                                                              'aftertaste',
                                                              'composition',
                                                              'is_combined',
                                                              'country',
                                                              'type',
                                                              'vid',
                                                              'color')

            # Записываем каждую запись в файл
            for beer in beers:
                writer.writerow(beer)

        self.stdout.write(self.style.SUCCESS('Data exported successfully'))
