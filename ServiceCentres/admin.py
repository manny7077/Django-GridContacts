from django.contrib import admin
from .models import Infirmary, MIS, systemCommunications 
# Register your models here.
admin.site.register(Infirmary)
admin.site.register(MIS)
admin.site.register(systemCommunications)