#coding=utf8
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Asset
import forms
from .forms import Assetadd
import models
import django.utils.timezone as timezone
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.decorators import permission_required



def index(request):
	print "1"
	print  request.user
	return render(request, 'index.html')

def asset_list(request):
	asset_list = Asset.objects.all()
	return render(request, 'tables.html',context ={ 'asset_list': asset_list})

def asset_l(request):
	asset_list = Asset.objects.all()
	return render(request, 'asset/asset_list.html',context ={ 'asset_list': asset_list})

def flot(request):
	return render(request, 'flot.html')

def morris(request):
	return render(request, 'morris.html')

@permission_required('asset.add_asset',raise_exception=True) #raise_exception=True 会抛出异常
def asset_add(request):
	if request.method == "POST":
			form = forms.Assetadd(request.POST)
			message = "请检查填写的内容！"
			if form.is_valid():
					asset_name = form.cleaned_data['asset_name']
					asset_sou_ip = form.cleaned_data['asset_sou_ip']
					asset_sou_dir = form.cleaned_data['asset_sou_dir']
					asset_des_ip = form.cleaned_data['asset_des_ip']
					asset_des_dir = form.cleaned_data['asset_des_dir']
					asset_cron    = form.cleaned_data['asset_cron']
			try:
				#print asset_name,asset_number,asset_source,asset_people,asset_application
					new = models.Asset.objects.create()
					new.asset_name = asset_name
					new.asset_sou_ip = asset_sou_ip
					new.asset_sou_dir = asset_sou_dir
					new.asset_des_ip = asset_des_ip
					new.asset_des_dir = asset_des_dir
					new.asset_cron = asset_cron
					new.save()
					return redirect('asset_list.html')
			except:
					message = ""
					return redirect('asset/asset_add.html')

	form = forms.Assetadd()
	return render(request, 'asset/asset_add.html', {'form' : form })

@permission_required('asset.change_asset',raise_exception=True)
def asset_mod(request,pk):
	asset = Asset.objects.get(pk=pk)
#	print asset.asset_application
	if request.method == "POST":
		form = forms.Assetadd(request.POST,initial = [{'asset_name': asset.asset_name,'asset_sou_ip': asset.asset_sou_ip,'asset_sou_dir':asset.asset_sou_dir,'asset_des_ip':asset.asset_des_ip,'asset_des_dir':asset.asset_des_dir,'asset_cron':asset.asset_cron}])
		if form.is_valid():
			asset.created_time = timezone.now()
			asset.asset_name = form.cleaned_data['asset_name']
			asset.asset_sou_ip = form.cleaned_data['asset_sou_ip']
			asset.asset_sou_dir = form.cleaned_data['asset_sou_dir']
			asset.asset_des_ip = form.cleaned_data['asset_des_ip']
			asset.asset_des_dir = form.cleaned_data['asset_des_dir']
			asset.asset_cron = form.cleaned_data['asset_cron']
			asset.save()
			return redirect('/asset_list')
#			return render(request, 'asset/asset_mod.html', {'form' : form ,'asset_name':asset.asset_name})
	
	form = forms.Assetadd(initial={
			'asset_name': asset.asset_name,
			'asset_sou_ip': asset.asset_sou_ip,
			'asset_sou_dir':asset.asset_sou_dir,
			'asset_des_ip':asset.asset_des_ip,
			'asset_des_dir':asset.asset_des_dir,
			'asset_cron':asset.asset_cron
					})
	return render(request, 'asset/asset_mod.html', {'form' : form })

@permission_required('asset.delete_asset',raise_exception=True)
def asset_delete(request,pk):
	asset=Asset.objects.get(pk=pk)
	asset.delete()
	return redirect('/asset_list')
