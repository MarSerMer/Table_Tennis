import random

from django.core.management.base import BaseCommand

from tt_round_robin_app.models import Tournament, Player


class Command(BaseCommand):
    help = 'Creates fake tournament'

    def handle(self, *args, **kwargs):
        year = '2024-01-17'
        # referee = Player(first_name = 'FakeChiefReferee',
        #                last_name = 'Changeable',
        #                referee=True)
        # other = Player(first_name = 'FakePlayer',
        #                last_name = 'Changeable',
        #                referee=False)
        tournament = Tournament(tournament_name=f'Test_tournament',
                                date=year,
                                # chief_referee=referee,
                                # winner=other,
                                # second_place=other,
                                # third_place_1=other)
                                )
        tournament.save()
        return f'Fake tournament created'
