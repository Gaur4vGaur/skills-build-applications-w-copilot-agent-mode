from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Sample test data
        users = [
            {"email": "user1@example.com", "name": "User One", "age": 25},
            {"email": "user2@example.com", "name": "User Two", "age": 30},
        ]

        teams = [
            {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
        ]

        activities = [
            {"user": "user1@example.com", "activity": "Running", "duration": 30},
        ]

        leaderboard = [
            {"user": "user1@example.com", "points": 100},
        ]

        workouts = [
            {"name": "Morning Yoga", "duration": 60},
        ]

        # Insert data into collections
        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activity.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
