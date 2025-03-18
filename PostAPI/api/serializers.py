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
    
    
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product', 'quantity')    
    
    
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ('order_id', 'user', 'created_at', 'status', 'items')
        