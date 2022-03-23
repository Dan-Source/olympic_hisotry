from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from .models import (
    Athlete,
    AthleteEvent,
    City,
    Event,
    Games,
    Team,
    Sport,
)

from .serializers import (
    AthleteSerializer,
    AthleteEventSerializer,
    CitySerializer,
    EventSerializer,
    GamesSerializer,
    TeamSerializer,
    SportSerializer,
)

class AthleteViewSet(ModelViewSet):
    serializer_class = AthleteSerializer
    queryset = Athlete.objects.all().order_by('name')
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'name',
        'sex',
    ]


class AthleteEventViewSet(ModelViewSet):
    serializer_class = AthleteEventSerializer
    queryset = AthleteEvent.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'event__event',
        'event__sport',
        'athelte__name',
        'athelte__sex',
        'medal',
        'games__year',
        'games__season',
    ]

class CityViewSet(ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'city',
    ]

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'event',
        'sport',
        'city',
        'games__year',
        'games__season',
    ]

class GamesViewSet(ModelViewSet):
    serializer_class = GamesSerializer
    queryset = Games.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'year',
        'season',
    ]

class TeamViewSet(ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'team',
    ]

class SportViewSet(ModelViewSet):
    serializer_class = SportSerializer
    queryset = Sport.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'sport',
    ]
