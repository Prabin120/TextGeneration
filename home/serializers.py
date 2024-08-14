from rest_framework import serializers
from .models import Summary, BulletPoint

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        exclude = ('id','user')

class BulletPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulletPoint
        exclude = ('id','user')
