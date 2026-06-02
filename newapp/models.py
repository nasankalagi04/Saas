# Create your models here.
'''from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    billing_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name'''