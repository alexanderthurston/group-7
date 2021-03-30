from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
 

# This is how we store data that Django's default User class doesn't have built in.
# We can add more fields to this later if we need to
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Event(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    eventName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    eventDate = models.DateTimeField()

class ParkingLot(models.Model):
    eventID = models.ForeignKey(Event, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

class ParkingSpot(models.Model):
    parkingLotID = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    spaceCode = models.CharField(max_length=50)

class ParkingSpotType(models.Model):
    parkingSpotID = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    typeName = models.CharField(max_length=20)

class ParkingSpotHistory(models.Model):
    spotID = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    rentStartDate = models.DateTimeField()
    rentEndDate = models.DateTimeField()

class TransactionHistory(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    eventID = models.ForeignKey(Event, on_delete=models.CASCADE)
    parkingSpotID = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    transDate = models.DateTimeField()
    amount = models.DecimalField(decimal_places=2, max_digits=5)

class TransactionType(models.Model):
    transHistoryID = models.ForeignKey(TransactionHistory, on_delete=models.CASCADE)
    transTypeName = models.CharField(max_length=20) 
