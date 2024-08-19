from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutorRuralViewSet

router = DefaultRouter()
router.register(r"produtores", ProdutorRuralViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
