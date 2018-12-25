from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q

class Product(models.Model):
    product_type = models.CharField(max_length=100)
    brand = models.CharField(max_length=120)
    date_posted = models.DateTimeField(default=timezone.now)
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    model_no = models.CharField(max_length=100 ,validators=[alphanumeric])
    product_retailer = models.CharField(max_length=120)
    purchase_date = models.DateField(blank=False)
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    customer = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=39.99)

    def __str__(self):
        return f'{self.brand} product'

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk' : self.pk})


class Repair(models.Model):

    CHOICE_DEVICE = (
        ('Smartphone', 'Smartphone'),
        ('Desktop/Laptop', 'Desktop/Laptop'),
        ('Refrigerator', 'Refrigerator'),
        ('Television', 'Television'),
        ('Others', 'Others')
    )

    CHOICES = (
        ('Software', 'Software'),
        ('Hardware', 'Hardware'),
        ('Both', 'Both')
    )

    product_type = models.CharField(max_length=100, choices=CHOICE_DEVICE, default='Software')
    brand = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    description = models.TextField()
    option_field = models.CharField(max_length=100, choices=CHOICES, default='Smartphone')
    address = models.TextField()
    customer = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.brand} repair'

    def get_absolute_url(self):
        return reverse('repair-detail', kwargs={'pk' : self.pk})


class Complaint(models.Model):

    CHOICES = (
        ('1', 'Poor quality material or workmanship'),
        ('2', 'Alternate is not equal to brand specified'),
        ('3', 'Not operating properly - needs frequent repair'),
        ('4', 'Old or discolored stock'),
        ('5', 'Other'),
    )

    product_type = models.CharField(max_length=110)
    brand = models.CharField(max_length=100)
    choice_field = models.CharField(max_length=100, choices=CHOICES, default='1')
    complaint_description = models.TextField()
    purchase_date = models.DateField(blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_no = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    suggestions = models.TextField()
    customer = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.brand} complaint'

    def get_absolute_url(self):
        return reverse('complaint-detail', kwargs={'pk' : self.pk})


