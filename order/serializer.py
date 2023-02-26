from rest_framework import serializers
from order.models import Shop, Order, OrderFood, Menu


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class OrderFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFood
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    orderfood_set = OrderFoodSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'