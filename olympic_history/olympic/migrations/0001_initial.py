# Generated by Django 4.0.3 on 2022-03-19 17:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import olympic_history.olympic.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('sex', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, verbose_name='Sex')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200, verbose_name='City')),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1896), olympic_history.olympic.models.max_value_current_year], verbose_name='Year')),
                ('season', models.CharField(choices=[('Summer', 'Summer'), ('Winter', 'Winter')], max_length=6, verbose_name='Season')),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(max_length=200, verbose_name='Event')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=70, verbose_name='Team')),
                ('noc', models.CharField(max_length=3, verbose_name='NOC')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=200, verbose_name='Event')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='olympic.city')),
                ('games', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='olympic.games')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sports', to='olympic.sport')),
            ],
        ),
        migrations.CreateModel(
            name='AthleteEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Weight')),
                ('height', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(300)], verbose_name='Height')),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Age')),
                ('medal', models.CharField(choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronze', 'Bronze'), ('NA', 'NA')], max_length=6, verbose_name='Medal')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atheltes', to='olympic.athlete')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='olympic.event')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='olympic.team')),
            ],
        ),
    ]
