from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "avatar",
            "password",
            "gender",
            "birthday",
            "nickname",
            "age",
        )
        read_only_fields = (
            "id",
            "username",
            "email",
            "nickname",
            "age",
        )

    # def validate_email(self, email):
    #     print(email)
    #     return email

    # def validate_nickname(self, nickname):
    #     print(nickname)
    #     if len(nickname.encode()) <= 5:
    #         raise serializers.ValidationError("too short nickname!")
    #     if len(nickname.encode()) > 18:
    #         raise serializers.ValidationError("too long nickname!")
    #     return nickname

    # def validate_age(self, age):
    #     print(age)
    #     age = int(age)
    #     if age < 5 or age > 100:
    #         raise serializers.ValidationError("Invalid age!")
    #     return age
