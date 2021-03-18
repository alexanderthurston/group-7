from django.urls import path

from . import views

app_name = 'parkingapp'
urlpatterns = [

    path('', views.sign_in, name='sign-in'),
    path('index', views.index, name='index'),
    path('sign-in-update', views.create_or_update_account, name="create-update"),
    path('account/<int:account_id>', views.account, name="account"),
    path('reserve', views.reserve, name="reserve"),
    path('list', views.list, name="list"),
]