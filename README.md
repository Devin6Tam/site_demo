## 简单的使用方法：

```
创建虚拟环境
使用pip安装第三方依赖
修改settings.example.py文件为settings.py
运行migrate命令，创建数据库和数据表
运行python manage.py runserver启动服务器
```

路由设置：

```python
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
    url('admin/', admin.site.urls),
    url(r'^user/', include(('user.urls', 'apps'), namespace='user')),
    url(r'^polls/', include(('polls.urls', 'apps'), namespace='polls')),
    url(r'^captcha/', include('captcha.urls')),   # 增加这一行
    # 添加多媒体访问路径
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
```