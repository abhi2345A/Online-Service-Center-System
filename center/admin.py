from django.contrib import admin
from .models import Product, Repair, Complaint

# Register your models here.
admin.site.register(Product)
admin.site.register(Repair)
admin.site.register(Complaint)
