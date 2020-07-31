from rest_framework import serializers
from .models import Pants


class PantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pants
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
