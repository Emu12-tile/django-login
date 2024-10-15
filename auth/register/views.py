from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]  # Use appropriate permissions

    def get_queryset(self):
        # Customize the queryset if necessary, e.g., to filter users by a specific condition
        return CustomUser.objects.all()
