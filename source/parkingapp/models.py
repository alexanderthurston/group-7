from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phonenumber = models.IntegerField()

class UserType(models.Model):
    userID = models.ForeignKey(User,on_delete=models.CASCADE)
    typename = models.CharField(max_length=10)

class Event(models.Model):
    userID = models.ForeignKey(User,on_delete=models.CASCADE)
    eventname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    eventdate = models.DateTimeField()

class ParkingLot(models.Model):
    eventID = models.ForeignKey(Event,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

class ParkingSpot(models.Model):
    parkinglotID = models.ForeignKey(ParkingLot,on_delete=models.CASCADE)
    spacecode = models.CharField(max_length=50)

class ParkingSpotType(models.Model):
    parkingspotID = models.ForeignKey(ParkingSpot,on_delete=models.CASCADE)
    typename = models.CharField(max_length=20)

class ParkingSpotHistory(models.Model):
    spotID = models.ForeignKey(ParkingSpot,on_delete=models.CASCADE)
    rentstartdate = models.DateTimeField()
    rentenddate = models.DateTimeField()



class TransactionHistory(models.Model):
    userID = models.ForeignKey(User,on_delete=models.CASCADE)
    eventID = models.ForeignKey(Event,on_delete=models.CASCADE)
    parkSpotID = models.ForeignKey(ParkingSpot,on_delete=models.CASCADE)
    transDate = models.DateTimeField()
    amount = models.DecimalField()


class TransactionType(models.Model):
    transHistoryID = models.ForeignKey(TransactionHistory,on_delete=models.CASCADE)
    transTypeName = models.CharField(max_length=20) 



