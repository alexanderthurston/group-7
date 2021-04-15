from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model
# from .models import Event

User = get_user_model()

class BasicTests(TestCase):
    
    @classmethod
    def setUp(self):
        testuser = User(username = "testuser", email = 'parkingapp@group7.com')
        
        # testuser2 = User.objects.create_user(username = "testuser2", password ="12345")
        # testuser3 = User.objects.create_user(username = "testuser3", password ="12345")
        testuser.is_staff = True
        testuser.is_superuser = True
        testuser.set_password("123randomuser")
        testuser.save()

        

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)


    # def test_events(self):
    #     event = Event()
    #     event.name = "FunEvent"
    #     event.address = "123 Main"
    #     event.date = "2021-03-03" 
    #     event.save()

    #     record = Event.objects.get(pk=event.pk)
    #     self.assertEqual(record,event)
