from django.contrib import admin
from address_book.models import Depart, Contact

class DepartAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class ContactAdmin(admin.ModelAdmin):
    list_display=['number', 'name', 'email']

admin.site.register(Depart, DepartAdmin)
admin.site.register(Contact, ContactAdmin)
