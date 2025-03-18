from django.shortcuts import render
from django.shortcuts import get_object_or_404
from api.models import User, Product, Order, OrderItem  
from api.serializers import ProductSerializer, OrderItemSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(["GET"])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)