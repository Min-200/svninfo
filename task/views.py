#!coding=utf8
from django.shortcuts import render, redirect
from asset.models import Asset
from .models import Task
import forms
# Create your views here.
import paramiko
import models
from django.contrib.auth.decorators import permission_required
def host_list(request):
	pass
	return render(request,'task/host_list.html')



def task_list(request):
	tasklist = Task.objects.all()

	return render(request,'task/task_list.html',{'tasklist':tasklist})


def task_execute(request):
  	if request.method == "POST":
                form = forms.Taskstart(request.POST)
                message = "请检查填写的内容！"
		if form.is_valid():
			task_target  = form.cleaned_data['task_target']
			task_agrs    = form.cleaned_data['task_args']
			try:	
				print task_target
				ssh = paramiko.SSHClient()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				ssh.connect(hostname=task_target, port=22, username='root', password='123456')
				stdin, stdout, stderr = ssh.exec_command(task_agrs)
				succ_result = stdout.read()
				print succ_result
				error_result = stderr.read()
				return render(request, "task/task_execute.html",{'form': form,'succ_result':succ_result,'error_result':error_result})				     
			#	return redirect('ansible_add.html')
                        except:
                                message = "填写错误！"
                                return redirect('task/task_execute.html')
        form = forms.Taskstart()
        return render(request, 'task/task_execute.html', {'form' : form })

@permission_required('task.add_task',raise_exception=True)
def task_add(request):
	if request.method == "POST":
		form = forms.Taskadd(request.POST)
		if form.is_valid():
			task_name     = form.cleaned_data['task_name']
			task_describe = form.cleaned_data['task_describe']
			task_command  = form.cleaned_data['task_command']
			task_host     = form.cleaned_data['task_host']
			split_command = task_command.split('|')
			final_command = split_command[0]
			task_desc      = split_command[1]
						
			task = models.Task.objects.create()
			task.task_name = task_name
			task.task_describe = task_desc
			task.task_command = final_command
			task.task_host = task_host
			task.save()
			
			try:	
				ssh = paramiko.SSHClient()
                                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                                ssh.connect(hostname=task_host, port=22, username='root', password='zjxl2018#')
				command = 'echo "%s" >> /etc/crontab' %(task_command)
				print task_command
                                stdin, stdout, stderr = ssh.exec_command(command)
	                        print command
				ssh.close()

#				f = open('/etc/crontab','a')
#				f.write(str(task_command)+"\n")
#				f.close()
				return redirect('task_add.html')
			except:
                                message = "填写错误！"
				return render(request,'task/task_add.html',{'form':form ,'message':message})
#				return redirect('task_add.html')
	form = forms.Taskadd()
	return render(request,'task/task_add.html',{'form':form})

@permission_required('task.delete_task',raise_exception=True)
def task_delete(request,pk):
	try:
		task = Task.objects.get(pk=pk)
		task_host    = task.task_host
		task_describe = task.task_describe
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=task_host, port=22, username='root', password='123456')
		command = 'sed -i "/%s/d"  /etc/crontab' %(task_describe)
		print task_describe
		stdin, stdout, stderr = ssh.exec_command(command)
		print command
		ssh.close()
		task.delete()
	except:		
		pass
	return redirect('/task_list.html')
	
