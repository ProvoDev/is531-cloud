from django.db import models

# Create your models here.

class asset_catalog(models.Model):
  location = models.CharField(max_length=100)
  manufacturer = models.CharField(max_length=200)
  manufacturer_part_num = models.IntegerField()
  description = models.CharField(max_length=1000)
  date_implemented = models.DateField()
  maintenance_notes = models.CharField(max_length=1000)
  organization_tag = models.CharField(max_length=1000)