from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8,write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email','name','password']

    def create_user(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            isinstance.set_password(password)
        instance.save()

        return instance

