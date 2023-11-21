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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories',
                                 verbose_name='Категории')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    image = models.ImageField(verbose_name='Фото продукта', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator', verbose_name='Автор')

    def __str__(self):
        return self.product_name

    @property
    def rating(self):
        total_amount = self.reviews.all().count()
        if total_amount == 0:
            return 0
        sum_ = 0
        for i in self.reviews.all():
            sum_ += i.stars
        return sum_ / total_amount


class UserInfo(models.Model):
    user = models.OneToOneField(User,related_name='userinfo', on_delete=models.CASCADE)
    address = models.CharField(max_length=150, verbose_name='Адресс')
    REQUIRED_FIELDS = ['address']

    def __str__(self):
        return self.user.username


class Review(models.Model):
    product_reviews = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews',
                                        verbose_name='Отзывы')
    review_text = models.TextField(max_length=1000, verbose_name='Текст отзыва')
    stars = models.IntegerField(default=0, verbose_name='Рейтинг')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author',
                               verbose_name='Автор отзыва')

    def __str__(self):
        return self.review_text


class Comment(models.Model):
    product_comments = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',
                                         verbose_name='Комментарии')
    comment_text = models.TextField(max_length=1000, verbose_name='Текст комментария')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author',
                               verbose_name='Автор комментария')

    def __str__(self):
        return self.comment_text
