import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib import admin
from django.db import models

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Games(models.Model):
    year = models.IntegerField(
        verbose_name="Year",
        validators=[MinValueValidator(1896),
        max_value_current_year]
    )

    SEASON = (
        ("Summer", "Summer"),
        ("Winter", "Winter"),
    )
    season = models.CharField(verbose_name="Season", max_length=6, choices=SEASON)

    # @property
    # @admin.display(
    #     ordering='year',
    #     description='Games Year and Season',
    # )
    # def games(self):
    #     return f'{self.year} {self.season}'

    def __str__(self):
        return f'{self.year} {self.season}'

class Team(models.Model):
    team = models.CharField(verbose_name="Team", max_length=70)
    noc = models.CharField(verbose_name="NOC", max_length=3)

    def __str__(self):
        return f'{self.team}'

class Athlete(models.Model):
    name = models.CharField(verbose_name="Name", max_length=200)
    SEX = (
        ("M", "M"),
        ("F", "F"),
    )
    sex = models.CharField(verbose_name="Sex", max_length=1, choices=SEX)

    def __str__(self):
        return f'{self.name}'

class Sport(models.Model):
    sport = models.CharField(verbose_name="Sport", max_length=200)

    def __str__(self):
        return f'{self.sport}'

class City(models.Model):
    city = models.CharField(verbose_name="City", max_length=200)

    def __str__(self):
        return f'{self.city}'

class Event(models.Model):
    event = models.CharField(verbose_name="Event", max_length=200)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='sports')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='cities')
    games = models.ForeignKey(Games, on_delete=models.CASCADE, related_name='games')

    def __str__(self):
        return f'{self.event}'

class AthleteEvent(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='atheltes')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teams')
    weight = models.DecimalField(
        verbose_name='Weight',
        decimal_places=2,
        max_digits=5,
        null=True,
        blank=True
    )
    height = models.IntegerField(
        verbose_name="Height",
        validators=[MaxValueValidator(300)],
        null=True, blank=True
    )
    age = models.IntegerField(
        verbose_name="Age",
        validators=[MaxValueValidator(100)],
        null=True,
        blank=True
    )

    MEDAL = (
        ("Gold", "Gold"),
        ("Silver", "Silver"),
        ("Bronze", "Bronze"),
        ("NA", "NA"),
    )
    medal = models.CharField(verbose_name="Medal", max_length=6, choices=MEDAL)

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='events'
    )

    def __str__(self):
        return f'{self.athlete} - {self.event}'
