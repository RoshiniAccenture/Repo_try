from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.workout.suggested_for.set([self.user])
        self.activity = Activity.objects.create(user=self.user, type='Test Activity', duration=10, date=timezone.now().date())
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=50)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Test Team')

    def test_activity_user(self):
        self.assertEqual(self.activity.user, self.user)

    def test_workout_suggested_for(self):
        self.assertIn(self.user, self.workout.suggested_for.all())

    def test_leaderboard_points(self):
        self.assertEqual(self.leaderboard.points, 50)
