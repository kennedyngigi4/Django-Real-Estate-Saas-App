from django.urls import path


from apps.listings.views import *
from apps.listings.views_realtors import *

urlpatterns = [

    # realtor links
    path( "county", CountyView.as_view(), name="county", ),
    path( "property_type", PropertyTypeView.as_view(), name="property_type", ),
    path( "property", PropertyView.as_view(), name="property", ),

    # user links

]



