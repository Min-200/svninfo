#coding=utf-8
from django import forms
class Taskstart(forms.Form):
    task_target   = forms.CharField(label="目标", max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    task_args     = forms.CharField(label="参数", max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))



class Taskadd(forms.Form):
    task_name     = forms.CharField(label="任务名称", max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    task_describe = forms.CharField(label="任务描述", max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    task_command  = forms.CharField(label="执行命令", max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    task_host     = forms.CharField(label="目标主机", max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))

