from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path('hello', views.hello),
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
    re_path('privet', views.privet),
    path('create_post', views.create_post),
    path('get_posts', views.get_posts),
    path('create_comment', views.create_comment),
]