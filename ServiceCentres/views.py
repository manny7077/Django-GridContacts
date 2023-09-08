from django.shortcuts import render
from .models import Infirmary, MIS, systemCommunications
# Create your views here.

def infirmary_view(request):
    infirmary= Infirmary.objects.all()
    return render(request, 'infirmary.html', {'infirmary':infirmary})


def MIS_view(request):
    mis= MIS.objects.all()
    return render(request, 'mis.html', {'mis':mis})



def systemCommunications_view(request):
    systemcomm= systemCommunications.objects.all()
    return render(request, 'systemcomm.html', {'systemcomm':systemcomm})