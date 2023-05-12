from django.db import models


# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    balance = models.FloatField()
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.username


class consumption_record(models.Model):
    Time = models.DateTimeField()
    Recipient = models.CharField(max_length=45)
    Amount = models.IntegerField()
    Money = models.FloatField()
    secret_key = models.CharField(max_length=45)
    UserId = models.IntegerField()
    Airline_order = models.CharField(max_length=45)
    State = models.BooleanField()
