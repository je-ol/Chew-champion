from django.urls import re_path
from . import views

urlpatterns = [
    re_path('hello', views.hello),
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
    re_path('privet', views.privet),
    re_path('create_post', views.create_post)
]