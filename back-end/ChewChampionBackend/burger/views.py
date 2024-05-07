from rest_framework.viewsets import ModelViewSet
from burger.models import User

# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BurgerSerializer