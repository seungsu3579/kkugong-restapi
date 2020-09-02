from rest_framework import serializers
from .models import Pants, PantsImage


class PantsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PantsImage
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


class PantsSerializer(serializers.ModelSerializer):
    images = PantsImageSerializer(many=True, read_only=True)

    class Meta:
        model = Pants
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
