from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)  
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
