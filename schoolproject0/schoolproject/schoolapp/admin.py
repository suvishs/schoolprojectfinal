from django.contrib import admin

# Register your models here.
from .models import department, employee

admin.site.register(department)
admin.site.register(employee)