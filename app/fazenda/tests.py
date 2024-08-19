from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import ProdutorRural
from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import ProdutorRural


class ProdutorRuralModelTest(TestCase):

    def setUp(self):
        self.valid_data = {
            "nome": "João da Silva",
            "cpf": "12345678901",
            "cidade": "São Paulo",
            "estado": "SP",
            "area_total": 100.0,
            "area_agricultavel": 60.0,
            "area_vegetacao": 30.0,
            "culturas_plantadas": "Soja",
        }

        self.invalid_area_data = self.valid_data.copy()
        self.invalid_area_data.update(
            {"area_agricultavel": 70.0, "area_vegetacao": 40.0}
        )

        self.invalid_cpf_cnpj_data = self.valid_data.copy()
        self.invalid_cpf_cnpj_data.update({"cnpj": "12345678000195"})

    def test_valid_produtor_rural(self):
        produtor = ProdutorRural.objects.create(**self.valid_data)
        self.assertEqual(produtor.nome, "João da Silva")
        self.assertEqual(produtor.cpf, "12345678901")
        self.assertEqual(produtor.cidade, "São Paulo")
        self.assertEqual(produtor.estado, "SP")
        self.assertEqual(produtor.area_total, 100.0)
        self.assertEqual(produtor.area_agricultavel, 60.0)
        self.assertEqual(produtor.area_vegetacao, 30.0)
        self.assertEqual(produtor.culturas_plantadas, "Soja")

    def test_area_validation(self):
        produtor = ProdutorRural(**self.invalid_area_data)
        with self.assertRaises(ValidationError):
            produtor.clean()

    def test_cpf_and_cnpj_validation(self):
        produtor = ProdutorRural(**self.invalid_cpf_cnpj_data)
        with self.assertRaises(ValidationError):
            produtor.clean()

    def test_clean_method(self):
        # Test CPF and CNPJ validation (should raise an error)
        produtor = ProdutorRural(
            nome="João da Silva",
            cpf="12345678901",
            cnpj="12345678000195",
            cidade="São Paulo",
            estado="SP",
            area_total=100.0,
            area_agricultavel=60.0,
            area_vegetacao=30.0,
            culturas_plantadas="Soja",
        )
        with self.assertRaises(ValidationError):
            produtor.clean()


class ProdutorRuralAPITests(APITestCase):

    def setUp(self):
        self.valid_data = {
            "nome": "João da Silva",
            "cpf": "12345678901",
            "cidade": "São Paulo",
            "estado": "SP",
            "area_total": 100.0,
            "area_agricultavel": 60.0,
            "area_vegetacao": 30.0,
            "culturas_plantadas": "Soja",
        }

    def test_produtor_create(self):
        response = self.client.post(
            "/api/produtores-rurais/", self.valid_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["nome"], "João da Silva")

    def test_produtor_list(self):
        self.client.post("/api/produtores-rurais/", self.valid_data, format="json")
        response = self.client.get("/api/produtores-rurais/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_produtor_update(self):
        response = self.client.post(
            "/api/produtores-rurais/", self.valid_data, format="json"
        )
        fazenda_id = response.data["id"]
        update_data = {
            "nome": "João Atualizado",
            "cpf": "12345678901",
            "cidade": "São Paulo Atualizado",
            "estado": "SP",
            "area_total": 100.0,
            "area_agricultavel": 60.0,
            "area_vegetacao": 30.0,
            "culturas_plantadas": "Soja",
        }
        response = self.client.put(
            f"/api/produtores-rurais/{fazenda_id}/", update_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], "João Atualizado")

    def test_produtor_delete(self):
        response = self.client.post(
            "/api/produtores-rurais/", self.valid_data, format="json"
        )
        produtor_id = response.data["id"]
        response = self.client.delete(f"/api/produtores-rurais/{produtor_id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f"/api/produtores-rurais/{produtor_id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
