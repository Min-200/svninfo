使用方法：

1.需要将svn_str目录,check.py,svn_create.sh 项目成员表 4个文件放入svn仓库目录，例如 /data/svn



2.sh svn_create.sh 库名 项目组成员表

例如： sh svn_create.sh YYX AAA.xlsx



svn_create.sh

最开头3行 需设置svn家目录地址,ip地址，如有变化可修改

hook="/data/svn/test/hooks/pre-commit"
svndir="/data/svn"

ip="192.168.1.1"
