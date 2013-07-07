#coding=utf-8

from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers
from address_book.models import Depart, Contact

def index(request):
#    p = Person.objects.get()
    #infos = p.personinfo_set.all()
    #return HttpResponse(serializers.serialize('json', p))
    return HttpResponse("hello")
    #json = [{'label': '姓名', 'value': '船长'}, {'label':'电话', 'value': '234234'}]
    #return HttpResponse(simplejson.dumps(json, ensure_ascii=False))    

def personContact(request, keywords):
    contacts = Contact.objects.filter(name__contains=keywords, type='p')
    json = serializers.serialize('json', contacts);
    return HttpResponse(json)

def allDepart(request):
    departs = Depart.objects.all()
    json = serializers.serialize('json', departs, fields=('id', 'name'), indent=2)
    return HttpResponse(json)

def departContact(request, departID):
    contacts = Contact.objects.filter(depart_id = departID,type='d')
    json = serializers.serialize('json', contacts)
    return HttpResponse(json)

