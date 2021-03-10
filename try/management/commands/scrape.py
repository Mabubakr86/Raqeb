from django.core.management.base import BaseCommand
import requests
from parsel import Selector
from ...models import Gold


class Command(BaseCommand):
    help = "collect prices"
    # define logic of command

    def handle(self, *args, **options):
        url = "https://egypt.gold-price-today.com/"
        res = requests.get(url)

        sel = Selector(res.text)
        gold24_price = sel.xpath(
            """//table[@id="main-table"]/tbody/tr[1]/td[1]/text()""").extract_first().split()[0]
        gold21_price = sel.xpath(
            """//table[@id="main-table"]/tbody/tr[3]/td[1]/text()""").extract_first().split()[0]
        gold18_price = sel.xpath(
            """//table[@id="main-table"]/tbody/tr[4]/td[1]/text()""").extract_first().split()[0]

        gold24, created = Gold.objects.get_or_create(name='gold24')
        gold24.price = float(gold24_price)
        gold24.save()

        gold21, created = Gold.objects.get_or_create(name='gold21')
        gold21.price = float(gold21_price)
        gold21.save()

        gold18, created = Gold.objects.get_or_create(name='gold18')
        gold18.price = float(gold18_price)
        gold18.save()
