from rest_framework.response import Response
from .serializers import UserSerializer, PostsSerializer, CommentsSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Posts, Comments
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import viewsets

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

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # @action(detail=False, methods=['GET'])
    def get_queryset(self):
        user = self.request.user
        return Posts.objects.filter(user_id=user)
    
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
    


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        post = Posts.objects.get(post=self.request.data['post_id'])
        serializer.save(user=user, post=post)