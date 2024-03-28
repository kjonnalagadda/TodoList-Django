from rest_framework import serializers
from .models import UserRegister, UserTodoList
from django.contrib.auth.hashers import make_password

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = ['id', 'Username', 'Firstname', 'Lastname', 'Age', 'Email', 'Password', 'Confirm_Password']
    
    def create(self, validated_data):
        # Extract password and confirm password from validated_data
        password = validated_data.pop('Password')
        confirm_password = validated_data.pop('Confirm_Password')

        if password != confirm_password:
            raise serializers.ValidationError("The passwords do not match.")
        else:
            hashed_password = make_password(password)
            hashed_password1 = make_password(confirm_password)
            return UserRegister.objects.create(Password=hashed_password, Confirm_Password=hashed_password1, **validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = ['Username', 'Password']

class UserTodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTodoList
        fields = '__all__'