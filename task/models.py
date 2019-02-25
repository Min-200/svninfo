from __future__ import unicode_literals
import django.utils.timezone as timezone
from django.db import models

# Create your models here.


class Task(models.Model):
	created_time  = models.DateTimeField(default=timezone.now)
	task_name     = models.CharField(max_length=10)
	task_describe = models.CharField(max_length=20)
	task_host     = models.CharField(max_length=20)
	task_command  = models.CharField(max_length=200)
	
	def __unicode__(self):
                return "%s,%s,%s,%s,%s"%(self.created_time, self.task_name,self.task_describe,self.task_host,self.task_command)
