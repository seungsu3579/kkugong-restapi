from rest_framework import serializers
from .models import Shoes


class ShoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoes
        fields = (
            "_id",
            "brand",
            "product",
            "item_url",
        )

        read_only_fields = (
            "_id",
            "brand",
            "product",
            "item_url",
        )
