import random

from django.core.management.base import BaseCommand

from tt_round_robin_app.models import Player


class Command(BaseCommand):
    help = 'Creates fake players'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='how many players needed')

    def handle(self, *args, **kwargs):
        number = kwargs['number']
        for i in range(1, number + 1):
            year = f'{2000 + i}-01-07'
            if i>=10:
                nt = 2
            else:
                nt = i
            player = Player(first_name=f'Name{i}',
                            last_name = f'Lastname{i}',
                            birthdate =year,
                            email=f'mail{i}@iii.ff',
                            phone=f'+7-{nt}{nt}{nt}-{nt}{nt}',
                            rating = 100 + i,
                            referee = bool(random.randint(0,1)))
            player.save()
        return f'{number} fake players created'