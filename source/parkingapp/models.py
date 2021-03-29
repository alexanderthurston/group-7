from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phoneNumber = models.IntegerField()
    logged_in = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class UserType(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    typeName = models.CharField(max_length=10)

    # def __str__(self):
    #     return self.typeName
    

class Event(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    eventName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    eventDate = models.DateTimeField()

    # def __str__(self):
    #     return self.eventName + ' ' + self.eventDate

class ParkingLot(models.Model):
    eventID = models.ForeignKey(Event, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    
    # def __str__(self):
    #     return self.address

class ParkingSpot(models.Model):
    parkingLotID = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    spaceCode = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.spaceCode

class ParkingSpotType(models.Model):
    parkingSpotID = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    typeName = models.CharField(max_length=20)

    # def __str__(self):
    #     return self.typeName

class ParkingSpotHistory(models.Model):
    spotID = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    rentStartDate = models.DateTimeField()
    rentEndDate = models.DateTimeField()

    # def __str__(self):
    #     return self.rentStartDate + ' ' + self.rentEndDate
    

class TransactionHistory(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    eventID = models.ForeignKey(Event, on_delete=models.CASCADE)
    parkingSpotID = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    transDate = models.DateTimeField()
    amount = models.DecimalField(decimal_places=2, max_digits=5)

    # def __str__(self):
    #     return self.userID + ' ' + self.eventID + ' ' + self.transDate
    

class TransactionType(models.Model):
    transHistoryID = models.ForeignKey(TransactionHistory, on_delete=models.CASCADE)
    transTypeName = models.CharField(max_length=20) 

    # def __str__(self):
    #     return self.transTypeName
    