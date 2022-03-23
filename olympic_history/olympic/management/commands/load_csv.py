import csv
from django.core.management import BaseCommand
from django.utils import timezone
from olympic_history.olympic.models import (
    Athlete,
    AthleteEvent,
    City,
    Event,
    Games,
    Team,
    Sport,
)

class Command(BaseCommand):
    help = "Loads athlete, city, sport, event, games, team from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def get_athletes(self):
        athletes = {athelte.id: athlete for athlete in Athlete.objects.all()}
        return athletes

    def csv_to_list(self, file_path):
        with open(file_path) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            csv_data = [line for line in reader]
        return csv_data

    def handle(self, *args, **options):
        start_time = timezone.now()
        file_path = options["file_path"]
        data = self.csv_to_list(file_path)

        count = 0
        flag = 500
        for item in data:

            athlete_name = item.get('Name')
            athlete_sex = item.get('Sex')
            athlete_obj, created = Athlete.objects.get_or_create(
                name=athlete_name,
                sex=athlete_sex,
            )

            team_name = item.get('Team')
            team_noc = item.get('NOC')
            team_obj, created= Team.objects.get_or_create(
                team=team_name,
                noc=team_noc,
            )

            games_year = item.get('Year')
            games_season = item.get('Season')
            games_obj, created = Games.objects.get_or_create(
                year=games_year,
                season=games_season,
            )

            sport_name = item.get('Sport')
            sport_obj, created = Sport.objects.get_or_create(
                sport=sport_name,
            )

            city_name = item.get('City')
            city_obj, created = City.objects.get_or_create(
                city=city_name,
            )

            event_name = item.get('Event')
            event_obj, created = Event.objects.get_or_create(
                event = event_name,
                sport = sport_obj,
                city = city_obj,
                games = games_obj,
            )

            medal = item.get('Medal')
            age = item.get('Age')
            if age == 'NA':
                age = None
            weight = item.get('Weight')
            if weight == 'NA':
                weight = None
            height = item.get('Height')
            if height == 'NA':
                height = None
            athlete_event_obj, created= AthleteEvent.objects.get_or_create(
                athlete = athlete_obj,
                team = team_obj,
                age = age,
                weight = weight,
                height = height,
                medal = medal,
                event = event_obj,
            )
            if count > flag:
                end_time = timezone.now()
                self.stdout.write(
                    self.style.WARNING(
                        f"Loading...{(end_time-start_time).total_seconds()} seconds. "+\
                        f"Added {count} items."
                    )
                )
                flag = flag + 500
            count+=1


        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )
