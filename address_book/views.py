#coding=utf-8

from django.http import HttpResponse
from django.utils import simplejson
from address_book.models import Person, PersonInfo
from django.core import serializers

def index(request):
    p = Person.objects.get()
    #infos = p.personinfo_set.all()
    return HttpResponse(serializers.serialize('json', p))
    #json = [{'label': '姓名', 'value': '船长'}, {'label':'电话', 'value': '234234'}]
    #return HttpResponse(simplejson.dumps(json, ensure_ascii=False))    
