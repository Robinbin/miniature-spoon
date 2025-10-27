from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='captain@marvel.com', name='Captain America', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='superman@dc.com', name='Superman', team='dc'),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user='Iron Man', activity_type='run', duration=30, date='2025-10-25'),
            Activity(user='Captain America', activity_type='cycle', duration=45, date='2025-10-24'),
            Activity(user='Batman', activity_type='swim', duration=20, date='2025-10-23'),
            Activity(user='Superman', activity_type='fly', duration=60, date='2025-10-22'),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        leaderboard = [
            Leaderboard(user='Iron Man', points=100),
            Leaderboard(user='Captain America', points=90),
            Leaderboard(user='Batman', points=95),
            Leaderboard(user='Superman', points=110),
        ]
        for lb in leaderboard:
            lb.save()

        # Workouts
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups', difficulty='easy'),
            Workout(name='Situps', description='Do 30 situps', difficulty='medium'),
            Workout(name='Squats', description='Do 40 squats', difficulty='hard'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
