from rest_framework.viewsets import ModelViewSet

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

class AthleteEventViewSet(ModelViewSet):
    serializer_class = AthleteEventSerializer
    queryset = AthleteEvent.objects.all()

class CityViewSet(ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class GamesViewSet(ModelViewSet):
    serializer_class = GamesSerializer
    queryset = Games.objects.all()

class TeamViewSet(ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

class SportViewSet(ModelViewSet):
    serializer_class = SportSerializer
    queryset = Sport.objects.all()
