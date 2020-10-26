from rest_framework import serializers
from .models import Shoes, ShoesImage, UserShoes


class ShoesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoesImage
        fields = (
            "id",
            "img_url",
            "img",
            "shoes",
        )

        read_only_fields = (
            "id",
            "img_url",
            "img",
            "shoes",
        )


class ShoesSerializer(serializers.ModelSerializer):
    images = ShoesImageSerializer(many=True, read_only=True)

    class Meta:
        model = Shoes
        fields = (
            "id",
            "brand",
            "product",
            "item_url",
            "images",
        )

        read_only_fields = (
            "id",
            "brand",
            "product",
            "item_url",
            "images",
        )


class UserShoesSerializer(serializers.ModelSerializer):
    meta_shoes = ShoesSerializer(many=True, read_only=True)

    class Meta:
        model = UserShoes
        fields = (
            "id",
            "nickname",
            "user",
            "img",
            "meta_shoes",
            "jjim",
        )

        read_only_fields = (
            "id",
            "nickname",
            "user",
            "img",
            "meta_shoes",
            "jjim",
        )

