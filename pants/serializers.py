from rest_framework import serializers
from .models import Pants, PantsImage, UserPants


class PantsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PantsImage
        fields = (
            "id",
            "img_url",
            "img",
            "pants",
        )

        read_only_fields = (
            "id",
            "img_url",
            "img",
            "pants",
        )


class PantsSerializer(serializers.ModelSerializer):
    images = PantsImageSerializer(many=True, read_only=True)

    class Meta:
        model = Pants
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


class UserPantsSerializer(serializers.ModelSerializer):
    meta_pants = PantsSerializer(many=True, read_only=True)

    class Meta:
        model = UserPants
        fields = (
            "id",
            "nickname",
            "user",
            "img",
            "meta_pants",
            "jjim",
        )

        read_only_fields = (
            "id",
            "nickname",
            "user",
            "img",
            "meta_pants",
            "jjim",
        )
