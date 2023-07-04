from rest_framework import serializers
from apps.accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [ 'email','name','phone', ]



class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        extra_kwargs = { 'write_only': { 'password': True }}
        fields = [ 'email','name','phone', 'is_realtor', 'password' ]


    def create(self, validated_data):
    
        if not validated_data['is_realtor']:
            user = User.objects.create_user(
                email=validated_data['email'],
                name=validated_data['name'],
                phone=validated_data['phone'],
                password=validated_data['password'],
            )

            return user

        else:
            user = User.objects.create_realtor(
                email=validated_data['email'],
                name=validated_data['name'],
                phone=validated_data['phone'],
                password=validated_data['password'],
            )

            return user






