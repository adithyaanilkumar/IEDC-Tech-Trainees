from django.db import models
from authors.models import AuthorProfile


class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='Book Description')
    thumbnail = models.ImageField(default = 'default.jpg', upload_to='book_thumbnail')
    author =models.ForeignKey(AuthorProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


