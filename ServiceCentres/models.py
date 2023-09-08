from django.db import models

# Create your models here.
class Infirmary(models.Model):
    infirmary_section= models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    plc_number = models.CharField(max_length=20)
    
    def __str__(self):
        return self.infirmary_section
    class Meta:
        verbose_name_plural = 'Infirmaries'
        


class MIS(models.Model):
    service = models.CharField(max_length=100)
    service_description = models.CharField(max_length=100)
    plc_number = models.CharField(max_length=100)
    
    def __str__(self):
        return self.service
    class Meta:
        verbose_name_plural = 'MIS'
        
    
    
class systemCommunications(models.Model):
    service = models.CharField(max_length=100)
    service_description = models.CharField(max_length=100)
    plc_number = models.CharField(max_length=100)
    
    def __str__ (self):
        return self.service
    class Meta:
        verbose_name_plural='System Communications'