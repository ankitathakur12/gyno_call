from django.db import models

# Create your models here.
class FileModel(models.Model):
    # name = models.CharField(max_length=50)
    face = models.FileField(upload_to='videos/')
    audio = models.FileField(upload_to='videos/')