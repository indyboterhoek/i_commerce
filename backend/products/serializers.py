from rest_framework.serializers import ModelSerializer
from products.models import Product, Category, Sale, Coupon, Option, OptionCategory, OptionImage

class ProductSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"

class CategorySerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = "__all__"

class SaleSerializer(ModelSerializer):
	class Meta:
		model = Sale
		fields = "__all__"

class CouponSerializer(ModelSerializer):
	class Meta:
		model = Coupon
		fields = "__all__"

class OptionSerializer(ModelSerializer):
	class Meta:
		model = Option
		fields = "__all__"

class OptionCategorySerializer(ModelSerializer):
	class Meta:
		model = OptionCategory
		fields = "__all__"

class OptionImageSerializer(ModelSerializer):
	class Meta:
		model = OptionImage
		fields = "__all__"