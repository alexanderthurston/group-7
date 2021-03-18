from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phoneNumber = models.IntegerField()
    logged_in = False


class UserType(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    typeName = models.CharField(max_length=10)

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
    amount = models.DecimalField()

class TransactionType(models.Model):
    transHistoryID = models.ForeignKey(TransactionHistory, on_delete=models.CASCADE)
    transTypeName = models.CharField(max_length=20) 
