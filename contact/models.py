#coding=utf-8

from django.db import models

class Depart(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Person(models.Model):
    empID = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100) 
    depart = models.ForeignKey(Depart)

    def __unicode__(self):
        return self.name

class DepartDetail(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    label = models.CharField(max_length=20)
    value = models.CharField(max_length=100)
    depart = models.ForeignKey(Depart)
    order = models.IntegerField(max_length=2)

class PersonDetail(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    label = models.CharField(max_length=20)
    value = models.CharField(max_length=100)
    person = models.ForeignKey(Person)
    order = models.IntegerField(max_length=2)




