from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileModelTest(TestCase):

    def test_profile_creation(self):
        test_user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        test_profile = Profile.objects.get(owner=test_user)

        self.assertEqual(Profile.objects.filter(owner=test_user).count(), 1)
        self.assertEqual(test_profile.name, '')
        self.assertEqual(test_profile.content, '')
        self.assertEqual(str(test_profile), f"{test_user}'s profile")

    def test_profile_ordering(self):
        user1 = User.objects.create_user(username='user1', password='password1')
        user2 = User.objects.create_user(username='user2', password='password2')

        profile1 = Profile.objects.get(owner=user1)
        profile2 = Profile.objects.get(owner=user2)

        # Check that profiles are ordered by creation date in descending order
        self.assertGreater(profile2.created_at, profile1.created_at)

    def test_default_image_path(self):
        test_user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        test_profile = Profile.objects.get(owner=test_user)

        # Check the actual default image path set in the model
        self.assertEqual(test_profile.image.name, 'default_profile_qdjgyp')