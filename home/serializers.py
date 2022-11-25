from attr import fields, validate
from pkg_resources import require
from rest_framework import serializers
from home.models import Task ,UserProfile
from django.contrib.auth.models import User

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')
        extra_kwargs = {
             'first_name': {'required': True},
            'last_name': {'required': True}
        }
        
        # def create(self, validated_data):
        #     user = User.objects.create(
        #         username=validated_data['username'],
        #         email=validated_data['email'],
        #         first_name=validated_data['first_name'],
        #         last_name=validated_data['last_name']
        #     )

            
        #     user.set_password(validated_data['password'])
        #     user.save()

        #     return user
        

class UserProfileSerializer(serializers.ModelSerializer):
    
    user = UserSerializers()
    class Meta:
        model = UserProfile
        fields = ('user','age','education',)
        
    
    def create(self,validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializers.create(UserSerializers(),validated_data = user_data)
        student = UserProfile.objects.create(user = user,age = validated_data.pop('age'),education = validated_data.pop('education'))
        
        return student
        
    
    