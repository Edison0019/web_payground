from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test','tssef@test.com','test134232&@')

    def test_registration_signal(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists,True)