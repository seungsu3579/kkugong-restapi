from rest_framework import serializers
from .models import Tops, TopsImage


class TopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopsImage
        fields = (
            "_id",
            "img_url",
            "img_dir",
            "top",
        )

        read_only_fields = (
            "_id",
            "brand",
            "product",
            "item_url",
        )


class TopsSerializer(serializers.ModelSerializer):
    images = TopImageSerializer()

    class Meta:
        model = Tops
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
        )
