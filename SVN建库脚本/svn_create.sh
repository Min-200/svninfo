#!/bin/bash
exec 1>>/home/svn.log
exec 2>>/home/svn.log

date
svndir="/opt/svn"
hook="$svndir/AAA/hooks/pre-commit"

ip="192.168.1.1"


#备份
cp $svndir/authz $svndir/authz_shellback
cp $svndir/passwd $svndir/passwd_shellback



if [ -d $svndir/$1 ];then
	echo "project is exist $1"
	exit

else
	echo "start create $1"
fi

#创建svn仓库
cd $svndir
svnadmin create  $1
cp $hook $1/hooks/
chmod -R 777 $1
echo "SVN库创建完毕"


#初始化目录结构
svn checkout https://$ip/svn/$1 /tmp/$1
cp -r $svndir/svn_str/* /tmp/$1
cd /tmp/$1
svn add *
svn commit -m "初始化项目"

echo "初始化目录结构完毕"

#更改授权文件

cd $svndir
cmd="python check.py $2"
a=`$cmd`
req=`echo $a | awk '{print $1}'`
devlead=`echo $a | awk '{print $2}'`
dev=`echo $a | awk '{print $3}'`
#testlead=`echo $a | awk '{print $4}'`
#test=`echo $a | awk '{print $5}'`
test=`echo $a | awk '{print $4}'`
pm=`echo $a | awk '{print $5}'`
nonamelist=`echo $a | awk '{print $6}'`

echo "[=========================================================================]"

if [[ $nonamelist != "" ]];then
	echo "新添加的人:$nonamelist,初始密码为qazWSX123"
	date
        echo "$nonamelist" > /home/newpeople.txt

	
else
	echo "$nonamelist" > /home/newpeople.txt
	echo "所有用户都存在"
fi


if [ $req == "noone" ];then
	req=""
fi	

if [ $devlead == "noone" ];then
	devlead=""
fi	
if [ $dev == "noone" ];then
	dev=""
fi	
#if [ $testlead == "noone" ];then
#	testlead=""
#fi	
if [ $test == "noone" ];then
	test=""
fi	
if [ $pm == "noone" ];then
	pm=""
fi	


REQ="$1_REQ=$req"
PM="$1_PM=$pm"
DEV="$1_DEV=$dev"
DEVLEADER="$1_DEVLEADER=$devlead"
#TEST="$1_TEST=$test,$testlead"
TEST="$1_TEST=$test"




sed -i "/\[\/\]/i$REQ"    $svndir/authz
sed -i "/\[\/\]/i$PM"     $svndir/authz
sed -i "/\[\/\]/i$DEV"    $svndir/authz
sed -i "/\[\/\]/i$DEVLEADER" $svndir/authz
sed -i "/\[\/\]/i$TEST" $svndir/authz

echo """
[$1:/]
@SCM=rw
@$1_DEV=r
@$1_PM=r
@$1_DEVLEADER=r
@$1_TEST=r
@$1_REQ=r
@QA=r
*=

[$1:/data]
@DB=r
@$1_DEV=rw
@$1_DEVLEADER=rw
@$1_REQ=

[$1:/dep]
@$1_DEV=rw
@$1_DEVLEADER=rw
@$1_REQ=

[$1:/source]
@$1_DEV=r
@$1_DEVLEADER=r
@$1_REQ=
@$1_TEST=

[$1:/source/dev]
@$1_DEV=rw
@$1_DEVLEADER=rw

[$1:/source/release]
@$1_DEV=r
@$1_DEVLEADER=rw

[$1:/source/trunk]
@$1_DEV=r
@$1_DEVLEADER=rw

[$1:/项目文档]
@$1_PM=r
@$1_DEV=r
@$1_TEST=r
@$1_REQ=r
@QA=rw

[$1:/项目文档/01立项管理]
@$1_PM=rw

[$1:/项目文档/02产品需求]
@$1_REQ=rw
@$1_DEV=rw

[$1:/项目文档/03UI文档]
@$1_REQ=rw

[$1:/项目文档/04研发文档]
@$1_DEV=rw

[$1:/项目文档/05测试文档]
@$1_TEST=rw

[$1:/项目文档/06质量跟踪]
@QA=rw


[$1:/项目文档/07手册]
@$1_TEST=rw
@$1_DEV=rw
@$1_PM=rw
@$1_REQ=rw

[$1:/项目文档/08其他]
@$1_TEST=rw
@$1_DEV=rw
@$1_PM=rw
@$1_REQ=rw
""" >> $svndir/authz
echo "更改权限文件完毕"
