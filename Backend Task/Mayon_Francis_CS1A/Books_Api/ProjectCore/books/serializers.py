from rest_framework import serializers
from django.contrib.auth.models import User
from authors.models import AuthorProfile
from .models import Book
from rest_framework.validators import UniqueValidator


class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source = 'author.user.username', read_only=True)
    name = serializers.CharField(validators=[UniqueValidator(queryset=Book.objects.all())] )

    class Meta:
        model = Book     # MIGHT NEED TO CHANGE TO User, not sure
        fields = ['name','description','thumbnail','author']