# Question_bank

Question_bank 是一个自定义的随机做题题库，目前仅支持选择题。前端采用 vue 单文件，后端基于django，可通过 django 的 api 很方便的在浏览器上添加题目并在前端页面上随机做题。

demo:  http://101.35.202.174/qbank

api: http://101.35.202.174:8000/

## 截图

![](/images/screenshot1.png)
![](/images/screenshot2.png)
![](/images/screenshot3.png)

## 搭建步骤
首先自己创建一个python虚拟环境，然后安装requirement.txt下的包

`pip install -r requirement.txt`

然后对数据库进行一次初始化

`python manage.py makemigrations`

`python manage.py migrate --run-syncdb`

然后创建一个用户，否则没有权限新建问题

`python manage.py shell` 

打开python命令行，输入以下命令来创建一个admin用户

```python
from django.contrib.auth.models import User
User.objects.create_superuser(username='admin', password='123', email='no@no,com')
exit()
```

然后开启后台服务

`python manage.py runserver` 

默认开启在8000端口，当然也可以自己指定端口，此时访问 localhost:8000 即可浏览后台管理的api文档（可直接操作），使用刚刚新建的用户登录就可以新建问题了

前端页面由vue编写，直接打开项目根目录下的html文件即可浏览（当然，数据库里需要有你新建的问题）

## 技术栈
- django
- vue

## TODO
(欢迎小伙伴来一起完善)
- [x] 后台权限
- [ ] 根据不同的类型获取问题
- [ ] 完善问题的评级系统
- [ ] 答案解析支持代码高亮
