from django.urls import path
from apps.accounts.views import *

urlpatterns = [
    path( 'register/', UserRegistration.as_view(), name="register", ),
    # path( 'me', )
]






