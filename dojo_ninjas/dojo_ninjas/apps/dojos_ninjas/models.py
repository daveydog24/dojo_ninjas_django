from __future__ import unicode_literals
from django.db import models

class Dojos(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Ninja(models.Model):
    id = models.IntegerField(primary_key = True)
    dojo_id = models.ForeignKey(Dojos, related_name="Ninjas")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
