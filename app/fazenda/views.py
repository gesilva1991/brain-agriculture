from django.shortcuts import render
from rest_framework import viewsets
from .models import ProdutorRural
from .serializers import ProdutorRuralSerializer, DashSerializer
from rest_framework.response import Response


class ProdutorRuralViewSet(viewsets.ModelViewSet):
    queryset = ProdutorRural.objects.all()
    serializer_class = ProdutorRuralSerializer


class DashboardViewSet(viewsets.ModelViewSet):
    queryset = ProdutorRural.objects.all()
    serializer_class = DashSerializer

    def list(self, request):
        total_fazendas = ProdutorRural.objects.count()

        # Gráficos de pizza

        data = {
            "total_fazendas": total_fazendas,
            "uso_do_solo": total_fazendas,
        }

        return Response(data)
