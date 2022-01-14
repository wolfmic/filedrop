from pyexpat import model
from django.db import models
import datetime


def expire():
    return datetime.datetime.today() + datetime.timedelta(days=1)

class File(models.Model):
    file = models.FileField(upload_to='uploads')
    expiration_date = models.DateTimeField(default=expire)
