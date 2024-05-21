from django.urls import re_path, path, include
from . import views
from server.views import LoginView, SignupView, TestTokenView, HelloView, PrivetView, PostsViewSet, CommentsViewSet, UserViewSet, LikeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostsViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'users', UserViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('test_token/', TestTokenView.as_view(), name='test_token'),
    path('', include(router.urls)),
    path('privet/', PrivetView.as_view(), name='privet'),
]