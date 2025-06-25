from rest_framework import serializers
from .models import OTTShow, Watchlist

class OTTShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTTShow
        fields = '__all__'

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = '__all__'
