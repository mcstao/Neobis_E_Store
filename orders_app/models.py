from django.db import models
from django.contrib.auth.models import User
from store_app.models import Product


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('processing', 'В процессе'),
        ('completed', 'Завершен'),
        ('canceled', 'Отменен'),
    ]
    ADDRESS_CHOICES = [
        ('default', 'Использовать адрес по умолчанию'),
        ('new', 'Введите новый адрес'),
    ]
    order_user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_products = models.ManyToManyField(Product)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='processing')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='')
    address_option = models.CharField(max_length=150, choices=ADDRESS_CHOICES, default='default')
    new_address = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"Order #{self.id}"

    def save(self, *args, **kwargs):
        if self.address_option == 'default':
            self.address_option = self.order_user.userinfo.address
        super().save(*args, **kwargs)