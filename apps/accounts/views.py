from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import *
from apps.accounts.serializers import *
# Create your views here.


class UserRegistration(APIView):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    def post(self, request):
        # try:
        print(request.data)
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                'message': 'success',
                'status': status.HTTP_201_CREATED
            })
        
        else:
            return Response({
                'message': 'failed',
                'errors': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST
            })

        # except:
        #     return Response(
        #         { 'error': 'Something went wrong, try again'},
        #         status=status.HTTP_500_INTERNAL_SERVER_ERROR
        #     )
