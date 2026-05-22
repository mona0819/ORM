from django.contrib import admin
from .models import Order_Database,Order_DatabaseAdmin
admin.site.register(Order_Database,Order_DatabaseAdmin)