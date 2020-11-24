from rest_framework import serializers
from .models import Cody


class CodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cody
        fields = (
            "id",
            "img",
        )

        read_only_fields = (
            "id",
            "img",
        )


class CodyRecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cody
        fields = (
            "id",
            "img",
            "jjim",
        )

        read_only_fields = (
            "id",
            "img",
            "jjim",
        )
