from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=130)
    link1 = models.CharField(max_length=130)
    link2 = models.CharField(max_length=130)
    web = models.CharField(max_length=130)
    