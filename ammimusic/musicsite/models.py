from django.db import models
class NewRegister(models.Model):
    FirstName=models.CharField(max_length=100)
    MiddleName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Number=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    def _str_(self):
      return self.Email

class Mymedia(models.Model):
    song=models.CharField(max_length=100)
    singer=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    file=models.ImageField(upload_to = 'Songs/')
    rating=models.CharField(max_length=100)
    views=models.CharField(max_length=100)
    def _str_(self):
      return self.song
      



class umedia(models.Model):
    song=models.CharField(max_length=100)
    singer=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    file=models.ImageField(upload_to = 'Media/')
    rating=models.CharField(max_length=100)
    views=models.CharField(max_length=100)
    def _str_(self):
      return self.Email

# Create your models here.
