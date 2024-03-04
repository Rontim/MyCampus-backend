import random
from django import db
from django.db import models
from datetime import datetime


class Image(models.Model):
    image = models.ImageField(
        upload_to='blog/images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Image'
        verbose_name_plural = ('Images')
