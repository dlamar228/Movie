from django.urls import path , include

from . import views

urlpatterns = [
    path('account/registration/',views.UserRegistrtionView.as_view(), name = 'registration'),
    path('account/authorization/',views.UserAuthorizationView.as_view(), name = 'authorization'),
    path('account/logout/',views.logout, name = 'logout'),
]