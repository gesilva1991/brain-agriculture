from django.shortcuts import render

from rest_framework import viewsets
from .models import Fazenda, ProdutorRural
from .serializers import FazendaSerializer, ProdutorRuralSerializer

class FazendaViewSet(viewsets.ModelViewSet):
    queryset = Fazenda.objects.all()
    serializer_class = FazendaSerializer

class ProdutorRuralViewSet(viewsets.ModelViewSet):
    queryset = ProdutorRural.objects.all()
    serializer_class = ProdutorRuralSerializer

