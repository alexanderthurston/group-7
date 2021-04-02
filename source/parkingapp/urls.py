from django.urls import path
from . import views

app_name = 'parkingapp'
urlpatterns = [
    path('', views.sign_in, name='sign-in'),
    path('index', views.index, name='index'),
    path('sign-up', views.sign_up, name="sign-up"),
    path('sign-out', views.sign_out, name="sign-out"),
    path('update-account', views.update_account, name="update-account"),
    path('account-info', views.account_info, name="account-info"),
    path('events', views.events, name="events"),
    path('transfer-funds', views.transfer_funds, name="transfer-funds"),
    path('lot-attendant-home', views.lot_attendant_home, name="lot-attendant-home"),
    path('reserve-spot', views.reserve_spot, name="reserve-spot"),
    path('manage-lot', views.manage_lot, name="manage-lot"),
    path('supervisor-home', views.supervisor_home, name="supervisor-home"),
    path('create-event', views.create_event, name="create-event"),
    path('create-lot', views.create_lot, name="create-lot"),
]