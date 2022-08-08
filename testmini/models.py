from django.db import models


# Create your models here.
class Client(models.Model):
    fields = ('name', 'company', 'id', 'sum', 'date', 'service')
    name = models.CharField(max_length=60)
    company = models.CharField(max_length=60)
    client_id = models.CharField(max_length=60)
    sum = models.CharField(max_length=60)
    date = models.DateTimeField()
    service = models.CharField(max_length=60)

    def __str__(self):
        return self.name
