from django.db import models

# Create your models here.
class UserOfSecondApp(models.Model):
    name = models.CharField(max_length=240)
    preferences = models.BooleanField(default=False)
    age = models.IntegerField()