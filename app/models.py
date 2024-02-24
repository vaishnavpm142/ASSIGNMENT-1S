# Importing necessary modules
from django.db import models

# UserAccount model for storing user information
class UserAccount(models.Model):
    # Fields for user account
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50, default='user', blank=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(default='')
    status = models.IntegerField(default=0, blank=True)
    branch = models.CharField(max_length=50, default='')

    class Meta:
        db_table = "useraccount"  # Setting table name in the database


# TempStatus model for storing temporary status of users
class TempStatus(models.Model):
    # Fields for temporary status
    username = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=(('Online', 'Online'), ('Offline', 'Offline')))

    class Meta:
        db_table = "temp_status"  # Setting table name in the database
