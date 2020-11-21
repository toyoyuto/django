from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'accounts'

urlpatterns = [
    # csrf_exemptは無効にしている
    path('', csrf_exempt(views.index), name='index'),
    path('hello/', views.hello, name='hello'),
    path('user/', views.user, name='user'),
    path('list/', views.list, name='list'),

    path('', views.Top.as_view(), name='top'),
    # path('login/', views.Login.as_view(), name='login'),
    path('login/', views.login, name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    # re_path(r'^get/$', views.index),
    # re_path(r'^get/(?P<id>\d+)/$', views.get),
]