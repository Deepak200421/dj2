from django.contrib import admin
from .models import Artist,Persons
# Register your models here.
admin.site.register(Artist)
admin.site.register(Persons)

from django.contrib import admin
from .models import Order

admin.site.register(Order)



