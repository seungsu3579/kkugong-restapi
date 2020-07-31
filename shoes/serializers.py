from rest_framework import serializers
from .models import Shoes


class ShoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoes
        fields = (
            "id",
            "_id",
            "brand",
            "product",
            "item_url",
        )

        read_only_fields = (
            "id",
            "_id",
            "brand",
            "product",
            "item_url",
        )
