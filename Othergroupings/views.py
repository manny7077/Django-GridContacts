from django.shortcuts import render
from .models import Address,Stakeholder,Substation
# Create your views here.


def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'address_list.html', {'addresses': addresses})


def stakeholder_list(request):
    stakeholders = Stakeholder.objects.all()
    return render(request, 'stakeholder_list.html', {'stakeholders': stakeholders})

def substation_list(request):
    substations = Substation.objects.all()
    return render(request, 'substation_list.html', {'substations': substations})