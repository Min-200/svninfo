"""shield URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
#from asset.views  import index , assets_config, assets_add, assets_list, assets_log
from asset.views import index, asset_list , asset_add, flot, morris,asset_l, asset_mod,asset_delete
#from task.views import task_execute,task_add,task_list,task_delete,host_list
from userinfo.views import *
from subversion.views import *
app_name = 'shield'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^index', index),
    url(r'^tables', asset_list),
    url(r'^asset_list', asset_l),
    url(r'^asset_add', asset_add),
    url(r'^asset_mod/(?P<pk>[0-9]+)/$', asset_mod ,name = 'assetmod'),
    url(r'^asset_delete/(?P<pk>[0-9]+)/$', asset_delete ,name = 'assetdelete'),
#    url(r'^host_list', host_list),
#    url(r'^task_execute',task_execute),
#    url(r'^task_add',task_add),
#    url(r'^task_list',task_list),
#    url(r'^task_delete/(?P<pk>[0-9]+)/$', task_delete),
    url(r'^login',login),
    url(r'^accounts/login',login),
    url(r'^accounts/logout',logout),
    url(r'^svnlist',svnlist),
    url(r'^svn_add',svn_add),
    url(r'^svn_delete/(?P<pk>[0-9]+)/$', svn_delete),
    url(r'^svn_mod/(?P<pk>[0-9]+)/$', svn_mod)
]
