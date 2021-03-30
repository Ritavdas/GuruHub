from django.db import models

# Create your models here.

class Card(models.Model):
   img = models.ImageField(upload_to='pics')
   name = models.CharField(max_length=20)
   desc = models.TextField()



class Tutor(models.Model):
   tid = models.IntegerField(primary_key = True)
   pic = models.ImageField(upload_to='pics')
   name = models.CharField(max_length=50)
   star = models.IntegerField()
   about = models.CharField(max_length=200)
   taught = models.IntegerField()
   rate = models.IntegerField()
   address = models.CharField(max_length=50)



class Subject(models.Model):

   tid = models.ForeignKey(Tutor, on_delete=models.CASCADE)
   subject = models.CharField(max_length=20)
   level = models.CharField(max_length=20)
   mode = models.CharField(max_length=20)


class Register(models.Model):
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   user_name = models.CharField(max_length=50)
   password= models.CharField(max_length=50)
   email = models.EmailField(max_length=50)






