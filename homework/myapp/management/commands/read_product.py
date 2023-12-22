from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Product


class Command(BaseCommand):
    help = "Read a product by id"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.filter(pk=pk).first()
        self.stdout.write(f'{product}')