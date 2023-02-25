from rest_framework import serializers
from order.models import Shop,Order,OrderFood,Menu

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        # fields = ['id', 'title', 'code', 'linenos', 'language', 'style']