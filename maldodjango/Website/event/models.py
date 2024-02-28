from typing import Any
from django.db import models

# Create your models here.
class Expriance(models.Model):
    text = models.CharField(max_length=100)
    Thumbnail = models.ImageField()
    html_link = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    des = models.TextField(null=True)
    def __str__(self) -> str:
        return self.text

class Oldies_Day(models.Model):
    image = models.ImageField()
    text = models.CharField(max_length =100)
    def __str__(self) -> str:
        return self.text

class workers_day(models.Model):
    image = models.ImageField()
    text = models.CharField(max_length =100)
    def __str__(self) -> str:
        return self.text
    
class Culture_Day(models.Model):
    image = models.ImageField()
    text = models.CharField(max_length =100)
    def __str__(self) -> str:
        return self.text
    
class prom(models.Model):
     image = models.ImageField()
     text = models.CharField(max_length =100)
     def __str__(self) -> str:
        return self.text

class Graduation(models.Model):
     image = models.ImageField()
     text = models.CharField(max_length =100)
     def __str__(self) -> str:
        return self.text
     


class homepage(models.Model):
    image=models.ImageField(upload_to='media/BG0A9014.JPG')
    text= models.CharField(max_length=100)
    des = models.TextField(null=True)
    def __str__(self) -> str:
        return self.text
class Futures(models.Model):
    description = models.TextField(null=True)
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
    


class About(models.Model):
    description = models.TextField(null=True)
    title = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.title


    

class contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    email  = models.EmailField( null=True)
    text  = models.TextField( null=True)

    def __str__(self) -> str:
        return self.name
    
class founders(models.Model):
    Names = models.CharField(max_length=100)
    occupatipon = models.CharField(max_length=200)
    img = models.ImageField()
    
    def __str__(self) -> str:
        return self.Names
    
class Titles(models.Model):
    title = models.CharField(max_length=100, null=True)
    title2= models.CharField(max_length=100, null=True)
    desc= models.TextField(null=True)
    desc2= models.TextField(null=True)

    def __str__(self) -> str:
        return self.title
    
    

