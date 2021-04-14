from django.test import TestCase

from .models import Profile, Event, User

class BasicTest(TestCase):

    @classmethod
    def setupTestData(cls):
        testuser = User.objects.create_user(username = "testuser", password ="12345")
        testuser2 = User.objects.create_user(username = "testuser2", password ="12345")
        testuser3 = User.objects.create_user(username = "testuser3", password ="12345")

        
        
    def test_events(self):
        event = Event()
        event.name = "FunEvent"
        event.address = "123 Main"
        event.date = "2021-03-03" 
        event.save()

        record = Event.objects.get(pk=event.pk)
        self.assertEqual(record,event)

    # def test_profile(self):
    #     profile = Profile()
    #     profile.balance = 12.12
    #     profile.isSupervisor = False
        
    #     profile.save()
        
    #     record = Profile.objects.get(pk=profile.pk)
    #     self.assertEqual(record,profile)


