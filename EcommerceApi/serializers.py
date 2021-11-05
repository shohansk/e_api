from rest_framework import serializers

from .models import Category,Book,Product

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        field = (
            'id',
            'tittle'
        )
        model = Category

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        field =(
            'id',
            'tittle',
            'category',
            'isbn',
            'pages',
            'stocks',
            'descriptions',
            'imageURL',
            'status',
            'date_created'
        )
        model = Book
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        field =(
            'id',
            'product_tag',
            'name',
            'price',
            'category',
            'stocks',
            'imageURL',
            'status',
            'date_created',
        )
        model = Product
