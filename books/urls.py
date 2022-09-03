from rest_framework import routers
from .views import AuthorViewSet, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'authors', AuthorViewSet, basename='authors')


urlpatterns = []+router.urls