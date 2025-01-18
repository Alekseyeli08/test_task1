from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sales_network/', include('sales_network.urls', namespace='sales_network')),
]
