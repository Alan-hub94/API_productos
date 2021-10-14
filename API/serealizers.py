from .models import *
from rest_framework import serealizers


class ProductoSereaziler(serealizers.HyperLinkedModelSerealizer):
    class Meta:
        model = productos
        fields = '__all__'

