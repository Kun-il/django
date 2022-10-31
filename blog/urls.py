from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list')     # 기본 root-url, views = 일종의 controller
]