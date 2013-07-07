#coding=utf-8

from django.db import models

TYPE_CHOICES = {
    ('p', '个人'),
    ('d', '部门'),
}

class Depart(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Contact(models.Model):
    id = models.IntegerField(max_length=10)
    number = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    depart = models.ForeignKey(Depart)
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    mobileShort = models.CharField(max_length=100)
    email = models.EmailField()




