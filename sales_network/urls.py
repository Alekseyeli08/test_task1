from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sales_network.apps import SalesNetworkConfig
from .views import SupplierViewSet, ProductViewSet, NodeViewSet

app_name = SalesNetworkConfig


router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'node', NodeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]