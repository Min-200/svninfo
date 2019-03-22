#coding: utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  Joblist, Triggerbuild
import jenkins
import sys
import time
import os
import models
import django.utils.timezone as timezone


ip = "192.168.1.1"
file="/jenkinsdata/data/.jenkins/common-extended"



def Buildrefresh(request):
	print "refresh"
	server = jenkins.Jenkins('http://192.168.1.1:8080/jenkins/', username='admin', password='123456')
	for l in server.get_jobs():
		job_project = l['name']
       		for i in l['jobs']:     
			job_name = i['name']            
               		job_url =  i['url']
			aaa=Joblist.objects.filter(job_name=job_name)                           #将joblist添加到数据库里面
			if not aaa:
				new = models.Joblist.objects.create()				#存在问题,jenkins删除一个构建后,怎么在这里删除对应的数据库
				new.job_project = job_project
				new.job_name = job_name
				new.job_url  = job_url
				new.save()
				print new.job_name, new.job_url, new.job_project
			
	
	return redirect('/build_list')


def Buildlist(request):
	build_list=Joblist.objects.all()
	
	if request.method == "POST":
		print "aaaaa"
		print request.body
		name = request.POST.getlist('list')
		print name
		concat = request.POST
        	postBody = request.body
        	print(concat)
        	print(type(postBody))
        	print(postBody) 

	
	return render(request,'ci/build_list.html',context={'build_list': build_list})	



def Tbuild(request):
		
	Tbuild_list=Triggerbuild.objects.all()
	
	return render(request,'ci/Tbuild.html',context={'Tbuild_list': Tbuild_list})	

def build_job(request,pk):
	job = Joblist.objects.get(pk=pk)

	server = jenkins.Jenkins('http://192.168.104.187:8080/jenkins/', username='admin', password='123456')
	full_name = job.job_project+"/"+job.job_name
	print full_name
	next_build_number = server.get_job_info(full_name)['nextBuildNumber']
	server.build_job(full_name)
	B_name = Joblist.objects.get(job_name=job.job_name)
        B_name.id=B_name.id
	job_log = "http://192.168.104.187:8080/jenkins/job/%s/job/%s/%s/console" %(job.job_project,job.job_name,next_build_number)	

        print B_name.id
        new = Triggerbuild.objects.create(job_name_id=B_name.id,job_build_time=timezone.now(),job_status="loading",job_num= next_build_number,job_log=job_log)
	

	return redirect('/Tbuild_list')


def Build(request):
	if request.method == "POST":
		print "aaaaa"
		name = request.POST.getlist(list)
		print name 
	Tbuild_list=Triggerbuild.objects.all()

	return render(request,'ci/Tbuild.html',context={'Tbuild_list': Tbuild_list})	
