from django.db import models

# Create your models here.
class Receipe(models.Model):
    Name=models.CharField(max_length=100)
    Description=models.TextField()
    Ingredients=models.TextField()
    Iamge=models.ImageField(upload_to='images/')