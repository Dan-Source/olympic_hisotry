from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import (
    AthleteViewSet,
    AthleteEventViewSet,
    CityViewSet,
    EventViewSet,
    GamesViewSet,
    TeamViewSet,
    SportViewSet,
)

router = SimpleRouter()

router.register(r'athlete', AthleteViewSet, basename="athelte")
router.register(r'athlete_event', AthleteEventViewSet, basename="athelte_event")
router.register(r'city', AthleteEventViewSet, basename="city")
router.register(r'event', EventViewSet, basename="event")
router.register(r'games', GamesViewSet, basename="games")
router.register(r'team', TeamViewSet, basename="team")
router.register(r'sport', SportViewSet, basename="sport")

urlpatterns = [
    path('', include(router.urls)),
]