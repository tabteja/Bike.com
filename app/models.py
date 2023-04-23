from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from app.managers import UserManager
from django.urls import reverse
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={'required': "Role must be provided"})
    email = models.EmailField(unique=True, blank=False,error_messages={'unique': "A user with that email already exists.",})

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()

    
BRAND = (
    ('Royal Enfield',"Royal Enfield"),
    ('Bajaj',"Bajaj"),
    ('Hero',"Hero"),
    ('Honda',"Honda"),
    ('Suzuki',"Suzuki"),
    ('TVS',"TVS"),
    ('Jawa',"Jawa"),
    ('Yamaha',"Yahama"),
)

MODEL_TYPE = (
    ('BS-1',"BS-1"),
    ('BS-2',"BS-2"),
    ('BS-3',"BS-3"),
    ('BS-4',"BS-4"),
    ('BS-5',"BS-5"),
    ('BS-6',"BS-6"),
)

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    

class Vehicle(models.Model):
    image1 = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    image3 = models.ImageField(upload_to='')
    title = models.CharField(max_length=100)
    brand = models.CharField(choices=BRAND, max_length=150)
    model_type = models.CharField(choices=MODEL_TYPE, max_length=150)
    model_year = models.IntegerField(('model_year'), validators=[MinValueValidator(2007), max_value_current_year])
    km_run = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    phone = models.IntegerField(null=True,blank=True)
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_year(self):
        return self.model_year.year

    def year_choices():
        return [(r,r) for r in range(2007, datetime.date.today().year+1)]

    
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
     
    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile_photo = models.ImageField(upload_to='')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    images = models.ImageField(upload_to='')
    description = models.CharField(max_length=500)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("post_details", kwargs={"id": self.id})
    
    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(Blog, self).save(*args, **kwargs)
     
    def __str__(self):
        return self.title
    

SERVICES = (
    ('Standard service - Rs.800',"Standard service - Rs.800"),
    ('Comprehesive service - Rs.1200',"Comprehesive service - Rs.1200"),
    ('Premium service - Rs.1500',"Premium service - Rs.1500"),
)

class Membership_Applicants(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(choices=SERVICES, max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


class Buyer_Applicants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    brand = models.CharField(choices=BRAND, max_length=150)
    model_type = models.CharField(choices=MODEL_TYPE, max_length=150)
    model_year = models.IntegerField()
    location = models.CharField(max_length=200)
    km_run = models.IntegerField()
    city = models.CharField(max_length=50)
    price = price = models.DecimalField(max_digits=7, decimal_places=2)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)
  
 
class Price_suggestion(models.Model):
    year = models.IntegerField()
    kilometers = models.IntegerField()


class Book(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,unique=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=350)
    service_date = models.CharField(max_length=50)
     
    def __str__(self):
        return self.email