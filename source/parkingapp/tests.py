from django.conf import settings
from django.contrib.auth.forms import UsernameField
from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Event,ParkingLot,ParkingLotEventData,ParkingSpot

User = get_user_model()

class BasicTests(TestCase):
    
    @classmethod
    def setUp(self):
        testuser = User(username = "testuser", email = 'parkingapp@group7.com')
        testuser.is_staff = True
        testuserid = testuser.id
        self.testuserid = testuserid
        testuser.is_superuser = True
        testuser_pw = "123randomuser"
        self.testuser_pw = testuser_pw
        testuser.set_password(testuser_pw)
        testuser.isSupervisor = True
        testuser.balance = 100.00
        testuser.save()
        self.testuser = testuser
        
        event = Event(supervisor = testuser, name = 'aggie test event', address = '123 aggieroad', date = '2021-04-19')
        event.save()
        
        parking_lot = ParkingLot(owner = testuser, nickname = 'test nickname', address = '123 aggieroad', numMotorcycleSpots = 12, numCarSpots = 10, 
            numOversizeSpots = 5, motorcycleSpotPrice = 5.50, carSpotPrice = 10.50, oversizeSpotPrice = 15.50)
        parking_lot.save()

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertNotEquals(user_count,0)
        all_users = User.objects.all()
        for i in all_users:
            print(i)
        print("\n================== User Exists Test:PASSED ==================")

    def test_user_password(self):
        user_pw = User.objects.get(username="testuser")
        self.assertTrue(user_pw.check_password(self.testuser_pw))
        print("\n================== Password Test:PASSED ==================")
    
    def test_event(self):
        events = Event.objects.all()
        event_count = Event.objects.all().count
        print(event_count)
        for i in events:
            print(i)
        self.assertNotEquals(event_count,0)
        print("\n================== Event Test:PASSED ==================")

    def test_event_supervisor(self):
        super_event = Event.objects.get(supervisor = self.testuser)
        all_events = Event.objects.all()
        self.assertTrue(super_event is not None)
        print("All events in database:")
        for i in all_events:
            print(i)
        print("\n================== Supervisor Event Test:PASSED ==================")

    def test_parkinglot(self):
        parkinglot = ParkingLot.objects.get(owner = self.testuser)
        parkinglots = ParkingLot.objects.all()
        self.assertTrue(parkinglot is not None)
        print("All parking lots in database:")
        for i in parkinglots:
            print(i)
        print("\n================== Parking Lot Test:PASSED ==================")


    
