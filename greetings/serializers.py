from rest_framework import serializers


class GreetingsSerializers(serializers.Serializer):
    name=serializers.CharField()
    brand=serializers.CharField()
    price=serializers.IntegerField()
    specs=serializers.CharField()
    band=serializers.CharField()
    