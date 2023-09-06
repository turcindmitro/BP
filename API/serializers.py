from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer  # Подключите сериализатор для продуктов, если необходимо

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)  # Сериализатор для связанных элементов заказа

    class Meta:
        model = Order
        fields = '__all__'
