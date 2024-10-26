from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=20, blank=True, null=True)  # Added phone field

    

class RegisterE(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name= models.CharField(max_length=255,blank=True,null=True)
    last_name= models.CharField(max_length=255,blank=True,null=True)
    email=models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Field to store the hashed password
    password_confirmation= models.CharField(max_length=128)  # Field to store the hashed passwor

    # Use set_password to hash the password before saving
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    # Use check_password to verify the password
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
