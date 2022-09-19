
from django.db import models
from city.models import City,Competition


class Person(models.Model):
    name = models.CharField(max_length=124)
    field=models.CharField(max_length=40,null=True)
    contactno=models.CharField(max_length=40,null=True)
    email=models.EmailField(max_length=40,null=True)
    solo = models.BooleanField(default=1)
    
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True,default=None)
    competition= models.ManyToManyField(Competition, blank=True,default=None)
   
    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person)
    competition= models.ForeignKey(Competition,on_delete=models.SET_NULL,blank=True, null=True,default='')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True,default=None)

    def __str__(self):
        return self.name