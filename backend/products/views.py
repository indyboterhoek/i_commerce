from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product, Category, Sale, Coupon, Option, OptionCategory, OptionImage
from .serializers import ProductSerializer, CategorySerializer, SaleSerializer, CouponSerializer, OptionSerializer, OptionCategorySerializer, OptionImageSerializer

class ProductViewSet(ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class ProductSearchView(APIView):
	def get(self, request, format=None):
		queryset = Product.objects.all()
		query = request.GET.get('q')
		if query:
			queryset = queryset.filter(name__icontains=query)
		serializer = ProductSerializer(queryset, many=True)
		return Response(serializer.data)
	
class ProductsOnHomePageView(APIView):
	def get(self, request, format=None):
		queryset = Product.objects.all()
		queryset = queryset.filter(display_home=True)
		serializer = ProductSerializer(queryset, many=True)
		return Response(serializer.data)

class ProductsOnSliderView(APIView):
	def get(self, request, format=None):
		queryset = Product.objects.all()
		queryset = queryset.filter(display_slider=True)
		serializer = ProductSerializer(queryset, many=True)
		return Response(serializer.data)

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