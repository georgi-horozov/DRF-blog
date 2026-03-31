from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import CustomUserModel


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length = 80)
    password = serializers.CharField(min_length = 8, write_only = True)

    class Meta:
        model = CustomUserModel
        fields = ["email", "password"]

    def validate(self, attrs):
        email_exists = CustomUserModel.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError("Email has already been used")

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)
        user.set_password(password)  # 🔥 ключовото
        user.save()

        return user