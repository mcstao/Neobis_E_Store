from django.urls import path, include
from rest_framework.routers import DefaultRouter

from store_app.views import ReviewViewSet, ProductViewSet, CommentViewSet, CategoryView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryView.as_view())
]