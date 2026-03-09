from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class IftarTable(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=1000)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    governorate = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='iftar_photos/', null=True, blank=True)

