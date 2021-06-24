from django.db.models import Q
from django.shortcuts import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Serie, Brand
from .serializers import ProductSerializer, SerieSerializer, BrandSerializer

# Create your views here.
class ProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
