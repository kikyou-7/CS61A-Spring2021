# CS61A-Spring2021

本地文件通过git上传到github仓库的步骤:
1. $ git init (只需要在第一次的时候使用)
2. $ git add .
3. $ git commit -m"***"
4. (如果github仓库有修改,需要先 git pull origin master 更新本地仓库)
5. $ git push origin master


作业在终端中的命令行语句:
python -m doctest hwxx.py #本地测试,如果有fail case会返回相关信息
python ok --local #利用ok脚本进行测评
