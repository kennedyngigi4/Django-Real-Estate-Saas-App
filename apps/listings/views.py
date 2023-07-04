from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.listings.models import *
from apps.listings.serializers import *
# Create your views here.


"""==============================================================
    GENERAL USER BUSINESS LOGIC FUNCTIONS
    We have all user logics on listings here
==============================================================="""














