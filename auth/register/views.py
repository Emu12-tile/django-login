from .models import Register 
from .serializers import UserSerializer
from rest_framework import mixins,viewsets
from rest_framework import generics

class UserListSet(mixins.ListModelMixin, 
                   mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin, 
                    viewsets.GenericViewSet):  # Inherit from GenericViewSet
    queryset = Register.objects.all()
    serializer_class = UserSerializer