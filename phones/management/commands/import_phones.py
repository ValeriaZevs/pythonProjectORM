import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            new_phone = Phone(int(phone['id']), phone['name'], int(phone['price']), phone['image'],
                              phone['release_date'], phone['lte_exists'], slugify(phone['name']))
            new_phone.save()
            pass
