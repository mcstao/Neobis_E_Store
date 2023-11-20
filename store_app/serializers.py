from rest_framework import serializers
from .models import Product, Category, Comment, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'username', 'comment_text', 'author']


class ReviewSerializer(serializers.ModelSerializer):
    review_text = serializers.CharField(min_length=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    product_reviews_id = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ['id', 'product_reviews_id', 'review_text', 'stars', 'author']


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'author', 'image', 'product_name', 'description', 'price', 'category', 'reviews', 'rating',
                  'created_time', 'modified_time']
