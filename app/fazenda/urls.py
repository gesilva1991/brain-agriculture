from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutorRuralViewSet, DashboardViewSet

router = DefaultRouter()
router.register(r"produtores", ProdutorRuralViewSet)
router.register(r"dashboard", DashboardViewSet, basename="dashboard")


urlpatterns = [
    path("", include(router.urls)),
]
