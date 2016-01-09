from django.core.management.base import BaseCommand


class MySubcommand(BaseCommand):
    help = 'My Sub Command'

    def handle(self, *args, **options):
        self.stdout.write('OK')
