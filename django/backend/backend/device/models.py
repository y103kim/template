from django.db import models

# Create your models here.

class Os(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    pub_date = models.DateTimeField('date published')

class Device(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    os = models.ForeignKey(Os, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
