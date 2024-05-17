from django.urls import re_path, path, include
from . import views
from server.views import LoginView, SignupView, TestTokenView, HelloView, PrivetView, PostsViewSet, CommentsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostsViewSet)
router.register(r'comments', CommentsViewSet)

urlpatterns = [
    # re_path('hello', views.hello),
    path('hello/', HelloView.as_view(), name='hello'),
    # re_path('login', views.login),
    # re_path('signup', views.signup),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    # re_path('test_token', views.test_token),
    path('test_token/', TestTokenView.as_view(), name='test_token'),
    # path('create_post', views.create_post),
    # path('get_posts', views.get_posts),
    path('', include(router.urls)),
    # path('create_comment', views.create_comment),
    path('privet/', PrivetView.as_view(), name='privet')
]