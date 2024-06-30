from rest_framework import serializers

from announcement.models import Adt, Review


class AdtSerializers(serializers.ModelSerializer):
    class Meta:
        model = Adt
        fields = "__all__"


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
