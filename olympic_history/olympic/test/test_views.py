from django.urls import reverse, resolve
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
import factory
from .factories import (
    AthleteEventFactory,
    AthleteFactory,
    CityFactory,
    EventFactory,
    GamesFactory,
    TeamFactory,
    SportFactory,
)
from ..models import (
    Athlete,
    AthleteEvent,
    City,
    Event,
    Games,
    Team,
    Sport,
)

class TestAthleteListTestCase(APITestCase):
    def setUp(self):
        self.url = resolve('/api/v1/olympic/athlete/')
        self.athlete_data = factory.build(dict, FACTORY_CLASS=AthleteFactory)
    
    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.athlete_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        athlete = Athlete.objects.get(pk=response.data.get('id'))
        eq_(athlete.username, self.athlete_data.get('name'))
        eq_(self.athlete_data.get('sex'), athlete.sex)