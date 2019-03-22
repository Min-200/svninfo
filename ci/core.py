from .models import  Joblist, Triggerbuild, Packageurl
import jenkins
import sys
import time
import os
import models



def updatestatus():
	print "start!!!!!!!!!!!"
	url_file = "/jenkinsdata/data/.jenkins/common-extended"
	server = jenkins.Jenkins('http://192.168.104.187:8080/jenkins/', username='admin', password='123456')
	jilu = Triggerbuild.objects.filter(job_status='loading')
        for i in  jilu.values():
                num= i["job_num"]
                job_id=i["job_name_id"]
		build_id=i["id"]
		print build_id
                print num
                print job_id
                A = Joblist.objects.get(id=i["job_name_id"])
                all_name = A.job_project+"/"+ A.job_name
		print A.job_name
		print all_name
                build_ing=server.get_build_info(all_name,int(num))['building']
		print build_ing
                if build_ing != True:
			print "Fa"
                        build_result=server.get_build_info(all_name,int(num))['result']
			models.Triggerbuild.objects.filter(job_name_id=A.id,job_num=i['job_num']).update(job_status=build_result)
			print build_result
			if build_result == "SUCCESS":
				url=os.popen("ssh 192.168.104.187 cat {}/{}.txt".format(url_file,A.job_name)).readlines()
				for i in url:
        				q=i.replace('\n','')
					package_url=q.split("&")[0]
					md5 = q.split("&")[1]
					d = package_url.split("/")
					package_name = d[len(d)-1]
					print q
					print package_name,package_url,md5, build_id
					Packageurl.objects.create(job_name_id=build_id, package_name=package_name, package_url=package_url, package_md5=md5)
					print "aaaaa"
				
