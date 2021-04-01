from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserCreationFormExtended

from .models import Event, ParkingLot, ParkingLotEventData, ParkingSpot


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


# Creates a new parking lot, which can then be listed for events.
# Gets called by a form on the manage_lot page
@login_required(login_url='parkingapp:sign-in')
def create_lot(request):
    nickname = request.POST['lot_nickname']
    address = request.POST['lot_address']
    num_motorcycle_spots = request.POST['num_motorcycle_spots']
    num_car_spots = request.POST['num_car_spots']
    num_oversize_spots = request.POST['num_oversize_spots']

    lot = ParkingLot(
        owner=User,
        nickname=nickname, 
        address=address,
        numMotorcycleSpots=num_motorcycle_spots,
        numCarSpots=num_car_spots,
        numOversizeSpots=num_oversize_spots
    )
    lot.save()

    return HttpResponseRedirect(reverse('parkingapp:manage-lot'))


# List an existing lot for an event
# This gets called by a form on the manage_lot page
@login_required(login_url='parkingapp:sign-in')
def list_lot(request, lot_id, event_id):
    lot = get_object_or_404(ParkingLot, pk=lot_id)
    event = get_object_or_404(Event, pk=event_id)
    distance_from_event = request.POST['distance_from_event']
    available_motorcycle_spots = lot.numMotorcycleSpots
    available_car_spots = lot.numCarSpots
    available_oversize_spots = lot.numOversizeSpots

    lot_event_data = ParkingLotEventData(
        parkingLot=lot,
        event=event,
        distanceFromEvent=distance_from_event,
        availableMotorcycleSpots=available_motorcycle_spots,
        availableCarSpots=available_car_spots,
        availableOversizeSpots=available_oversize_spots
    )
    lot_event_data.save()

    # Create the parking spots for this lot and event
    for i in range(available_motorcycle_spots):
        ParkingSpot(parkingLotEventData=lot_event_data, spotType='1', isTaken=False).save()
    for i in range(available_car_spots):
        ParkingSpot(parkingLotEventData=lot_event_data, spotType='2', isTaken=False).save()
    for i in range(available_oversize_spots):
        ParkingSpot(parkingLotEventData=lot_event_data, spotType='3', isTaken=False).save()

    return HttpResponseRedirect(reverse('parkingapp:manage-lot'))


# View to create new event. Runs within the supervisor homepage
@login_required(login_url='parkingapp:sign-in')
def create_event(request):
    pass


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


# Supervisor view to manage already listed events
@login_required(login_url='parkingapp:sign-in')
def manage_event(request):
    pass


# Supervisor overview
@login_required(login_url='parkingapp:sign-in')
def supervisor_home(request):
    context = {}
    return render(request, "parkingapp/supervisor_home.html", context)
