from rest_framework import serializers
from .models import Tops


class TopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tops
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
