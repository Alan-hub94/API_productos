from django.contrib import admin
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('API_productos.urls'))
]


admin.site.site_header = 'API REST PRODUCTOS'