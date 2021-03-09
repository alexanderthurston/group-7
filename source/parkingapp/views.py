from django.shortcuts import render


# Homepage
def index(request):
    return render(request, "parkingapp/index.html")


# Login procedures
def sign_in(request):
    pass


# First time sign-up or updating account info
def sign_up_or_update_account(request):
    pass


# Account details
def account(request):
    pass


# Reserve parking spot
def reserve_spot(request):
    pass


# List lot and spots
def list_spot(request):
    pass

