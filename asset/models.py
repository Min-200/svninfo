from __future__ import unicode_literals
import django.utils.timezone as timezone
from django.db import models

# Create your models here.


class Asset(models.Model):
	created_time = models.DateTimeField(default=timezone.now)
	asset_name = models.CharField(max_length=10)
	asset_sou_ip = models.CharField(max_length=20)
	asset_sou_dir = models.TextField(max_length=200)
	asset_des_ip = models.CharField(max_length=100)
	asset_des_dir = models.TextField(max_length=200)
	asset_cron    = models.TextField(max_length=500)
	
	def __unicode__(self):
		return "%s,%s,%s,%s,%s,%s"%(self.asset_name, self.asset_sou_ip, self.asset_sou_dir, self.asset_des_ip, self.asset_des_dir,self.asset_cron)
