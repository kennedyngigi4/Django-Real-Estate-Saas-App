import uuid
from django.db import models
from django.utils import timezone
# Create your models here.

class County(models.Model):

    name = models.CharField(max_length=100, null=True)
    created_by = models.EmailField()

    def __str__(self):
        return str(self.name)

class PropertyType(models.Model):

    name = models.CharField(max_length=255, null=True)
    created_by = models.EmailField(null=True)

    def __str__(self):
        return self.name

class Property(models.Model):

    category_list = (
        ( 'For Sale', 'For Sale', ),
        ( 'For Rent', 'For Rent', ),
    )

    pid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=255, null=True)
    total_units = models.IntegerField(null=True, blank=True)
    occupied_units = models.IntegerField(null=True, blank=True)

    address = models.CharField(max_length=255, null=True)
    county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True)
    geo_location = models.CharField(max_length=255, null=True)

    price = models.IntegerField(null=True,)
    description = models.TextField(null=True)
    category = models.CharField(max_length=10, null=True, choices=category_list)
    propertytype = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    main_photo = models.ImageField(upload_to='properties', null=True,)

    is_published = models.BooleanField(default=False)
    created_by = models.EmailField(null=True)
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


    



