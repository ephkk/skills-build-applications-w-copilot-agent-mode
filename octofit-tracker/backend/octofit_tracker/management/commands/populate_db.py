from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        activities = [
            Activity.objects.create(name='Running', type='Cardio'),
            Activity.objects.create(name='Swimming', type='Cardio'),
            Activity.objects.create(name='Weight Lifting', type='Strength'),
        ]

        # Create workouts
        Workout.objects.create(name='Morning Run', duration=30, user=users[0])
        Workout.objects.create(name='Evening Swim', duration=45, user=users[1])
        Workout.objects.create(name='Gym Session', duration=60, user=users[2])
        Workout.objects.create(name='Night Patrol', duration=90, user=users[3])

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=80)
        Leaderboard.objects.create(user=users[2], score=120)
        Leaderboard.objects.create(user=users[3], score=110)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
