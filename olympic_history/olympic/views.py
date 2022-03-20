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
    AtheleteSerializer,
    AthleteEventSerializer,
    CitySerializer,
    EventSerializer,
    GamesSerializer,
    TeamSerializer,
    SportSerializer,
)

class AthleteViewSet(ModelViewSet):
    serializers_class = AtheleteSerializer
    queryset = Athlete.objects.all().order_by('name')

class AthleteEventViewSet(ModelViewSet):
    serializers_class = AthleteEventSerializer
    queryset = AthleteEvent.objects.all()

class CityViewSet(ModelViewSet):
    serializers_class = CitySerializer
    queryset = City.objects.all()

class EventViewSet(ModelViewSet):
    serializers_class = EventSerializer
    queryset = Event.objects.all()

class GamesViewSet(ModelViewSet):
    serializers_class = GamesSerializer
    queryset = Games.objects.all()

class TeamViewSet(ModelViewSet):
    serializers_class = TeamSerializer
    queryset = Team.objects.all()

class SportViewSet(ModelViewSet):
    serializers_class = SportSerializer
    queryset = Sport.objects.all()
