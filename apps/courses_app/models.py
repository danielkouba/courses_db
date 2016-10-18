from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Description(models.Model):
	content = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Course(models.Model):
	name = models.CharField(max_length=100)
	description = models.OneToOneField(Description, on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)