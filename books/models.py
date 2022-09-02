from pyexpat import model
from django.db import models


class Author(models.Model):
    first_name = models.TextField(max_length=250)
    last_name = models.TextField(max_length=250)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    name = models.TextField(max_length=250)
    isbn = models.TextField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,)


    def __str__(self):
        return self.name