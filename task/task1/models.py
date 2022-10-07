from django.db import models

# Create your models here.
class Plan(models.Model):
    amount = models.PositiveIntegerField()
    data = models.CharField(max_length=20)
    sms = models.IntegerField()
    roaming = models.CharField(max_length=20)
    subscription_choice =(
        ('yes','yes'),
        ('no','no')
    )
    subscription = models.CharField(max_length=20,choices=subscription_choice)

class Buyplan(models.Model):
    amount = models.PositiveIntegerField(null=True)
    data = models.CharField(max_length=20,null=True)
    sms = models.IntegerField(null=True)
    roaming = models.CharField(max_length=20,null=True)
    subscription = models.CharField(max_length=20,null=True)