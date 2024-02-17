from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('all-players/', views.all_players, name = 'all_players'),
    path('all-tournaments/', views.all_tournaments, name = 'all_tournaments'),
    path('add-player/', views.add_player, name = 'add_player'),
    path('add-tournament/', views.add_tournament, name='add_tournament'),
    path('add-to-play/', views.players_for_tournaments, name = 'players_for_t'),
    path('add-to-play/<int:tournament_id>/', views.show_pairs, name = 'show_pairs'),
    path('add-to-play/<int:tournament_id>/<int:res_id>/', views.enter_results, name='enter_results'),
]