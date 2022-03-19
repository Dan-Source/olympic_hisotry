import factory
import random
from olympic_history.olympic.models import Athlete


def get_choice_athlete_sex():
    choice = [x[0] for x in Athlete.SEX]
    return random.choice(choice)

class AthleteFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Athlete

    name = factory.Sequence(lambda n: 'AthelteTest%s' % n)
    sex = factory.LazyFunction(get_choice_athlete_sex)

