#coding=utf-8
from django import forms
class Assetadd(forms.Form):
    asset_name   = forms.CharField(label="名称", max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}))
    asset_sou_ip = forms.CharField(label="源IP", max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    asset_sou_dir = forms.CharField(label="源目录", max_length=200,widget=forms.Textarea(attrs={'class':'form-control'}))
    asset_des_ip = forms.CharField(label="目标IP", max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    asset_des_dir =  forms.CharField(label="目标目录", max_length=200,widget=forms.Textarea(attrs={'class':'form-control'}))
    asset_cron =  forms.CharField(label="计划任务", max_length=500,widget=forms.Textarea(attrs={'class':'form-control'}))
