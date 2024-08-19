from django.test import TestCase

# produtores/test_fazenda.py
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Fazenda



class FazendaAPITests(APITestCase):

    def setUp(self):
        self.fazenda_data = {
            'nome': 'Fazenda Teste',
            'cidade': 'Cidade Teste',
            'estado': 'SP',
            'area_total': 100.0,
            'area_agricultavel': 50.0,
            'area_vegetacao': 30.0,
            'culturas_plantadas': 'Soja'
        }
    
    def test_fazenda_create(self):
        response = self.client.post('/api/fazendas/', self.fazenda_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], 'Fazenda Teste')

    def test_fazenda_list(self):
        self.client.post('/api/fazendas/', self.fazenda_data, format='json')
        response = self.client.get('/api/fazendas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fazenda_update(self):
        response = self.client.post('/api/fazendas/', self.fazenda_data, format='json')
        fazenda_id = response.data['id']
        update_data = {
            'nome': 'Fazenda Atualizada',
            'cidade': 'Cidade Atualizada',
            'estado': 'SP',
            'area_total': 120.0,
            'area_agricultavel': 60.0,
            'area_vegetacao': 40.0,
            'culturas_plantadas': 'Soja'
        }
        response = self.client.put(f'/api/fazendas/{fazenda_id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Fazenda Atualizada')

    def test_fazenda_delete(self):
        response = self.client.post('/api/fazendas/', self.fazenda_data, format='json')
        fazenda_id = response.data['id']
        response = self.client.delete(f'/api/fazendas/{fazenda_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f'/api/fazendas/{fazenda_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
