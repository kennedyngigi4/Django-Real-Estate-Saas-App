from rest_framework import serializers
from apps.listings.models import *


class CountySerializer(serializers.ModelSerializer):

    class Meta:
        model = County
        fields = [ 'name', ]


class PropertyTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyType
        fields = ['name']


class CreatePropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = [
            "name","total_units","occupied_units","address","county","geo_location",
            "price", "description", "category", "propertytype","bedrooms","bathrooms",
            "main_photo","is_published",
        ]




