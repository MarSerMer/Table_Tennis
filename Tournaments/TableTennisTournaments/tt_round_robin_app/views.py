from django.forms import Form
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from .forms import EnterResultsForm, AddPlayerForm, AddTournamentForm
from .models import Player, Tournament, Result


def all_players(request):
    players = Player.objects.all()
    context = {'players': players}
    return render(request, 'tt_round_robin_app/all_players.html', context=context)


def all_tournaments(request):
    tournaments = Tournament.objects.all()
    context = {'tournaments': tournaments}
    return render(request, 'tt_round_robin_app/all_tournaments.html', context=context)


def add_player(request):
    if request.method == 'POST':
        form = AddPlayerForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            patr_name = form.cleaned_data['patr_name']
            last_name = form.cleaned_data['last_name']
            birthdate = form.cleaned_data['birthdate']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            rating = form.cleaned_data['rating']
            referee = form.cleaned_data['referee']
            information = form.cleaned_data['information']
            photo = form.cleaned_data['photo']
            new_player = Player(first_name=first_name,
                                patr_name=patr_name,
                                last_name=last_name,
                                birthdate=birthdate,
                                email=email,
                                phone=phone,
                                rating=rating,
                                referee=referee,
                                information=information,
                                photo=photo)
            new_player.save()
            return HttpResponse('<h3> New player added</h3>')
        return HttpResponse('<h3> Problems with validation</h3>')
    else:
        form = AddPlayerForm()
        message = 'Please enter information about new player'
        return render(request, 'tt_round_robin_app/add_player.html', {'form': form, 'message': message})


def add_tournament(request):
    if request.method == 'POST':
        form = AddTournamentForm(request.POST)
        if form.is_valid():
            tournament_name = form.cleaned_data['tournament_name']
            date = form.cleaned_data['date']
            new_tournament = Tournament(tournament_name=tournament_name,
                                        date=date)
            new_tournament.save()
            return HttpResponse('<h3> New tournament added</h3>')
        return HttpResponse('<h3> Problems with validation</h3>')
    else:
        form = AddPlayerForm()
        message = 'Please enter information about new player'
        return render(request, 'tt_round_robin_app/add_player.html', {'form': form, 'message': message})


def players_for_tournaments(request):
    players_all = Player.objects.all()
    tournament = Tournament.objects.filter().last()
    participants = tournament.participants.all()
    players = []
    if request.method == "POST":
        pl_id = request.POST['player_id']
        player_to_add = Player.objects.filter(pk=pl_id).first()
        print(player_to_add)
        tournament.participants.add(player_to_add)
        for pl in players_all:
            if pl not in participants:
                players.append(pl)
        context = {
            'players': players,
            'tournament': tournament,
            'participants': participants}
        return render(request, 'tt_round_robin_app/players_for_tournament.html', context=context)
    else:
        for pl in players_all:
            if pl not in participants:
                players.append(pl)
        context = {'players': players,
                   'tournament': tournament,
                   'participants': participants}
        return render(request, 'tt_round_robin_app/players_for_tournament.html', context=context)


def create_pairs(tournament_id):
    tournament = Tournament.objects.filter(pk=tournament_id).first()
    participants = tournament.participants.all()
    results_of_tournament: list[Result] = []
    for i in range(len(participants) - 1):
        for j in range(i, len(participants) - 1):
            res = Result(tournament_id=tournament,
                         player1=participants[i],
                         player2=participants[j + 1])
            res.save()
            results_of_tournament.append(res)
    return results_of_tournament


#
def show_pairs(request, tournament_id):
    tournament = Tournament.objects.filter(pk=tournament_id).first()
    participants = tournament.participants.all()
    results_of_tournament = Result.objects.filter(tournament_id=tournament)
    if not results_of_tournament:
        results_of_tournament = create_pairs(tournament_id)
    res_to_be_filled: list[Result] = []
    res_entered: list[Result] = []
    for res in results_of_tournament:
        if res.pl1_parties == 0 and res.pl2_parties == 0:
            res_to_be_filled.append(res)
        else:
            res_entered.append(res)
    if len(res_to_be_filled) == 0:
        players_points_in_tournament: list[str] = []
        for person in participants:
            person_points: int = 0
            person_parties: int = 0
            for ready_res in res_entered:
                if ((person == ready_res.player1 and ready_res.pl1_points == 1) or
                        (person == ready_res.player2 and ready_res.pl2_points == 1)):
                    person_points += 1
                if (person == ready_res.player1):
                    person_parties += ready_res.pl1_parties
                if (person == ready_res.player2):
                    person_parties += ready_res.pl2_parties
            answer = f'{person.first_name} {person.last_name} ---> parties {person_parties} --- > POINTS: {person_points}'
            players_points_in_tournament.append(answer)
        context = {'tournament': tournament,
                   'participants': participants,
                   'players_points_in_tournament': players_points_in_tournament,
                   'res_entered': res_entered}
        return render(request, 'tt_round_robin_app/finish_tournament.html', context=context)
    context = {'tournament': tournament,
               'participants': participants,
               'res_to_be_filled': res_to_be_filled,
               'res_entered': res_entered}
    return render(request, 'tt_round_robin_app/show_pairs.html', context=context)


def enter_results(request, res_id, tournament_id):
    result = Result.objects.filter(pk=res_id).first()
    if request.method == 'POST':
        # result = Result.objects.select(pk=res_id).first()
        form = EnterResultsForm(request.POST)
        if form.is_valid():
            result.pl1_parties = form.cleaned_data['player1parties']
            result.pl2_parties = form.cleaned_data['player2parties']
            if result.pl1_parties > result.pl2_parties:
                result.pl1_points = 1
            elif result.pl1_parties < result.pl2_parties:
                result.pl2_points = 1
            result.save()
        tournament_id = result.tournament_id.id
        return show_pairs(request, tournament_id)
    else:
        form = EnterResultsForm()
        context = {'form': form}
        template = 'tt_round_robin_app/enter_results.html'
        return render(request, template, context)


def index(request):
    return HttpResponse("Page Index of round robin app")


def about(request):
    return HttpResponse("Page About content")
