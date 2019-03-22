#coding: utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Subversion
import forms
import models
import django.utils.timezone as timezone
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.decorators import permission_required
import paramiko
from django.contrib import messages
import os
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

people=[]

def SSH(svnname,filename):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #ssh.connect(hostname=host, port=22, username=username, password=password)
    ssh.connect(hostname='192.168.104.185', port=22, username="root", password="123456")
    print "start command"
    #command = 'cd /data/svn/ && sh /data/svn/svn_create.sh %s /var/tmp/svnupload/%s' %(svnname,filename)
    #command = 'cd /data/svna/ && sh /data/svn/svn_create.sh %s /var/tmp/svnupload/%s' %(svnname,filename)
    command = 'cd /SvnRepos/svn/ && sh /SvnRepos/svn/svn_create.sh %s /var/tmp/svnupload/%s' %(svnname,filename)
    print command
    stdin, stdout, stderr = ssh.exec_command(str(command))
    print "over"
    ssh.close()



#@login_required()
def svnlist(request):
	svn_list = Subversion.objects.all().order_by('-id') 
	return render(request, 'svn/svn_list.html',context ={ 'svn_list': svn_list})

@login_required()
def svn_add(request):
    if request.method == "POST":
            print "bbb"
            form = forms.SvnInfo(request.POST,request.FILES)
            #message = "请检查填写的内容！"
            if form.is_valid():

                svn_enname = form.cleaned_data['svn_enname']
                svn_company = form.cleaned_data['svn_company']
                svn_zhname = form.cleaned_data['svn_zhname']
                svn_url = form.cleaned_data['svn_url']
		jira_url = form.cleaned_data['jira_url']
                note = form.cleaned_data['note']
		codeType = form.cleaned_data['CodeType']
                print "start"
                print svn_enname,svn_company,svn_url,svn_zhname,note,codeType
		try:
                    aaa=Subversion.objects.get(svn_enname=svn_enname)
                    if aaa:
                        print "svn仓库名已被使用"
                        return HttpResponse("svn仓库名已经使用")
                except:

              	#	try:
				if codeType == "SVN":
                			File = request.FILES.get("myfile", None)
                			print File.name
					filename=str(File.name)
					print filename
					print type(filename)
                			if File:
                				with open("./svnupload/%s" % File.name, 'wb+') as f:
                            				# 分块写入文件
                            				for chunk in File.chunks():
                                				f.write(chunk)
                		else:
                        		print "是svn"
				
				if codeType == "SVN":
                            		print "执行脚本"
					cmd = "scp ./svnupload/%s 192.168.104.185:/var/tmp/svnupload" %(File.name)
					os.system(cmd)
					SSH(svnname=svn_enname,filename=File.name)
					time.sleep(7)				
					cmd1 = "scp 192.168.104.185:/home/newpeople.txt /opt/svninfo/newpeople.txt"
					os.system(cmd1)
                		print "添加记录"
				
				

				print svn_enname,svn_company,svn_url,svn_zhname,jira_url,note,codeType
                   		new = models.Subversion.objects.create()
                   		new.svn_enname = svn_enname
				new.code_type = codeType
                   		new.svn_company = svn_company
                   		new.svn_zhname = svn_zhname
                   		new.svn_url = svn_url
				new.jira_url = jira_url
                        	new.note = note
                   		new.save()
				
					
				
								
				f = open('/opt/svninfo/newpeople.txt', 'r')           #如改变文件位置需要修改
				people = f.read()
				people="".join(people)
				people=people.strip()
				people=people.split(",")
				people=",".join(people)

				f.close()
				if people != "" and codeType == "SVN":
					messages.success(request,people)
				else:
					messages.success(request,"所有人已经存在")
					print "-----"
					print people
                		return redirect('svnlist.html')
    			#	return render(request, 'svn/svn_list.html', context={'people': people})
					
                #	except:
                #    		message = ""
                #    		return redirect('svn_add.html')
            	#	else:
                #		print "aaaa"
                		print form.errors

    form = forms.SvnInfo()
    return render(request, 'svn/svn_add.html', {'form': form})



@login_required()
def svn_mod(request, pk):
    svn = Subversion.objects.get(pk=pk)
    
    print svn.svn_enname,svn.svn_company,svn.svn_url,svn.svn_zhname,svn.jira_url,svn.note,svn.code_type
    if request.method == "POST":
        form = forms.SvnInfo(request.POST, initial=[
            {'svn_enname': svn.svn_enname, 'svn_company': svn.svn_company, 'svn_zhname': svn.svn_zhname,
             'svn_url': svn.svn_url, 'jira_url': svn.jira_url, 'note': svn.note,'CodeType':svn.code_type}])
        if form.is_valid():
            svn.svn_enname = form.cleaned_data['svn_enname']
            svn.svn_company = form.cleaned_data['svn_company']
            svn.svn_zhname = form.cleaned_data['svn_zhname']
            svn.svn_url = form.cleaned_data['svn_url']
            svn.jira_url = form.cleaned_data['jira_url']
            svn.code_type = form.cleaned_data['CodeType']
            svn.note = form.cleaned_data['note']
            svn.save()
            return redirect('/svnlist.html')      

    form = forms.SvnInfo(initial={
        'svn_enname': svn.svn_enname,
        'svn_company': svn.svn_company,
        'svn_zhname': svn.svn_zhname,
        'svn_url': svn.svn_url,
        'jira_url': svn.jira_url,
        'CodeType': svn.code_type,
        'note':svn.note
    })
    return render(request, 'svn/svn_mod.html', {'form': form})




@login_required()
def svn_delete(request,pk):
    svn=Subversion.objects.get(pk=pk)
    svn.delete()
    return redirect('/svnlist')
