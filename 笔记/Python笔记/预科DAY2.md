**预科DAY2：**

一.版本控制工具

​	1.gitee

​		gitee中仓库的创建：

​	<img src=".\预科DAY2.assets\1.png">

<img src=".\预科DAY2.assets\2.png">

​	2.git使用

​		a.git下载完成后没有快捷方式，类似于cmd命令，可以直接使用

​		b.将文件上传至仓库的方法：

​			①.在文件夹空白处单击右键，选择Git Bash Here

​			②.若首次上传需要依次输入命令**git init**；

​				**git config --global user.name** "名称"；
​				**git config --global user.email** "邮箱"；

​				若非首次上传跳过此步

​			③.输入命令**git add .**(注意add与.之间一定要用空格)，用于匹配此文件				夹下的所有的增删改查操作

​			④.输入命令**git commit -m** "注释内容"，用于提交本次的增删改查操				作，-m后的内容作为注释

​			⑤.若之前没有绑定仓库需要先输入命令 **git remote add origin 库的				链接** 绑定仓库		

​				库的链接在此处获得：

<img src=".\预科DAY2.assets\3.png">)				

​			可以使用命令**git remote -v**检查是否绑定仓库

​		⑥.若用户名或密码错误可以通过凭据管理器修改密码

​		⑦.输入命令git push origin master 推送代码到文件到远程仓库

​	3.冲突报错

​		原则上永远不删除远程仓库上的内容，若推送失败则需要解决冲突。方法		如下：

​			①.使用命令git pull origin master将代码拉出，实现本地与远程仓库的				同步，然后再push

​			②.若还是不行，则输入命令 git pull origin master --allow-unrelated-				histories，然后再push

​			③.从不同分支push同名文件的话会冲突，解决冲突后合并两个文件

​			注：origin：给.git起的别名，无影响，但一般使用origin,master是分支				名字，固定使用

