from rest_framework import serializers
from .models import *



class BannerTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerTop
        fields = ['id','name','image']



class BannerDownSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerDown
        fields = ['id','name','image']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','image']



class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source ='category.name',read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','image','category','price','offer_price','offer','unit','category_name','last_update']
