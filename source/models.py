from django.db import models

# Create your models here.
class upload(models.Model):
    sourceName = models.CharField(max_length=200)
    uploadDate = models.DateTimeField('date upload')
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.sourceName

class download(models.Model):
    sourceName = models.CharField(max_length=200)
    downloadDate = models.DateField('date download')
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.sourceName

class source(models.Model):
    id = models.AutoField(primary_key=True)
    sourceName = models.CharField(max_length=200)

    def __str__(self):
        return self.sourceName
