from django.urls import path
from . import views

app_name = 'parkingapp'
urlpatterns = [
    path('', views.sign_in, name='sign-in'),
    path('index', views.index, name='index'),
    path('sign-up', views.sign_up, name="sign-up"),
    path('sign-out', views.sign_out, name="sign-out"),
    path('find-account', views.find_account, name="find-account"),
    path('create-account', views.create_account, name="create-account"),
    path('update-account', views.update_account, name="update-account"),
    path('account-info', views.account_info, name="account-info"),
    path('transfer-funds', views.transfer_funds, name="transfer-funds"),
    path('lot-attendant-home', views.lot_attendant_home, name="lot-attendant-home"),
    path('reserve-spot', views.reserve_spot, name="reserve-spot"),
    path('list-lot', views.list_lot, name="list-lot"),
    path('manage-lot', views.manage_lot, name="manage-lot"),
    path('supervisor-home', views.supervisor_home, name="supervisor-home"),
]