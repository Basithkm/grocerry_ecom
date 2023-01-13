from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import * 
from . serializer import *

# Create your views here.


class BannerTopViewSet(ModelViewSet):
    queryset =BannerTop.objects.all()
    serializer_class = BannerTopSerializer



class BannerDownViewSet(ModelViewSet):
    queryset = BannerDown.objects.all()
    serializer_class  = BannerDownSerializer



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

