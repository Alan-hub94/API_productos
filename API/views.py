from rest_framework import viewsets
from .serializers import ProductoSerializer
from .models import *

class productosViewSet(viewsets.ModelViewSet):
    queryset = productos.objects.all().order_by('name')
    serializer_class = ProductoSerializer


