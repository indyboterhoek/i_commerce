from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, SaleViewSet, CouponViewSet, OptionViewSet, OptionCategoryViewSet, OptionImageViewSet

products_router = DefaultRouter()
products_router.register("products/product", ProductViewSet, basename="products")
products_router.register("products/category", CategoryViewSet, basename="categories")
products_router.register("products/sale", SaleViewSet, basename="sales")
products_router.register("products/coupon", CouponViewSet, basename="coupons")
products_router.register("products/option", OptionViewSet, basename="options")
products_router.register("products/optioncategory", OptionCategoryViewSet, basename="optioncategories")
products_router.register("products/optionimage", OptionImageViewSet, basename="optionimages")