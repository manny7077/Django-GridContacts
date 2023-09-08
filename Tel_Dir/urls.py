"""
URL configuration for Tel_Dir project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Plc.views import staff_details_view, login_view, staff_view,management_view,logout_view, edit_profile_form, edit_user
from Othergroupings.views import address_list, stakeholder_list, substation_list
from ServiceCentres.views import infirmary_view, MIS_view,systemCommunications_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', staff_details_view, name='staff_details'),
    path('login/', login_view, name='login'),
    path('staff/', staff_view, name='staff'),
    path('management/', management_view, name='management'),
    path('logout/', logout_view, name='logout'),
    path('edit_profile_form/<int:staff_number>/', edit_profile_form, name='edit_profile_form'),
    path('addresses/', address_list,name='address_list'),
    path('stakeholders/', stakeholder_list,name='stakeholder_list'),
    path('substations/', substation_list,name='substation_list'),
    path('edit_user/<int:staff_number>/', edit_user, name='edit_user'), 
    path('infirmary/', infirmary_view, name='infirmary'), 
    path('mis/', MIS_view, name='mis'), 
    path('systemcommunications/', systemCommunications_view, name='systemcomm'), 
]
