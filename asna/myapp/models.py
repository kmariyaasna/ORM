from django.db import models
from django.contrib import admin
class vehicle_DB(models.Model):
    No_plate=models.CharField(max_length=10)
    Name=models.CharField(max_length=10)
    Phone_num=models.IntegerField()
    Bike_modal=models.CharField(max_length=10)
    Service_date=models.DateField()
    Service_cost=models.IntegerField()
    

class vehicle_DBAdmin(admin.ModelAdmin):
    list_display=["Name","No_plate","Phone_num","Bike_modal","Service_date","Service_cost"]
