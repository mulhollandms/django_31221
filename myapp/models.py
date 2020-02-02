from django.db import models
from django.contrib.postgres.fields import HStoreField

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=66)
    metadata = HStoreField(blank=True)