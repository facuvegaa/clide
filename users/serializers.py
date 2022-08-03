from rest_framework import serializers
from .models import Seller, User, Client

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:    
            instance.set_password(password)
        instance.save()
        return instance


class ClientSerializaer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_client']
        extra_kwargs = {
            'password' : {'write_only' : True},
        }

    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:    
            instance.set_password(password)
        instance.save()
        Client.objects.create(user = instance)
        return instance


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_seller']
        extra_kwargs = {
            'password' : {'write_only' : True},
        }

    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:    
            instance.set_password(password)
        instance.save()
        Seller.objects.create(user = instance)
        return instance
