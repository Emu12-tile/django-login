from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
import uuid

# class CustomUser(AbstractUser):
#     pass

class RegisterE(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name= models.CharField(max_length=255,blank=True,null=True)
    email=models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Field to store the hashed password

    # Use set_password to hash the password before saving
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    # Use check_password to verify the password
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
