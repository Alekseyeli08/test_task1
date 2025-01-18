from rest_framework import viewsets
from .models import Supplier, Product, Node
from .serializers import SupplierSerializer, ProductSerializer, NodeSerializer
from rest_framework.permissions import IsAuthenticated

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.query_params.get('country', None)
        if country is not None:
            queryset = queryset.filter(country=country)
        return queryset

    def perform_update(self, serializer):
        serializer.save(debt=self.get_object().debt)