from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework.validators import UniqueValidator


class UserProfileSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required=False)
    about = serializers.CharField(default='About Me')
    username = serializers.CharField(source = 'user.username' )  #validators=[UniqueValidator(queryset=User.objects.all())]
    email    = serializers.EmailField(source = 'user.email') # validators=[UniqueValidator(queryset=User.objects.all())]
    password = serializers.CharField(write_only=True, required=True)


    class Meta:
        model = UserProfile      # MIGHT NEED TO CHANGE TO User, not sure
        fields = ['username', 'email','image', 'about','password']
        
        # fields = '__all__' 

    # def create(self, validated_data):
    #     user = User(
    #         username = validated_data['user']['username'],
    #         email = validated_data['user']['email'],
    #         )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     instance = UserProfile(user=user,
    #                            image = validated_data['image'],  
    #                            about = validated_data['about']
    #                             )
    #     instance.save()
    #     return instance

    