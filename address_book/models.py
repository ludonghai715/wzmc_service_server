from django.db import models

# Create your models here.

class Person(models.Model):
    empID = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)

class PersonInfo(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    person = models.ForeignKey(Person)
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __unicode__(self):
        return "{'label':'"+self.label+"','value':'"+self.value+"'}"




