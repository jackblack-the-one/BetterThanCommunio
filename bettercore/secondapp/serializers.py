from rest_framework import serializers
from .models import UserOfSecondApp

class CoolSerialzer(serializers.Serializer):
    name = serializers.CharField()
    preferences = serializers.BooleanField()
    age = serializers.IntegerField()