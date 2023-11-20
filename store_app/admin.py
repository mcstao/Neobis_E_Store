from django.contrib import admin
from store_app.models import Category, Comment, Product, Review, UserInfo

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(UserInfo)
