from django.shortcuts import render
from .models import AuthorProfile
from .serializers import AuthorProfileSerializer
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



# class based view upcoming 2 classes
class AuthorProfileView(APIView):
    def get(self, request):
        authors = AuthorProfile.objects.all()
        serializer = AuthorProfileSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorProfileSerializer(data = request.data)
        if serializer.is_valid():
            validated_data = request.data

            #check unique to do

            #Create Common User
            user = User(username = validated_data['username'],
                        email = validated_data['email'],
                        )
            testdata = request.data
            user.set_password(validated_data['password'])
            user.save()

            #Create Author Profile
            # serializer.save(validated_data = validated_data, user = user)
            instance_data = serializer.data
            # if instance_data['image']== None:
            #     instance_data['image']='default.jpg'

            if instance_data.get('image'):
                instance = AuthorProfile(user=user,
                                    image = instance_data['image'],  
                                    nickname = instance_data['nickname']
                                        )
                instance.save()
            else:
                instance = AuthorProfile(user=user,
                                    nickname = instance_data['nickname']
                                        )
                instance.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)  #created
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    #error

class AuthorProfileViewDetails(APIView):

    def get_object(self, username):
        try:
            author = get_object_or_404(User, username = username)
            return author.authorprofile
        except AuthorProfile.DoesNotExist:
            raise Http404     #error not found said article


    def get(self, request, username):
        authorprofile = self.get_object(username)
        serializer = AuthorProfileSerializer(authorprofile)
        return Response(serializer.data)


    def put(self, request, username):
        authorprofile = self.get_object(username)

        serializer = AuthorProfileSerializer(authorprofile, data = request.data)
        if serializer.is_valid():
            if(request.data.get('username')):
                authorprofile.user.username= request.data.get('username')
            if(request.data.get('email')):
                authorprofile.user.email= request.data.get('email')
            if(request.data.get('password')):
                authorprofile.user.password= request.data.get('password')

            if(request.data.get('nickname')):
                authorprofile.nickname= request.data.get('nickname')
                Authorprofilenickname = request.data.get('nickname') #for debugging
            if(request.data.get('image')):
                authorprofile.image= request.data.get('image')
            authorprofile.user.save()
            authorprofile.save()

            # serializer.update(instance=userprofile, validated_data= validated_data)
            return Response(serializer.data)       # not returning status?  update

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  #error


    def delete(self, request, username):
        authorprofile = self.get_object(username)
        authorprofile.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)