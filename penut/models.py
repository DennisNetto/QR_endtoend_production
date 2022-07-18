from django.db import models

# Create your models here.


class HumanStorage(models.Model):
    id_number = models.CharField(max_length=26)
    hash = models.CharField(max_length=64)
    First_name = models.CharField(max_length=22)
    Last_name = models.CharField(max_length=22)
    DOB = models.DateField()


class TokenStorage(models.Model):
    id_number = models.CharField(max_length=26)
    hash = models.CharField(max_length=64)
    QR = models.BinaryField()



