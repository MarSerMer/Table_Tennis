# Generated by Django 4.2.10 on 2024-02-14 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('patr_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=40)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=6)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='players_photos/')),
                ('referee', models.BooleanField(default=False)),
                ('information', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament_name', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('chief_referee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tt_round_robin_app.player')),
                ('participants', models.ManyToManyField(related_name='participants', to='tt_round_robin_app.player')),
                ('second_place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='secondplace', to='tt_round_robin_app.player')),
                ('third_place_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='thirdplace', to='tt_round_robin_app.player')),
                ('third_place_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='thirdplaceagain', to='tt_round_robin_app.player')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='winner', to='tt_round_robin_app.player')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pl1_parties', models.PositiveIntegerField(default=0)),
                ('pl2_parties', models.PositiveIntegerField(default=0)),
                ('pl1_points', models.PositiveIntegerField(default=0)),
                ('pl2_points', models.PositiveIntegerField(default=0)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='firstplayer', to='tt_round_robin_app.player')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='secondplayer', to='tt_round_robin_app.player')),
                ('tournament_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tt_round_robin_app.tournament')),
            ],
        ),
    ]
