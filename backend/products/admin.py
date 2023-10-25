from django.contrib import admin
from .models import Product, Category, Sale, Coupon, Option, OptionCategory, OptionImage

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Sale)
admin.site.register(Coupon)
admin.site.register(Option)
admin.site.register(OptionCategory)
admin.site.register(OptionImage)