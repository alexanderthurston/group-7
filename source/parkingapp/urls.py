from django.urls import path
from . import views

app_name = 'parkingapp'
urlpatterns = [
    path('', views.sign_in, name='sign-in'),
    path('index/<int:account_id>', views.index, name='index'),
    path('sign-up', views.sign_up, name="sign-up"),
    path('find-account', views.find_account, name="find-account"),
    path('create-account', views.create_account, name="create-account"),
    path('update-account/<int:account_id>', views.update_account, name="update-account"),
    path('account-info/<int:account_id>', views.account_info, name="account-info"),
    path('transfer-funds/<int:account_id>', views.transfer_funds, name="transfer-funds"),
    path('lot-attendant-home/<account_id>', views.lot_attendant_home, name="lot-attendant-home"),
    path('reserve-spot/<int:account_id>', views.reserve_spot, name="reserve-spot"),
    path('list-lot/<int:account_id>', views.list_lot, name="list-lot"),
    path('manage-lot/<int:account_id>/<int:lot_id>', views.manage_lot, name="manage-lot"),
    path('supervisor-home/<int:account_id>', views.supervisor_home, name="supervisor-home"),
]