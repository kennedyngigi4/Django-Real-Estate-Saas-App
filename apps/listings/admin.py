from django.contrib import admin
from apps.listings.models import County, Property, PropertyType
# Register your models here.

admin.site.register(County)
admin.site.register(Property)
admin.site.register(PropertyType)



