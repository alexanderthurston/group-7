from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from .models import User, UserType


# Homepage
def index(request, account_id):
    account = User.objects.get(pk=account_id)
    account.logged_in = True
    context = {"account": account, }
    return render(request, "parkingapp/index.html", context)


# Sign-in page | will display error message upon completion of view
def sign_in(request, error_message=""):
    context = {'error_message': error_message}
    return render(request, "parkingapp/sign_in.html", context)


# First time sign-up
def sign_up(request):
    return render(request, "parkingapp/sign_up.html")


# Create user account in system
def create_account(request):
    pass


# Find and verify user's account in system
def find_account(request):
    # try:
    #     account = User.objects.get(username=request.POST['username'], password=request.POST['password'])
    #     return HttpResponseRedirect(reverse('parkingapp:index', args=[account.id]))
    # except(KeyError, User.DoesNotExist):   # Redirect user and alert them of invalid sign-in
    #     error_message = "Invalid sign-in credentials. Please Try Again"
    #
    #     # return HttpResponseRedirect(reverse('parkingapp:sign-in', args=[error_message]))

    account = User.objects.get(username=request.POST['username'], password=request.POST['password'])
    return HttpResponseRedirect(reverse('parkingapp:index', args=[account.id]))


# Update account info
def update_account(request, account_id):
    account = User.objects.get(pk=account_id)
    context = {'account': account, }
    return render(request, "parkingapp/update_account.html", context)


# Account details
def account_info(request, account_id):
    account = User.objects.get(pk=account_id)
    context = {'account': account, }
    return render(request, "parkingapp/account_info.html", context)

def transfer_funds(request, account_id):
    account = User.objects.get(pk=account_id)
    context = {'account': account, }
    return render(request, "parkingapp/transfer_funds.html", context)
# Reserve parking spot
def reserve_spot(request, account_id):
    account = User.objects.get(pk=account_id)
    context = {'account': account, }
    return render(request, "parkingapp/reserve_spot.html", context)


# List lot and spots
def list_lot(request, account_id):
    account = User.objects.get(pk=account_id)
    context = {'account': account, }
    return render(request, "parkingapp/list_lot.html", context)


# Manage lot
def manage_lot(request, account_id, lot_id):
    account = User.objects.get(pk=account_id)
    context = {'account': account, }
    return render(request, "parkingapp/manage_lot.html", context)

# Verification portal
def lot_attendant_home(request, account_id):
    account = User.objects.get(pk=account_id)
    context = {'account': account, }
    return render(request, "parkingapp/lot_attendant_home.html", context)


# Verification confirmation
def lot_attendant_confirmation(request):
    pass

# Supervisor view to create event
def create_event(request):
    pass


# Supervisor view to manage already listed events
def manage_event(request):
    pass


# Supervisor overview
def supervisor_home(request, account_id):
    account = User.objects.get(pk=account_id)
    context = {'account': account, }
    return render(request, "parkingapp/supervisor_home.html", context)