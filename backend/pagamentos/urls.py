from django.urls import path, include
from .views import PedidoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet, basename='pedido')

urlpatterns = router.urls