from django.test import TestCase
from django.forms.models import model_to_dict
from nose.tools import eq_, ok_
from .factories import (
    AthleteEventFactory,
    AthleteFactory,
    CityFactory,
    EventFactory,
    GamesFactory,
    TeamFactory,
    SportFactory,
)

from ..serializers import (
    AthleteSerializer,
    AthleteEventSerializer,
    CitySerializer,
    EventSerializer,
    GamesSerializer,
    TeamSerializer,
    SportSerializer,
)


class TestAthleteSerializer(TestCase):
    def setUp(self):
        self.athlete_data = model_to_dict(AthleteFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = AthleteSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_empty_data(self):
        serializer = AthleteSerializer(data=self.athlete_data)
        ok_(serializer.is_valid())
