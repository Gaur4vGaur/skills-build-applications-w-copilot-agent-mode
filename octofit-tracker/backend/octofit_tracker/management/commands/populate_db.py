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
            {"name": "Running", "duration": 30, "calories_burned": 300, "user": "user1@example.com"},
            {"name": "Cycling", "duration": 60, "calories_burned": 600, "user": "user2@example.com"},
        ]

        # Insert test data into the database
        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)

        self.stdout.write(self.style.SUCCESS('Test data successfully added to the database.'))
