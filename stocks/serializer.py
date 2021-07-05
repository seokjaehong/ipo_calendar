from rest_framework import serializers

from stocks.models import IPO


class IPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPO
        fields = ('ipo_id',)
