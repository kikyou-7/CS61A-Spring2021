# CS61A-Spring2021

本地文件通过git上传到github仓库的步骤:

先创建本地文件夹,初始化本地仓库
1. $ git init (只需要在第一次的时候使用)  

将本地文件添加到暂存区并上传到版本库
2. $ git add .
3. $ git commit -m '引号内是本次修改的备注'	//提交代码到版本库

再关联到远程仓库  
4. git remote add origin + 仓库地址	//仓库地址建议使用ssh

上传本地仓库的代码到远程仓库:
$ git add .
$ git commit -m "本地提交的备注"
$ git push origin -u master	//第一次上传
$ git push origin master	//不是第一次上传，更新数据

项目组成员克隆项目:
$ git clone + 地址  //建议使用ssh的地址


利用ok脚本在终端中的测评命令行语句:  
python -m doctest xx.py #本地测试,如果有fail case会返回相关信息  
python ok --local #利用ok脚本进行测评  
python ok -q xx --local # 单独测试某题/某个函数  
python ok -q xx -u --local # 与某题交互,帮助理解题意
