from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer, PostsSerializer, CommentsSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Posts, Comments

from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'detail':'Not found.'}, status=status.HTTP_400_BAD_REQUEST)
    token,  created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user.email))


@api_view(['GET'])
def hello(request):
    return Response({"message" : "Hello, world!"})

@api_view(['GET'])
def privet(request):
    return Response({"сообщение" : "Привет, мир!"})

@api_view(['GET'])
def get_posts(request):
    posts = Posts.objects.all()
    serializer = PostsSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_post(request):
    serializer = PostsSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.get(id=request.user.id)
        serializer.save(user_id=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_comment(request):
    serializer = CommentsSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.get(id=request.user.id)
        post = Posts.objects.get(post_id=request.data['post_id'])
        serializer.save(user_id=user, post_id=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)