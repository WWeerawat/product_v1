from rest_framework import serializers

from .models import Serie, Brand, Category, Product


class BrandRelatedSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)

    class Meta:
        model = Brand
        fields = [
            "id",
            "name",
        ]


class SerieRelatedSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)

    class Meta:
        model = Serie
        fields = [
            "id",
            "name",
        ]


class CategoryRelatedSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class ProductSerializer(serializers.ModelSerializer):
    serie = SerieRelatedSerializer()
    brand = BrandRelatedSerializer()
    category = CategoryRelatedSerializer()

    class Meta:
        model = Product
        fields = (
            "id",
            "id1",
            "id2",
            "name",
            "category",
            "unit",
            "serie",
            "brand",
            "subID",
            "subID2",
            "subID2",
            "minReq",
            "maxReq",
            "departmentPrice",
            "rate",
            "specialAttr",
            "cost",
            "get_absolute_url",
        )


class BrandSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)

    class Meta:
        model = Brand
        fields = (
            "id",
            "name",
            "get_absolute_url",
            # "products",
        )


class SerieSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)

    class Meta:
        model = Serie
        fields = (
            "id",
            "name",
            "get_absolute_url",
            # "products",
        )