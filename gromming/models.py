from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username


# Create your models here.
class ServiceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomizePackage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # User details
    fullname = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    address = models.TextField()

    # Pet details
    pet_name = models.CharField(max_length=100)
    TYPE_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('rabbit', 'Rabbit'),
        ('hamster', 'Hamster'),
        ('fish', 'Fish'),
        ('reptile', 'Reptile'),
        ('other', 'Other'),
    ]
    pet_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    pet_breed = models.CharField(max_length=100)
    pet_age = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    pet_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    pet_weight = models.IntegerField()
    pet_height = models.FloatField()
    pet_medical_condition = models.TextField()
    pet_vaccination_status = models.TextField()
    pet_image = models.ImageField(upload_to='pet_images/', null=True, blank=True)

    # Booking preferences
    booking_date = models.DateField()
    booking_time = models.TimeField()
    PACKAGE_CHOICES = [
        ('friendlypack', 'Friendlypack'),
        ('exclusivepack', 'Exclusivepack'),
        ('familypack', 'Familypack'),
        ('customizedpack', 'Customizepack'),
    ]
    package_type = models.CharField(max_length=100, choices=PACKAGE_CHOICES)

    # ✅ Multiple services selection via checkboxes
    services = models.ManyToManyField(ServiceType)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='updated soon') 



    def __str__(self):
        return self.fullname + " - " + self.pet_name
    




class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.service_name}"

  
    




