from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView    #class based views
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets   #model viewset
from rest_framework import generics, mixins  #generic views


class ModelViewset(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()



#Generic viewset
class BookGeneric(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'name'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, name = None):
        try:
            book = Book.objects.get(name=name)
        except:
            raise Http404

        serializer = BookSerializer(book)
        return Response(serializer.data)

        

    def post(self, request, username):
        return self.create(request)

    def put(self, request, username):
        return self.update(request,id)

    def delete(self, request):
        return self.destroy(request, id)