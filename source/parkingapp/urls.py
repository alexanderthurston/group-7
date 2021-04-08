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
    path('transfer-funds', views.transfer_funds, name="transfer-funds"),
    path('lot-attendant-home', views.lot_attendant_home, name="lot-attendant-home"),
    path('reserve-spot', views.reserve_spot, name="reserve-spot"),
    path('manage-lot', views.manage_lot, name="manage-lot"),
    path('supervisor-home', views.supervisor_home, name="supervisor-home"),
    path('create-event', views.create_event, name="create-event"),
    path('new-lot', views.new_lot, name="new-lot"),
    path('create-lot', views.create_lot, name="create-lot"),
    path('list-lot/<int:lot_id>/', views.list_lot, name="list-lot"),
    path('make-reservation/<int:lot_data_id>/<int:selected_event_id>/<str:spot_type>/', views.make_reservation, name="make-reservation"),
]