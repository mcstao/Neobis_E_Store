from django.urls import path, include, re_path
from .views import UserInfoDetailView, UserInfoListCreateView

urlpatterns = [
    path('drf-auth/', include('rest_framework.urls')),
    path(r'auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('info/<int:pk>/', UserInfoDetailView.as_view()),
    path('info/', UserInfoListCreateView.as_view())
]