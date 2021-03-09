from django.urls import path

from . import views

app_name = 'parkingapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('sign-in', views.sign_in(), name='sign-in'),
    path('sign-in-update', views.sign_up_or_update_account(), name="sign-up-update"),
    path('account/<int:account_id>', views.account(), name="account"),
    path('reserve', views.reserve_spot(), name="reserve"),
    path('list', views.list_spot(), name="list"),
]