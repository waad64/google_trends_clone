from django.db import models

class SearchQuery(models.Model):
    keyword = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
from django.db import models

# Create your models here.
