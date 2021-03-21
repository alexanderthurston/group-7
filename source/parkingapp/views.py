from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from .models import User, UserType
# Homepage
def index(request):
    account = User.objects.get(username=request.POST['username'], password=request.POST['password'])
    account.logged_in = True
    context = {"account": account,}
    return render(request, "parkingapp/index.html", context)


# Login procedures
def sign_in(request):
    return render(request, "parkingapp/sign_in.html")


# First time sign-up
def create_account(request):
    pass

# Update account info
def update_account(request):
    pass

# Account details
def account_info(request, account_id):
    account = User.objects.get(pk=account_id)
    context = {'account': account, }
    return render(request, "parkingapp/account_info.html", context)



# Reserve parking spot
def reserve_spot(request):
    pass


# List lot and spots
def list_lot(request):
    pass

# Manage lot
def manage_lot(request):
    pass

# Supervisor overview
def overview(request):
    pass
