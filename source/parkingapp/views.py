from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

# Homepage
def index(request, account_id):
    account = get_object_or_404(account_id)
    context = {"logged_in": account.logged_in,
               }
    return render(request, "parkingapp/index.html")


# Login procedures
def sign_in(request):
    pass


# First time sign-up or updating account info
def create_or_update_account(request):
    pass


# Account details
def account(request):
    pass


# Reserve parking spot
def reserve(request):
    pass


# List lot and spots
def list(request):
    pass


# Supervisor overview
def overview(request):
    pass
