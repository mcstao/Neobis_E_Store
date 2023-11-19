from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категории')

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=10000, verbose_name='Описание')
    price = models.DecimalField(max_digits=20, decimal_places=3, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    created_time = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    modified_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')
    image = models.ImageField(upload_to='media/', verbose_name='Фото продукта')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')

    def __str__(self):
        return self.product_name

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=150, verbose_name='Адресс')

    def __str__(self):
        return self.user.username

class Review(models.Model):
    product_reviews = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField(max_length=1000, verbose_name='Текст отзыва')
    stars = models.ImageField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return self.review_text
class Comment(models.Model):
    product_comments = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField(max_length=1000, verbose_name='Текст комментария')

    def __str__(self):
        return self.comment_text
