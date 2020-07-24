from rest_framework import serializers
from .models import User
from tops.serializers import TopsSerializer
from pants.serializers import PantsSerializer
from shoes.serializers import ShoesSerializer


class UserSerializer(serializers.ModelSerializer):

    # password는 보이지 않게
    password = serializers.CharField(write_only=True)

    class Meta:
        # serialize 대상 모델
        model = User

        # json으로 serialize해서 보여줄 fields
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
            "tops",
            "pants",
            "shoes",
        )

        # 읽기만 가능한 fields
        read_only_fields = ("id",)

    # validation 검사
    def validated_username(self, username):
        if self.instance:
            raise serializers.ValidationError("You can't change username(id)")

    def validate_nickname(self, nickname):
        if len(nickname.encode()) <= 5:
            raise serializers.ValidationError("too short nickname!")
        if len(nickname.encode()) > 18:
            raise serializers.ValidationError("too long nickname!")
        return nickname

    def validate_age(self, age):
        age = int(age)
        if age < 5 or age > 100:
            raise serializers.ValidationError("Invalid age!")
        return age

    def create(self, validated_data):
        password = validated_data.get("password")  # 암호화할 비밀번호 get
        user = super().create(validated_data)  # user객체 생성
        user.set_password(password)  # user객체 password 암호화해서 저장
        user.save()  # user 저장
        return user


class UserClosetSerializer(serializers.ModelSerializer):

    tops = TopsSerializer()
    pants = PantsSerializer()
    shoes = ShoesSerializer()

    class Meta:
        model = User
        fields = (
            "id",
            "tops",
            "pants",
            "shoes",
        )
        read_only_fields = ("id",)
