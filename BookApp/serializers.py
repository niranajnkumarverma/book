from rest_framework import serializers
from .models import Product, User,Cart

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'    
class CartItemSerializer(serializers.ModelSerializer):
    
    # product_name = serializers.CharField(max_length=200)
    # product_price = serializers.FloatField()
    # product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = Cart
        fields = ('__all__')            