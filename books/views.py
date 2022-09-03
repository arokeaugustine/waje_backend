from rest_framework import viewsets
from rest_framework import permissions
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('first_name')
    serializer_class = AuthorSerializer
    # permission_classes = [permissions.AllowAny]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer

