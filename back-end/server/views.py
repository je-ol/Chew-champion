from rest_framework.response import Response
from .serializers import UserSerializer, PostsSerializer, CommentsSerializer, LikeSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Posts, Comments, Like
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
import cloudinary
from cloudinary.uploader import upload
import os
from django.db import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class LoginView(APIView):
    def post(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({'detail':'incorrect password.'}, status=status.HTTP_400_BAD_REQUEST)
        token,  created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        return Response({"token": token.key, "user": serializer.data})

class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestTokenView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request)
        return Response("passed for {}".format(request.user.email))

class HelloView(APIView):
    def get(self, request):
        return Response({"message" : "Hello, world!"})

class PrivetView(APIView):
    def get(self, request):
        return Response({"сообщение" : "Привет, мир!"})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def current_user(self, request):
        user = self.request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    users = User.objects.all()
    serializer_class = PostsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def my_posts(self, request):
        user = self.request.user
        my_posts = Posts.objects.filter(user_id=user)
        serializer = self.get_serializer(my_posts,many=True)
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(id=request.user.id)
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user_id != request.user.id:
            return Response({"detail": "You do not have permission to update this post."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=['POST'])
    def upload_image(self, request):
        image = request.FILES.get('image')
        title = request.data.get('title', '')
        content = request.data.get('content', '')
        if not image:
            return Response({"detail": "No image provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        cloudinary.config( 
            cloud_name = os.getenv("cloud_name"), 
            api_key = os.getenv("api_key"), 
            api_secret = os.getenv("api_secret"),
            secure=True
        )

        upload_result = upload(image)
        image_url = upload_result["secure_url"]

        post = Posts.objects.create(image_url=image_url, user=request.user, title=title, content=content)
        post.save()

        serializer = self.get_serializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        user = self.request.user
        post = self.get_object()

        serializer = LikeSerializer(data={'user': user.id, 'post': post.post})
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError:
                return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"detail": "Post liked successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        post = Posts.objects.get(post=self.request.data['post_id'])
        serializer.save(user=user, post=post)
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user_id != request.user.id:
            return Response({"detail": "You do not have permission to update this comment."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    filterset_fields = ['user_id']