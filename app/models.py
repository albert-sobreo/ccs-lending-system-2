from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Admin_Account(models.Model):
    name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Request(models.Model):
    requested_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    instructor_in_charge = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    request_number = models.CharField(max_length=255, null=True)
    date_borrowed = models.DateField(null=True, blank=True)
    date_needed = models.DateField()
    date_returned = models.DateField(null=True, blank=True)
    time_in = models.TimeField()
    time_out = models.TimeField()
    device = models.ManyToManyField(Device)
    approved = models.BooleanField(null=True, blank=True)
    returned = models.BooleanField(null=True, blank=True)