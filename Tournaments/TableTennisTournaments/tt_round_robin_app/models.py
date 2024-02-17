from django.db import models

# Create your models here.

from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=25, blank=False)
    patr_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50, blank=False)
    birthdate = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=40)
    rating = models.DecimalField(decimal_places=2, max_digits=6)
    photo = models.ImageField(upload_to='players_photos/', blank=True, null=True)
    referee = models.BooleanField(default=False)
    information = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birthdate}'

    def all_player_info(self):
        if self.referee:
            referee = 'судья'
        else:
            referee = 'не судья'
        return f'Игрок {self.first_name} {self.last_name} {self.patr_name}, возраст: {self.age}, статус: {referee}'


class Tournament(models.Model):
    tournament_name = models.CharField(null=False, max_length=150)
    date = models.DateField(null=False)
    participants = models.ManyToManyField(Player, related_name='participants')
    chief_referee = models.ForeignKey(Player, on_delete=models.PROTECT, null=True, blank=True)
    winner = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='winner', null=True, blank=True)
    second_place = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='secondplace', null=True,
                                     blank=True)
    third_place_1 = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='thirdplace', null=True,
                                      blank=True)
    third_place_2 = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='thirdplaceagain', null=True,
                                      blank=True)

    def __str__(self):
        return f'{self.tournament_name}, дата проведения: {self.date}, главный судья: {self.chief_referee}'

    def get_all_info(self):
        if self.third_place_2:
            add_3rd = f', {self.third_place_2}'
        else:
            add_3rd = ''
        return f'{self.tournament_name}, дата проведения: {self.date}, главный судья: {self.chief_referee}' \
               f'победитель: {self.winner} ' \
               f'призёры: {self.second_place}, {self.third_place_1}{add_3rd}.'


class Result(models.Model):
    tournament_id = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player1 = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='firstplayer', null=True, blank=True)
    player2 = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='secondplayer', null=True, blank=True)
    # в эти поля нужно вносить, сколько партий за игру выиграл каждый игрок (2 и 0, или 1 и 2 и так далее)
    pl1_parties = models.PositiveIntegerField(default=0)
    pl2_parties = models.PositiveIntegerField(default=0)
    # в эти поля победителю игры(!) ставится 1, проигравшему ставится 0.
    # Потом использовать при подсчёте очков за турнир
    pl1_points = models.PositiveIntegerField(default=0)
    pl2_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.player1} - {self.pl1_parties} : {self.player2} {self.pl2_parties}'

