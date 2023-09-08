from django.db import models
# Create your models here.



class Address(models.Model):
    postal_address = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.postal_address


class Stakeholder(models.Model):
    stakeholder = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    external_lines = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)

    def __str__(self):
        return self.stakeholder


class Substation(models.Model):
    substation = models.CharField(max_length=100)
    station_nomenclature = models.CharField(max_length=100, blank="True")
    telephone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.substation
