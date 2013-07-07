#coding=utf-8

from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers
from contact.models import Person, PersonDetail, Depart, DepartDetail
import json

def person(request, keywords):
    persons = Person.objects.filter(name__contains=keywords)
    p_ = []
    for p in persons:
        temp = {'name': p.name, 'empId': p.empID, 'departID': p.depart.id, 'departName': p.depart.name, 'details':[]}
        details = PersonDetail.objects.filter(person_id=p.empID)
        for d in details:
            temp['details'].append({'label': d.label, 'value': d.value})    
        p_.append(temp)

    responseText =  json.dumps(p_)
    return HttpResponse(responseText)

def allDepart(request):
    departs = Depart.objects.all()
    d_ = []
    for d in departs:
        temp = {'name': d.name, 'id': d.id}
        d_.append(temp) 
    responseText = json.dumps(d_)
    return HttpResponse(responseText)

def depart(request, departID):
    depart = Depart.objects.get(pk=departID)
    details = DepartDetail.objects.filter(depart_id=departID)
    details_arr = []
    for d in details:
        details_arr.append({'label': d.label, 'value': d.value})
    d_ = {'name': depart.name, 'id': depart.id, 'details':details_arr}
    responseText = json.dumps(d_)
    return HttpResponse(responseText)

