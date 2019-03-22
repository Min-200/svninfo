from __future__ import unicode_literals
import django.utils.timezone as timezone
from django.db import models
# Create your models here.

class Joblist(models.Model):
	job_project = models.CharField(max_length=200)
        job_name = models.CharField(max_length=200, unique=True)
        job_url = models.CharField(max_length=1000)
        def __unicode__(self):
                return self.job_name

class Triggerbuild(models.Model):
	job_name = models.ForeignKey('Joblist', on_delete=models.CASCADE)
        job_build_time = models.DateTimeField(default=timezone.now)
        job_status  = models.CharField(max_length=200)
	job_num  = models.CharField(max_length=200)
	job_log  = models.CharField(max_length=1000)
        def __unicode__(self):
                return self.job_name

class Packageurl(models.Model):
	job_name = models.ForeignKey('Triggerbuild')
	package_url = models.CharField(max_length=500)
	package_md5 = models.CharField(max_length=100)
	package_name = models.CharField(max_length=100)
