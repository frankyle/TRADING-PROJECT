# serializers.py
from rest_framework import serializers
from .models import MgiCandles

class MgiCandlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MgiCandles
        fields = (
            'id', 'user', 'signal', 'timestamp', 'trade_signal', 'is_active',
            'idea_candle', 'line_graph_candle', 'signal_candle'
        )
        read_only_fields = ('id', 'timestamp')
