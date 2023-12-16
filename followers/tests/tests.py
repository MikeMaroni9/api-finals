from django.test import TestCase
from django.contrib.auth.models import User
from followers.models import Follower
from django.utils import timezone
from time import sleep

class FollowerModelTest(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='cheko', password='qweqwe123123')

    def test_follower_creation(self):
        # Create another user for testing
        other_user = User.objects.create_user(username='other_user', password='password123')

        # Create a Follower instance
        follower = Follower.objects.create(owner=self.user, followed=other_user)

        # Check that the Follower instance was created successfully
        self.assertEqual(follower.owner, self.user)
        self.assertEqual(follower.followed, other_user)
        self.assertIsNotNone(follower.created_at)

    def test_unique_together_constraint(self):
        # Try to create a Follower instance with the same owner and followed users
        with self.assertRaises(Exception):
            Follower.objects.create(owner=self.user, followed=self.user)
            Follower.objects.create(owner=self.user, followed=self.user)

    def test_follower_ordering(self):
        # Create Follower instances
        follower1 = Follower.objects.create(owner=self.user, followed=User.objects.create_user(username='user1', password='password1'))
        sleep(1)  # Introduce a delay of 1 second
        follower2 = Follower.objects.create(owner=User.objects.create_user(username='user2', password='password2'), followed=self.user)

        # Check that Follower instances are ordered by creation time
        self.assertLessEqual(follower1.created_at, follower2.created_at)

    def test_follower_str_method(self):
        # Create another user for testing
        other_user = User.objects.create_user(username='other_user', password='password123')

        # Create a Follower instance
        follower = Follower.objects.create(owner=self.user, followed=other_user)

        # Check that the __str__ method returns the expected string
        expected_str = f'{self.user} {other_user}'
        self.assertEqual(str(follower), expected_str)