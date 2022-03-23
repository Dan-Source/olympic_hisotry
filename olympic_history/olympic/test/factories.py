import factory
import factory.fuzzy
import random
from olympic_history.olympic.models import (
    Athlete,
    AthleteEvent,
    City,
    Event,
    Games,
    Team,
    Sport,
)


def get_random_choice(obj):
    choice = [x for x in obj]
    return random.choice(choice)

class AthleteFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Athlete

    name = factory.Sequence(lambda n: 'AthelteTest%s' % n)
    sex = factory.fuzzy.FuzzyChoice(get_random_choice(Athlete.SEX))

class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Team

    team = factory.Sequence(lambda n: 'CountryTest%s' % n)
    noc = factory.LazyAttribute(lambda o: '%s' % o.team[0:3].upper())

class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    city = factory.Sequence(lambda n: 'CityTest%s' % n)

class SportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sport

    sport = factory.Sequence(lambda n: 'SportTest%s' % n)

class GamesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Games

    year = factory.fuzzy.FuzzyInteger(1896, 2016, step=4)
    season = factory.fuzzy.FuzzyChoice(get_random_choice(Games.SEASON))

class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    event = factory.Sequence(lambda n: 'EventTest%s' % n)
    sport = factory.SubFactory(SportFactory)
    city = factory.SubFactory(CityFactory)
    games = factory.SubFactory(GamesFactory)

class AthleteEventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AthleteEvent

    athlete = factory.SubFactory(AthleteFactory)
    team = factory.SubFactory(TeamFactory)
    weight = factory.fuzzy.FuzzyDecimal(40, 150)
    height = factory.fuzzy.FuzzyInteger(40, 300)
    age = factory.fuzzy.FuzzyInteger(10, 100)
    medal = factory.fuzzy.FuzzyChoice(get_random_choice(AthleteEvent.MEDAL))
    event = factory.SubFactory(EventFactory)







