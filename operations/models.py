from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions.datetime import datetime

# Create your models here.
class Servis(models.Model):
    musteri_id = models.ForeignKey(User,on_delete = models.CASCADE)
    servis_tarihi = models.DateTimeField()
    
    class Meta:
        verbose_name_plural = "Servis Kayıtları"
    def __str__(self):
        return self.musteri_id