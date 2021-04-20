# Question_bank
（因为买的服务器到期已经用不了了，想看demo的话可以自己clone下来根据下面的步骤进行搭建）

demo:  http://121.199.64.120:8080/

api: http://121.199.64.120/

## 搭建步骤
首先自己创建一个python虚拟环境，然后安装requirement.txt下的包
`pip install -r requirement.txt`

然后对数据库进行一次初始化

`python manage.py makemigrations`

`python manage.py migrate --run-syncdb`

然后创建一个用户，否则没有权限新建问题

`python manage.py shell` 打开python命令行，输入以下命令来创建一个admin用户

```python
from django.contrib.auth.models import User
User.objects.create_superuser(username='admin', password='123', email='no@no,com')
```

然后开启后台服务

`python manage.py runserver` 

默认开启在8000端口，当然也可以自己指定端口

访问localhost:8000即可浏览后台管理的api文档（可直接操作）
使用刚刚新建的用户登录就可以新建问题了
