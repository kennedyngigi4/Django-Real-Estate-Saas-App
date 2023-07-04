"""
Import required packages
 - uuid used to generate unique userid
 - timezone for getting the actual time in different timezones
"""

import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Creating a custom user model

class UserManager(BaseUserManager):
   
    def create_user(self, email, name, phone, password=None):
       
        if not email:
           raise ValueError("Email address is required")

        user = self.model(
            email=self.normalize_email(email).lower(),
            name=name,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
   
    
    def create_realtor(self, email, name, phone, password=None):

        if not email:
           raise ValueError("Email address is required")
        

        user = self.create_user(
            email=email,
            name=name,
            phone=phone,
            password=password,
        )

        user.is_realtor = True
        user.save(using=self._db)

        return user
    


    def create_superuser(self, email, name, phone, password=None):

        if not email:
           raise ValueError("Email address is required")
        

        user = self.create_user(
            email=email,
            name=name,
            phone=phone,
            password=password,
        )

        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    email = models.EmailField(null=True, unique=True)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_realtor  = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name','phone',
    ]


    def __str__(self):
        return self.email


    @property
    def is_staff(self):
        # all admins are staff
        return self.is_admin

