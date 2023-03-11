from . models import *
from rest_framework import serializers

class CropRecommenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropRecommender
        fields = '__all__'