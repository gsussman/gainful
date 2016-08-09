from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Student(models.Model):
 name = models.CharField(max_length=255, null=True)
 phone_number = models.CharField(max_length=25, null=True)
 email = models.EmailField(max_length=25, null=True)


 def __unicode__(self):
  return self.name

class Group(models.Model):
 name = models.CharField(max_length=255, null=True)
 member = models.ManyToManyField(Student, blank = True, related_name = 'member')

 def __unicode__(self):
  return self.name

class Message(models.Model):
 date = models.DateTimeField()
 message = models.CharField(max_length=255, null=True)
 audience_Individuals = models.ManyToManyField(Student, blank = True)
 audience_Groups =  models.ManyToManyField(Group, blank = True)

 def __unicode__(self):
  return self.message