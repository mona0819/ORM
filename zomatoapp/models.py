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


