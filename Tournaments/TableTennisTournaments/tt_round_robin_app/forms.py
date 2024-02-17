from django import forms
import datetime
from django.forms import SplitDateTimeWidget


class EnterResultsForm(forms.Form):
    player1parties = forms.IntegerField(min_value=0, max_value=3)
    player2parties = forms.IntegerField(min_value=0, max_value=3)


class AddPlayerForm(forms.Form):
    first_name = forms.CharField(max_length=25, required=False, label='Name')
    patr_name = forms.CharField(max_length=25, required=False, label='Patronymic name')
    last_name = forms.CharField(max_length=50, required=True, label='Last name')
    birthdate = forms.DateField(initial=datetime.date.today)
    email = forms.EmailField(required=False)
    phone = forms.CharField(max_length=40, required=False)
    rating = forms.DecimalField(initial=0, decimal_places=2, required=False)
    photo = forms.ImageField(required=False)
    referee = forms.BooleanField(required=False, label='Mark if referee')
    information = forms.CharField(max_length=300, required=False, label='Additional information')


class AddTournamentForm(forms.Form):
    tournament_name = forms.CharField(required=True, label='Enter name of the tournament')
    date = forms.DateField(initial=datetime.date.today)


class UpdatePlayerForm(forms.Form):
    first_name = forms.CharField(max_length=25, required=False)
    patr_name = forms.CharField(max_length=25, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    age = forms.DateField(required=False)
    email = forms.EmailField(required=False)
    phone = forms.CharField(max_length=40, required=False)
    rating = forms.DecimalField(decimal_places=2, required=False)
    photo = forms.ImageField(required=False)
    referee = forms.BooleanField(required=False)
    information = forms.CharField(max_length=300, required=False)
