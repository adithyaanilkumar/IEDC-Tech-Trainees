from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AuthorProfile
from rest_framework.validators import UniqueValidator



class AuthorProfileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False,default='default.jpg')
    nickname = serializers.CharField(max_length=50, default= 'user.username')       #chck this LINE!!!!!!!!!!!!!
    username = serializers.CharField(source = 'user.username' )  #validators=[UniqueValidator(queryset=User.objects.all())]
    email    = serializers.EmailField(source = 'user.email') # validators=[UniqueValidator(queryset=User.objects.all())]
    password = serializers.CharField(write_only=True, required=True)
    
    # username = serializers.CharField(source = 'user.username',
    #                                     validators=[UniqueValidator(queryset=User.objects.all())] )
    # email    = serializers.EmailField(source = 'user.email',
    #                                     validators=[UniqueValidator(queryset=User.objects.all())]
    #                                     )

    class Meta:
        model = AuthorProfile     # MIGHT NEED TO CHANGE TO User, not sure
        fields = ['username', 'email','image', 'nickname','password']


    # def create(self, validated_data):
    #     user = User(
    #         username = validated_data['user']['username'],
    #         email = validated_data['user']['email'],
    #         )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     instance = AuthorProfile(user=user,
    #                            image = validated_data['image'],  
    #                            nickname = validated_data['nickname']
    #                             )
    #     instance.save()
    #     return instance