from rest_framework import serializers
from api.models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock',]
        
    def validate_pruice(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price cannot be negative")
        return value