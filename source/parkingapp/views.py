from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.utils import timezone
from django.urls import reverse
# from .models import User, UserType
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserCreationFormExtended

# Homepage
@login_required(login_url='parkingapp:sign-in')
def index(request):
    # account = User.objects.get(pk=account_id)
    # account.logged_in = True
    context = {}
    return render(request, "parkingapp/index.html", context)


# Sign-in page | will display error message upon completion of view
def sign_in(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('parkingapp:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('parkingapp:index')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, "parkingapp/sign_in.html", context)

    return render(request, "parkingapp/sign_in.html", context)


# First time sign-up
def sign_up(request):
    if request.user.is_authenticated:
        return redirect('parkingapp:index')

    form = UserCreationFormExtended()

    if request.method == 'POST':
        form = UserCreationFormExtended(request.POST)
        if form.is_valid():
            form.save()
            # user = form.cleaned_data.get('username')
            # messages.success(request, 'Account was created for ' + user)
            return redirect('parkingapp:sign-in')

    context = {'form': form}
    return render(request, "parkingapp/sign_up.html", context)


def sign_out(request):
    logout(request)
    return redirect('parkingapp:sign-in')


# Update account info
@login_required(login_url='parkingapp:sign-in')
def update_account(request):
    context = {}

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
    return render(request, "parkingapp/update_account.html", context)


# Account details
@login_required(login_url='parkingapp:sign-in')
def account_info(request):
    context = {}
    return render(request, "parkingapp/account_info.html", context)


@login_required(login_url='parkingapp:sign-in')
def transfer_funds(request):
    context = {}
    return render(request, "parkingapp/transfer_funds.html", context)


# Reserve parking spot
@login_required(login_url='parkingapp:sign-in')
def reserve_spot(request,):
    context = {}
    return render(request, "parkingapp/reserve_spot.html", context)


# List lot and spots
@login_required(login_url='parkingapp:sign-in')
def list_lot(request):
    context = {}
    return render(request, "parkingapp/list_lot.html", context)


# Manage lot
@login_required(login_url='parkingapp:sign-in')
def manage_lot(request):
    context = {}
    return render(request, "parkingapp/manage_lot.html", context)


# Verification portal
@login_required(login_url='parkingapp:sign-in')
def lot_attendant_home(request):
    context = {}
    return render(request, "parkingapp/lot_attendant_home.html", context)


# Verification confirmation
@login_required(login_url='parkingapp:sign-in')
def lot_attendant_confirmation(request):
    pass


# Supervisor view to create event
@login_required(login_url='parkingapp:sign-in')
def create_event(request):
    pass


# Supervisor view to manage already listed events
@login_required(login_url='parkingapp:sign-in')
def manage_event(request):
    pass


# Supervisor overview
@login_required(login_url='parkingapp:sign-in')
def supervisor_home(request):
    context = {}
    return render(request, "parkingapp/supervisor_home.html", context)
