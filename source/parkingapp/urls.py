from django.urls import path

from . import views

app_name = 'parkingapp'
urlpatterns = [
    path('', views.sign_in, name='sign-in'),
    path('index', views.index, name='index'),
    path('create-account', views.create_account, name="create-account"),
    path('update-account/<int:account_id>', views.update_account, name="update-account"),
    path('account-info/<int:account_id>', views.account_info, name="account-info"),
    path('reserve-spot/<int:account_id>', views.reserve_spot, name="reserve-spot"),
    path('list-lot/<int:account_id>', views.list_lot, name="list-lot"),
    path('manage-lot/<int:account_id>/<int:lot_id>', views.manage_lot, name="manage-lot"),
]