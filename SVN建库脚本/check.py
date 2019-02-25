#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
import xlrd
import sys
import os
import subprocess
#import urllib2

file=sys.argv[1]

data = xlrd.open_workbook(file)
table = data.sheets()[2]
nrows = table.nrows
#print 'nrows: %s' %(nrows)
pmlist = []
reqlist = []
devleadlist = []
devlist = []
testleadlist = []
testlist = []
alltest = []
X=""


for i in range(nrows):

        # url = table.row_values(i)[1:3]
        role = table.row_values(i)[0]
	
	if role == u"项目经理" or role == u"产品经理" or role == u"研发负责人" or role == u"研发人员" or role == u"测试负责人" or role == u"测试人员":
		name = table.row_values(i)[2]
		if role == u"项目经理":
			X = 0
			pmlist.append(name)
		if role == u"产品经理":
			X = 1
			reqlist.append(name)
		elif role == u"研发负责人":
			X = 2
			devleadlist.append(name)
		elif role == u"研发人员":
			X = 3
			devlist.append(name)
		elif role == u"测试负责人":
			X = 4
			testleadlist.append(name)
			alltest.append(name)
		elif role == u"测试人员":
			X = 5
			testlist.append(name)
			alltest.append(name)
	
	if role == "":
		name = table.row_values(i)[2]
		if X == 0:
			if name != "":
				pmlist.append(name)
		if X == 1:
			if name != "":
				reqlist.append(name)
		elif X == 2:
			if name != "":
				devleadlist.append(name)
		elif X == 3:
			if name != "":
				devlist.append(name)
		elif X == 4:
			if name != "":
				testleadlist.append(name)
				alltest.append(name)
		elif X == 5:
			if name != "":
				testlist.append(name)
				alltest.append(name)


pmlist1= []
reqlist1 = []
devleadlist1 = []
devlist1 = []
testleadlist1 = []
testlist1 = []
alltest1 = []
alllist = []

#格式处理函数,得到邮箱前缀,人名
def spl(list0,list1):
	list0=list(filter(None,list0))
	for req in list0:
		sp =  req.split('@')
		name = sp[0]
		list1.append(name)
		alllist.append(name)
	#list1 = ",".join(list1)
	
	return list1
	
#格式处理输出到一个文件中
#############################################
#req="REQ:%s" %(spl(reqlist,reqlist1))
#devlead="DEVLEAD:%s" %(spl(devleadlist,devleadlist1))
#dev="DEV:%s" %(spl(devlist,devlist1))
#testlead="TESTLEAD:%s" %(spl(testleadlist,testleadlist1))
#test="TEST:%s" %(spl(testlist,testlist1))
#print '-------------------------'
#print req
#print devlead
#print dev
#print testlead
#print test

#f = open('people.txt', 'w')
#f.write(str(req)+"\n")
#f.write(str(devlead)+"\n")
#f.write(str(dev)+"\n")
#f.write(str(testlead)+"\n")
#f.write(str(test)+"\n")
#f.close()
##############################################
pm=",".join(spl(pmlist,pmlist1))
req=",".join(spl(reqlist,reqlist1))
devlead=",".join(spl(devleadlist,devleadlist1))
dev=",".join(spl(devlist,devlist1))
#testlead=",".join(spl(testleadlist,testleadlist1))
#test=",".join(spl(testlist,testlist1))
test=",".join(spl(alltest,alltest1))
alllist=list(set(alllist))

def Panduan(role):
	if role == "":
		role = "noone"
		print role
	else:
		print role


Panduan(req)
Panduan(devlead)
Panduan(dev)
Panduan(test)               #只看测试人员，不分负责人和普通测试
#Panduan(testlead)
#Panduan(test)
Panduan(pm)
#os.environ['req']=str(req)
#os.system('echo $req')
#print req
#print devlead
#print dev
#print testlead
#print test
#print pm

Nouserlist=[]
passwd=[]

f = open("passwd","rw");
all = f.readlines()
for line in all:                    #读取passwd文件,格式化文本，输出namelist
	a=line.split(":")[0]
	passwd.append(a)

for name in alllist:		    #判断excel的中所有人是否在namelist中
	if name not in passwd:
		Nouserlist.append(name)
		
f.close()
Nouserlist=list(set(Nouserlist))
num = len(Nouserlist)
newname = ",".join(Nouserlist)
print	newname

#将Nouserlist中的人员添加到passwd中，密码为123456
if num != 0:
	for nouser in Nouserlist:
		cmd = "htpasswd -b -m passwd %s qazWSX123" %(nouser)
		os.system(cmd)

