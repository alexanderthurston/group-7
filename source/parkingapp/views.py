from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import decimal

from .forms import UserCreationFormExtended,EditProfileForm

from .models import Event, ParkingLot, ParkingLotEventData, ParkingSpot

from datetime import datetime


# Homepage
@login_required(login_url='parkingapp:sign-in')
def index(request):
    reservation_list = request.user.parkingspot_set.all()
    event_list = Event.objects.order_by('date')

    context = {"reservation_list": reservation_list,
               'event_list': event_list}
    return render(request, "parkingapp/index.html", context)


# Sign-in page
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
# @login_required
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


@login_required(login_url='parkingapp:sign-in')
def sign_out(request):
    logout(request)
    return redirect('parkingapp:sign-in')


# Update account info
@login_required(login_url='parkingapp:sign-in')
def update_account(request):

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('parkingapp:account-info')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'parkingapp/update_account.html',args)
    # context = {}

    # form = UserChangeForm()

    # if request.method == 'POST':
    #     form = UserChangeForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('parkingapp:account-info')
    #         # first_name = request.POST.get('first_name')
    #         # last_name = request.POST.get('last_name')
    #         # username = request.POST.get('username')
    #         # email = request.POST.get('email')
    #         # password = request.POST.get('password')
    # context = {'form': form}
    # return render(request, "parkingapp/update_account.html", context)


@login_required(login_url='parkingapp:sign-in')
def new_lot(request):
    context = {}
    return render(request, "parkingapp/new_lot.html", context)

# Creates a new parking lot, which can then be listed for events.
# Gets called by a form on the manage_lot page
@login_required(login_url='parkingapp:sign-in')
def create_lot(request):
    nickname = request.POST['lot_nickname']
    address = request.POST['lot_address']
    num_motorcycle_spots = request.POST['num-motorcycle-spots']
    num_car_spots = request.POST['num-car-spots']
    num_oversize_spots = request.POST['num-oversize-spots']
    motorcycle_spot_price = request.POST['motorcycle-spot-price']
    car_spot_price = request.POST['car-spot-price']
    oversize_spot_price = request.POST['oversize-spot-price']

    lot = ParkingLot(
        owner=request.user,
        nickname=nickname, 
        address=address,
        numMotorcycleSpots=num_motorcycle_spots,
        numCarSpots=num_car_spots,
        numOversizeSpots=num_oversize_spots,
        motorcycleSpotPrice=motorcycle_spot_price,
        carSpotPrice=car_spot_price,
        oversizeSpotPrice=oversize_spot_price
    )
    lot.save()

    return HttpResponseRedirect(reverse('parkingapp:manage-lot'))


# List an existing lot for an event
# This gets called by a form on the manage_lot page
@login_required(login_url='parkingapp:sign-in')
def list_lot(request, lot_id):
    lot = get_object_or_404(ParkingLot, pk=lot_id)
    event_id = request.POST['selected-event']
    distance_from_event = request.POST['distance-from-event']
    event = get_object_or_404(Event, pk=event_id)
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
        ParkingSpot(parkingLotEventData=lot_event_data, spotType='1', price=lot.motorcycleSpotPrice).save()
    for i in range(available_car_spots):
        ParkingSpot(parkingLotEventData=lot_event_data, spotType='2', price=lot.carSpotPrice).save()
    for i in range(available_oversize_spots):
        ParkingSpot(parkingLotEventData=lot_event_data, spotType='3', price=lot.oversizeSpotPrice).save()

    return HttpResponseRedirect(reverse('parkingapp:manage-lot'))


# View to create new event. Runs within the supervisor homepage
@login_required(login_url='parkingapp:sign-in')
def create_event(request):
    event_name = request.POST['event_name']
    event_address = request.POST['event_address']
    event_date = datetime.strptime(request.POST['event_date'], "%Y-%m-%d").date()

    event = Event(name=event_name, address=event_address, date=event_date)
    event.save()

    return HttpResponseRedirect(reverse('parkingapp:supervisor-home'))


# Supervisor overview
@login_required(login_url='parkingapp:sign-in')
def supervisor_home(request):
    event_list = Event.objects.order_by('date')
    context = {'event_list': event_list}
    return render(request, "parkingapp/supervisor_home.html", context)


# Manage lot
@login_required(login_url='parkingapp:sign-in')
def manage_lot(request):
    lot_list = request.user.parkinglot_set.all()
    event_list = Event.objects.order_by('date')
    lot_event_data_list = ParkingLotEventData.objects.filter(parkingLot__in=request.user.parkinglot_set.all())
    context = {'lot_list': lot_list, 'event_list': event_list, 'lot_event_data_list': lot_event_data_list}
    return render(request, "parkingapp/manage_lot.html", context)


# Reserve parking spot
@login_required(login_url='parkingapp:sign-in')
def reserve_spot(request):
    event_list = Event.objects.order_by('date')
    parking_list = []
    spot_type = None
    selected_event_id = None


    if request.method == 'POST':
        selected_event_id = request.POST['selected-event']
        spot_type = request.POST['spot-type']

        event = Event.objects.get(id=selected_event_id)
        if spot_type == "1":
            parking_list = event.parkingloteventdata_set.filter(
                availableMotorcycleSpots__gte=1
            ).order_by(
                '-distanceFromEvent'
            )
        elif spot_type == "2":
            parking_list = event.parkingloteventdata_set.filter(
                availableCarSpots__gte=1
            ).order_by(
                '-distanceFromEvent'
            )
        elif spot_type == "3":
            parking_list = event.parkingloteventdata_set.filter(
                availableOversizeSpots__gte=1
            ).order_by(
                '-distanceFromEvent'
            )

    context = {
        'event_list': event_list,
        'parking_list': parking_list,
        'spot_type': spot_type,
        'selected_event_id': selected_event_id
    }
    return render(request, "parkingapp/reserve_spot.html", context)


@login_required(login_url='parkingapp:sign-in')
def make_reservation(request, lot_data_id, selected_event_id, spot_type):
    lot_data = ParkingLotEventData.objects.get(id=lot_data_id)
    parking_spots = lot_data.parkingspot_set.filter(
            spotType=spot_type
        ).filter(
            renter=None
        )

    if spot_type == "1":
        lot_data.availableMotorcycleSpots = lot_data.availableMotorcycleSpots - 1
    elif spot_type == "2":
        lot_data.availableCarSpots = lot_data.availableCarSpots - 1
    else:
        lot_data.availableOversizeSpots = lot_data.availableOversizeSpots - 1
    lot_data.save()

    parking_spot = parking_spots[0]
    parking_spot.renter = request.user
    parking_spot.save()

    request.user.profile.balance -= parking_spot.price
    request.user.save()
    parking_spot.parkingLotEventData.parkingLot.owner.profile.balance += decimal.Decimal(0.75) * parking_spot.price
    parking_spot.parkingLotEventData.parkingLot.owner.save()
    # Add supervisor payment here

    return HttpResponseRedirect(reverse('parkingapp:index'))


@login_required(login_url='parkingapp:sign-in')
def transfer_funds(request):
    if request.method == "POST":
        amount_to_transfer = request.POST['amount']
        balance = request.user.profile.balance
        balance += decimal.Decimal(amount_to_transfer)
        request.user.profile.balance = balance
        request.user.save()
        return HttpResponseRedirect(reverse('parkingapp:account-info'))

    context = {}
    return render(request, "parkingapp/transfer_funds.html", context)


# Account details
@login_required(login_url='parkingapp:sign-in')
def account_info(request):
    context = {}
    return render(request, "parkingapp/account_info.html", context)


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
