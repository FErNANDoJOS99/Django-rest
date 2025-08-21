# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from .views import UsuarioViewSet
from .views import *


router = DefaultRouter()
router.register(r"usuarios", UsuarioViewSet)
router.register(r"listas", ListaViewSet)
router.register(r"articulos", ArticuloViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
