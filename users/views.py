from django.contrib.auth.models import User

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .permission import IsOwnerProfileOrReadOnly
from store_app.models import UserInfo
from users.serializers import UserSerializer, UserInfoSerializer


# Create your views here.

class UserInfoListCreateView(ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserInfoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerProfileOrReadOnly]
