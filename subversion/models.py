from __future__ import unicode_literals
import django.utils.timezone as timezone
from django.db import models
# Create your models here.

class Subversion(models.Model):
	created_time = models.DateTimeField(default=timezone.now)
	svn_enname = models.CharField(max_length=200)
	code_type = models.CharField(max_length=5)
	svn_company = models.CharField(max_length=200)
	svn_zhname = models.CharField(max_length=200)
	svn_url = models.CharField(max_length=200)
	jira_url = models.CharField(max_length=200)
	note = models.CharField(max_length=500)
	
	def __unicode__(self):
		return self.svn_enname
