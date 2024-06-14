
from django.contrib import admin
from django.urls import path, include
from AppMiranda.views import producto, lista_productos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app-miranda/', include('AppMiranda.urls')),
]
