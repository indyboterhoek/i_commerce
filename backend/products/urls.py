from django.urls import path
from .views import ProductViewSet, CategoryViewSet, SaleViewSet, CouponViewSet, OptionViewSet, OptionCategoryViewSet, OptionImageViewSet, ProductSearchView, ProductsOnHomePageView, ProductsOnSliderView

urlpatterns = [
	path('product/search', ProductSearchView.as_view(), name="productsearch"),
	path('product/home', ProductsOnHomePageView.as_view(), name="productshome"),
	path('product/slider', ProductsOnSliderView.as_view(), name="productsslider"),
	path('product/<slug:slug>', ProductViewSet.as_view({'get': 'retrieve'}), name="product"),
]


# Products
""" products_router.register("products/product", ProductViewSet, basename="products")
products_router.register("products/producthome", ProductsOnHomePageView, basename="productshome")
products_router.register("products/productslider", ProductsOnSliderView, basename="productsslider") """


""" products_router.register("products/category", CategoryViewSet, basename="categories")
products_router.register("products/sale", SaleViewSet, basename="sales")
products_router.register("products/coupon", CouponViewSet, basename="coupons")
products_router.register("products/option", OptionViewSet, basename="options")
products_router.register("products/optioncategory", OptionCategoryViewSet, basename="optioncategories")
products_router.register("products/optionimage", OptionImageViewSet, basename="optionimages") """