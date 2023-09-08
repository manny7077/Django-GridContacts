from django.contrib import admin
from .models import Address, Stakeholder, Substation
# Register your models here.

admin.site.register(Address)
admin.site.register(Stakeholder)
admin.site.register(Substation)