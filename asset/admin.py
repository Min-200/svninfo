from django.contrib import admin

# Register your models here.
from .models import Asset

class Qaback(admin.ModelAdmin):
    list_display = ('created_time','asset_name','asset_sou_ip','asset_sou_dir','asset_des_ip','asset_des_dir','asset_cron')

admin.site.register(Asset, Qaback)
