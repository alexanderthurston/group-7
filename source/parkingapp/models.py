from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# This is how we store data that Django's default User class doesn't have built in.
# We can add more fields to this later if we need to
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    isSupervisor = models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Event(models.Model):
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.eventName + " " + self.eventDate

class ParkingLot(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    numMotorcycleSpots = models.IntegerField(default=0)
    numCarSpots = models.IntegerField(default=0)
    numOversizeSpots = models.IntegerField(default=0)
    motorcycleSpotPrice = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    carSpotPrice = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    oversizeSpotPrice = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)


class ParkingLotEventData(models.Model):
    parkingLot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    distanceFromEvent = models.DecimalField(max_digits=6, decimal_places=1)
    availableMotorcycleSpots = models.IntegerField()
    availableCarSpots = models.IntegerField()
    availableOversizeSpots = models.IntegerField()


# spotType is 1 for motorcycle, 2 for car, 3 for oversize
class ParkingSpot(models.Model):
    parkingLotEventData = models.ForeignKey(ParkingLotEventData, on_delete=models.CASCADE)
    renter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    spotType = models.CharField(max_length=1)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=1.0)
    confirmationCode = models.CharField(max_length=6)

