from rest_framework.viewsets import ModelViewSet
from products.models import Product, Category, Sale, Coupon, Option, OptionCategory, OptionImage
from .serializers import ProductSerializer, CategorySerializer, SaleSerializer, CouponSerializer, OptionSerializer, OptionCategorySerializer, OptionImageSerializer

class ProductViewSet(ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class CategoryViewSet(ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class SaleViewSet(ModelViewSet):
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer

class CouponViewSet(ModelViewSet):
	queryset = Coupon.objects.all()
	serializer_class = CouponSerializer

class OptionViewSet(ModelViewSet):
	queryset = Option.objects.all()
	serializer_class = OptionSerializer

class OptionCategoryViewSet(ModelViewSet):
	queryset = OptionCategory.objects.all()
	serializer_class = OptionCategorySerializer

class OptionImageViewSet(ModelViewSet):
	queryset = OptionImage.objects.all()
	serializer_class = OptionImageSerializer