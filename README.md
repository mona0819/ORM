# Ex01 Django ORM Web Application
## Date: 30.04.2026

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```python
from django.db import models
from django.contrib import admin
class Order_Database(models.Model):
    Order_Id=models.IntegerField(primary_key=True)
    User_ID=models.IntegerField()
    Order_Date=models.DateTimeField(auto_now_add=True)
    Item_Name=models.CharField(max_length=100)
    Order_Qty=models.IntegerField()
    Unit_Price=models.DecimalField(max_digits=10,decimal_places=2)
    Total_Amount=models.DecimalField(max_digits=10,decimal_places=2)
    Delivery_Address=models.CharField(max_length=200)

class Order_DatabaseAdmin(admin.ModelAdmin):
    list_display=('Order_Id','User_ID','Order_Date','Item_Name','Order_Qty','Unit_Price','Total_Amount','Delivery_Address')
```
## ADMIN
```python
from django.contrib import admin
from .models import Order_Database,Order_DatabaseAdmin
admin.site.register(Order_Database,Order_DatabaseAdmin)
```


## OUTPUT
<img width="1920" height="1080" alt="Screenshot (153)" src="https://github.com/user-attachments/assets/06f688ff-9c73-4045-a610-182a22aa7dad" />
<img width="1920" height="1080" alt="Screenshot (152)" src="https://github.com/user-attachments/assets/4ec1eba5-66cd-4aa3-951e-e3660f3b27f9" />

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
