from django.urls import path
from . import views   # 从当前文件夹引入文件


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index')
]

# 先引入视图函数
# path()函数定义的路由最终都会在项目启动时加载
# path(路由规则， )
