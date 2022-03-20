from rest_framework import serializers
from .models import (
    Athlete,
    AthleteEvent,
    City,
    Event,
    Games,
    Team,
    Sport,
)

class AtheleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = [
            'name',
            'sex',
        ]

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'team',
            'noc',
        ]

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            'city',
        ]


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = [
            'sport',
        ]


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = [
            'year',
            'season',
        ]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'event',
            'sport',
            'city',
            'games',
        ]

class AthleteEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteEvent
        fields = [
            'athlete',
            'team',
            'weight',
            'height',
            'age',
            'medal',
            'event',
        ]
