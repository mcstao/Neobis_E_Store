from django.urls import path, include
from rest_framework.routers import DefaultRouter

from store_app.views import ReviewViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]