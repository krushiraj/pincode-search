from django.db import models

# Create your models here.
class PincodeRecord(models.Model):
    officetype_choices = (
        ('S.O', 'S.O'),
        ('B.O', 'B.O'),
        ('H.O', 'H.O')
    )

    deliverystatus_choices = (
        ('Delivery', 'DEL'),
        ('Non-Delivery', 'NOD')
    )

    officename = models.CharField(max_length=1024)
    pincode = models.CharField(max_length=6)
    officetype = models.CharField(max_length=3, choices=officetype_choices)
    deliverystatus = models.CharField(max_length=12, choices=deliverystatus_choices)
    divisionname = models.CharField(max_length=1024)
    regionname = models.CharField(max_length=1024)
    circlename = models.CharField(max_length=1024)
    taluk = models.CharField(max_length=1024)
    districtname = models.CharField(max_length=1024)
    statename = models.CharField(max_length=1024)