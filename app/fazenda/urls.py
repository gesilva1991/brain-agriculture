from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FazendaViewSet, ProdutorRuralViewSet

router = DefaultRouter()
router.register(r'fazendas', FazendaViewSet)
router.register(r'produtores-rurais', ProdutorRuralViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
