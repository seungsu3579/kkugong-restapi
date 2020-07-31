from rest_framework import serializers
from .models import Tops


class TopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tops
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
