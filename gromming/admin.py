from django.contrib import admin
from .models import CustomizePackage, ServiceType


# Register your models here.
admin.site.register(CustomizePackage)
admin.site.register(ServiceType)