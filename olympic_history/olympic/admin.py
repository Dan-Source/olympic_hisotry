from django.contrib import admin
from .models import (
    Athlete,
    AthleteEvent,
    City,
    Event,
    Games,
    Team,
    Sport,
)

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ['id', 'games']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'team', 'noc']

@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sex']

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ['id', 'sport']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'city']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'sport', 'city', 'games']


@admin.register(AthleteEvent)
class AthleteEventAdmin(admin.ModelAdmin):
    list_display = ['id', 'athlete', 'team', 'weight','height', 'age', 'medal', 'event']
