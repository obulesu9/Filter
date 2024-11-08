from django.db import models

# Create your models here.
class  FilterModel(models.Model):
    name=models.CharField(max_length=50)
    eCount=models.IntegerField()
    subject=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    date=models.DateField()
 