from django.contrib import admin

from .models import User,UserType,Event,ParkingLot,ParkingSpot,ParkingSpotType,ParkingSpotHistory,TransactionHistory,TransactionType

admin.site.register(User)
admin.site.register(Event)
admin.site.register(ParkingLot)
admin.site.register(ParkingSpotHistory)
admin.site.register(TransactionHistory)


