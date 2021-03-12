from django.db import models

# Create your models here.

class Card(models.Model):
   img = models.ImageField(upload_to='pics')
   name = models.CharField(max_length=20)
   desc = models.TextField()
