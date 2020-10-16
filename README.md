# 配置管理工具+持续集成

## 目前功能：
	1.SVN库初始化,添加新库，初始化目录结构,添加新的人员权限
	2.记录功能,目前字段 公司---项目组---创建时间---库类别--中文名--仓库名--配置库地址---JIRA地址---备注   增删改查
	3.服务器的备份信息--- 功能和上差不多 增删改查
	4.DEVOPS CI部分，具体介绍如下
## ci部分
	1.使用python-jenkins模块,获取所有的jenkins构建job,并将其写入Joblist这个库
	2.在页面展示Joblist库的信息，点击一条记录，触发远程的jenkins构建，同时将该构建的 任务名称、构建号、构建状态、构建时间、构建日志地址 写入数据库	Triggerbuild记录
	3.使用django-crontab 在ci的core.py中 实现在后台每分钟查询 Triggerbuild 这个库中构建状态是loading的记录，获取该记录的 任务名称和构建号， 调		用python-jenkins模块 去查询该任务的构建结果，如果成功则获取包url写到Packageurl这个库中，每个包一个记录，通过外键id对应
		

## 相关日志
	SVN服务器上的日志 /home/svn.log
	新添加的人： SVN: /home/newpeople.txt
	WEB服务器： /opt/svninfo/newpeople.txt
	djangolog   /opt/svninfo/newpeople.txt


## 安装
	apt-get install libmysqlclient-dev
        yum -y install mysql-devel 
	pip install paramiko
	python manage.py makemigrations
	pip install MySQL-python
	yum install python-devel
	pip install django-crontab
	
## django-crontab使用
	pip install django-crontab
	 在settings中添加 
	INSTALLED_APPS = (
       ...
       'django_crontab',
   	)
   	在app内新建py文件，文件名称随意。
	例如我们在名为ci的app下新建了一个core.py文件。
		def task():
   			#要执行的任务函数
	CRONJOBS = [
    	('*/1 * * * *', 'ci.core.updatestatus','>> /var/core.log')
	]

	python manage.py crontab add
	python manage.py crontab show
	python manage.py crontab remove


展示图片

![](https://github.com/shiminde/svninfo/blob/master/images/QQ%E5%9B%BE%E7%89%8720190329133120.png)
![](https://github.com/shiminde/svninfo/blob/master/images/QQ%E5%9B%BE%E7%89%8720190329133137.png)
![](https://github.com/shiminde/svninfo/blob/master/images/QQ%E5%9B%BE%E7%89%8720190329133256.png)
![](https://github.com/shiminde/svninfo/blob/master/images/QQ%E5%9B%BE%E7%89%8720190329133331.png)
![](https://github.com/shiminde/svninfo/blob/master/images/9CD983FB-4060-46ef-AC95-04A837B4DC98.png)
