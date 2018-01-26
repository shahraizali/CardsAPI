from rest_framework import serializers

from cards.models import Card


class CardSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer form model of card"""
    # name = serializers.CharField(max_length=10)
    # email = serializers.EmailField()
    # address = serializers.CharField(max_length=30)
    # phoneNumber = serializers.IntegerField()
    class Meta:
        model = Card
        fields = ('id','name', 'address', 'phoneNumber', 'email')
