from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),     # 기본 root-url, views = 일종의 controller
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),     # 게시물 등록 처리
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]