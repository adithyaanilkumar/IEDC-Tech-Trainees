from django.shortcuts import render
from .models import UserProfile
from .serializers import UserProfileSerializer
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
class UserProfileView(APIView):
    def get(self, request):
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserProfileSerializer(data = request.data)
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

            #Create User Profile
            # serializer.save(validated_data = validated_data, user = user)
            instance_data = serializer.data
            # if instance_data['image']== None:
            #     instance_data['image']='default.jpg'

            if instance_data.get('image'):
                instance = UserProfile(user=user,
                                    image = instance_data['image'],  
                                    about = instance_data['about']
                                        )
                instance.save()
            else:
                instance = UserProfile(user=user,
                                    about = instance_data['about']
                                        )
                instance.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)  #created
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    #error

class UserProfileViewDetails(APIView):

    def get_object(self, username):
        try:
            user = get_object_or_404(User, username = username)
            return user.userprofile
        except UserProfile.DoesNotExist:
            raise Http404     #error not found said article


    def get(self, request, username):
        userprofile = self.get_object(username)
        serializer = UserProfileSerializer(userprofile)
        return Response(serializer.data)


    def put(self, request, username):
        userprofile = self.get_object(username)     # will result in 404 if username doesnot exist

        serializer = UserProfileSerializer(userprofile, data = request.data)
        if serializer.is_valid():
            if(request.data.get('username')):
                userprofile.user.username= request.data.get('username')
            if(request.data.get('email')):
                userprofile.user.email= request.data.get('email')
            if(request.data.get('password')):
                userprofile.user.password= request.data.get('password')

            if(request.data.get('about')):
                userprofile.about= request.data.get('about')
                userprofileabout = request.data.get('about')
            if(request.data.get('image')):
                userprofile.image= request.data.get('image')
            userprofile.user.save()
            userprofile.save()

            # serializer.update(instance=userprofile, validated_data= validated_data)
            return Response(serializer.data)       # not returning status?  update
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  #error


    def delete(self, request, username):
        userprofile = self.get_object(username)
        userprofile.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 






#modelviewset
class ModelViewset(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()



# generic viewset
class GenericApiView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    lookup_field = 'username'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, username = None):
        if id:
            return self.retrieve(request)

        else:
            return self.list(request)
        

    def post(self, request, username):
        return self.create(request)

    def put(self, request, username):
        return self.update(request,id)

    def delete(self, request):
        return self.destroy(request, id)








