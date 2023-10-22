from rest_framework.routers import DefaultRouter
from products.api.urls import products_router
from django.urls import path, include

router = DefaultRouter()

# Products
router.registry.extend(products_router.registry)

urlpatterns = [
	path("", include(router.urls))
]
