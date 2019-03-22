# 配置管理工具+持续集成

## 目前功能：
	1.SVN库初始化,添加新库，初始化目录结构,添加新的人员权限
	2.记录功能,目前字段 公司---项目组---创建时间---库类别--中文名--仓库名--配置库地址---JIRA地址---备注   增删改查
	3.服务器的备份信息--- 功能和上差不多 增删改查
	4.DEVOPS CI部分，具体介绍如下
## ci部分
1.使用python-jenkins模块,获取所有的jenkins构建job,并将其写入Joblist这个库
2.在页面展示Joblist库的信息，点击一条记录，触发远程的jenkins构建，同时将该构建的 任务名称、构建号、构建状态、构建时间、构建日志地址 写入数据库Triggerbuild记录
3.使用django-crontab 在ci的core.py中 实现在后台每分钟查询 Triggerbuild 这个库中构建状态是loading的记录，获取该记录的 任务名称和构建号， 调用python-jenkins模块 去查询该任务的构建结果，如果成功则获取包url写到Packageurl这个库中，每个包一个记录，通过外键id对应
		

## 相关日志
	SVN服务器上的日志 /home/svn.log
	新添加的人： SVN: /home/newpeople.txt
	WEB服务器： /opt/svninfo/newpeople.txt
	djangolog   /opt/svninfo/newpeople.txt


## 安装
	apt-get install libmysqlclient-dev
	pip install paramiko
	python manage.py makemigrations
	pip install MySQL-python

