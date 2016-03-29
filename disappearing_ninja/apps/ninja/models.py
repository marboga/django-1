from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    creator = models.CharField(max_length=30)
    post = models.TextField(max_length=140)
    createdAt = models.DateTimeField(auto_now=True)
