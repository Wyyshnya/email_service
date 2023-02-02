from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    email = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=255)
    second_name = serializers.CharField(max_length=255)

    class Meta:
        model = Customer
        fields = ('id', 'email', 'first_name', 'second_name')