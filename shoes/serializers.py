from rest_framework import serializers
from .models import Shoes, ShoesImage


class ShoesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoesImage
        fields = (
            "_id",
            "img_url",
            "img_dir",
            "top",
        )

        read_only_fields = (
            "_id",
            "img_url",
            "img_dir",
            "top",
        )


class ShoesSerializer(serializers.ModelSerializer):
    images = ShoesImageSerializer(many=True, read_only=True)

    class Meta:
        model = Shoes
        fields = (
            "_id",
            "brand",
            "product",
            "item_url",
            "images",
        )

        read_only_fields = (
            "_id",
            "brand",
            "product",
            "item_url",
            "images",
        )
