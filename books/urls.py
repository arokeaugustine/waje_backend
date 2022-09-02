from rest_framework import routers
from .views import AuthorViewSet, BookViewSet
from books import views
from rest_framework.routers import DefaultRouter
from .models import Author, Book

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'authors', AuthorViewSet, basename='authors')


urlpatterns = []+router.urls