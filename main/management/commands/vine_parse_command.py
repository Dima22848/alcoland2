import csv
from django.core.management.base import BaseCommand

from main.models import Vine_characters
from main.parse.vine import vine_parse


class Command(BaseCommand):
    help = 'Export products data to a CSV file'

    def handle(self, *args, **kwargs):
        vine_parse.vine_array()
        for x in vine_parse.vine_list:
            Vine_characters.objects.create(name=x[0],
                                           price=x[1],
                                           color=x[2],
                                           country=x[3],
                                           alcogol_percentage=x[4],
                                           type=x[5],
                                           brand=x[6],
                                           sugar=x[7],
                                           region=x[8],
                                           style=x[9],
                                           sort=x[10],
                                           classification=x[11],
                                           image=x[12])

        # Открываем файл для записи данных
        with open('vine_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            # Записываем заголовки
            writer.writerow(['name',
                             'price',
                             'color',
                             'country',
                             'alcogol_percentage',
                             'type',
                             'brand',
                             'sugar',
                             'region',
                             'style',
                             'sort',
                             'classification',
                             ])

            vines = Vine_characters.objects.all().values_list('name',
                                                              'price',
                                                              'color',
                                                              'country',
                                                              'alcogol_percentage',
                                                              'type',
                                                              'brand',
                                                              'sugar',
                                                              'region',
                                                              'style',
                                                              'sort',
                                                              'classification',)

            # Записываем каждую запись в файл
            for vine in vines:
                writer.writerow(vine)

        self.stdout.write(self.style.SUCCESS('Data exported successfully'))