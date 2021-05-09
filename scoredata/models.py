from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone


class Scoresp(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    ver_no = models.IntegerField()
    ver_name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)
    level = models.IntegerField()
    score = models.IntegerField()
    pgreat = models.IntegerField()
    great = models.IntegerField()
    misscount = models.IntegerField(null=True)
    cleartype = models.CharField(max_length=200)
    djlevel = models.CharField(max_length=3, null=True)
    created_date = models.DateTimeField(default=timezone.now)

class Scoredp(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    ver_no = models.IntegerField()
    ver_name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)
    level = models.IntegerField()
    score = models.IntegerField()
    pgreat = models.IntegerField()
    great = models.IntegerField()
    misscount = models.IntegerField(null=True)
    cleartype = models.CharField(max_length=200)
    djlevel = models.CharField(max_length=3, null=True)
    created_date = models.DateTimeField(default=timezone.now)

class CsvUpload(models.Model):
    iidx_id = models.CharField(max_length=9, null=True, verbose_name='IIDX ID')
    uploaded = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        verbose_name='※CSV形式のみ対応',
        validators=[FileExtensionValidator(['csv',])],
        )
    created_date = models.DateTimeField(default=timezone.now)

class VersionList(models.Model):
    ver_no = models.IntegerField()
    ver_name = models.CharField(max_length=100, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ver_name

