# import required libraries, and functions
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.listings.models import *
from apps.listings.serializers import *


"""==========================================================================
    REALTORS BUSINESS LOGIC FUNCTIONS
    We have all realtors logics on listings here
=========================================================================="""


class CountyView(generics.ListCreateAPIView):
    queryset = County.objects.all()
    serializer_class = CountySerializer
    permission_classes = [ IsAuthenticated ]

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = CountySerializer(data=request.data)
        if serializer.is_valid():
            
            if not request.user.is_realtor:

                return Response(
                    { 'errors': 'Sorry, you do not have permissions to create a county' },
                    status=status.HTTP_403_FORBIDDEN,
                )

            else:

                serializer.save(created_by=request.user)

                return Response(
                    { 'message': 'County created successfully' },
                    status=status.HTTP_201_CREATED,
                )
            
        else:
            return Response({
                "message": 'failed',
                "errors": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            })

    def get_queryset(self):
        return County.objects.filter(created_by=self.request.user)
    


class PropertyTypeView(generics.ListCreateAPIView):

    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    permission_classes = [ IsAuthenticated ]

    def post(self, request, *args, **kwargs):

        serializer = PropertyTypeSerializer(data=request.data)
        if serializer.is_valid():
            
            if not request.user.is_realtor:

                return Response(
                    { 'errors': 'Sorry, you do not have permissions to create a property type' },
                    status=status.HTTP_403_FORBIDDEN,
                )

            else:

                serializer.save(created_by=request.user)

                return Response(
                    { 'message': 'County created successfully' },
                    status=status.HTTP_201_CREATED,
                )
            
        else:
            return Response({
                "message": 'failed',
                "errors": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            })

    def get_queryset(self):
        return PropertyType.objects.filter(created_by=self.request.user)
    


class PropertyView(generics.ListCreateAPIView):

    queryset = Property.objects.all()
    serializer_class = CreatePropertySerializer
    permission_classes = [ IsAuthenticated ]

    def post(self, request):
        print(request.data)
        serializer = CreatePropertySerializer(data=request.data)
        
        if serializer.is_valid():

            if not request.user.is_realtor:

                return Response({
                    "message": "failed",
                    "error": "You do not have permissions to create a property",
                    "status": status.HTTP_403_FORBIDDEN
                })
            
            else:
                serializer.save(created_by=request.user)

                return Response({
                    "message": "success",
                    "status": status.HTTP_201_CREATED
                })
            

        else:
            return Response({
                "message": "failed",
                "error": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            })



    def get_queryset(self):
        return Property.objects.filter(created_by=self.request.user).order_by('-date_created')



