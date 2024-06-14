# files/models.py
from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title

class Document(models.Model):
    title = models.CharField(max_length=255)
    document_file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title
