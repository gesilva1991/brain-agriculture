from rest_framework import serializers
from .models import ProdutorRural


class ProdutorRuralSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProdutorRural
        fields = [
            "id",
            "nome_produtor",
            "nome_fazenda",
            "cpf",
            "cnpj",
            "cidade",
            "estado",
            "area_total",
            "area_agricultavel",
            "area_vegetacao",
            "culturas_plantadas",
        ]

    def validate(self, data):
        """
        Valida se o CPF e o CNPJ são fornecidos ao mesmo tempo.
        """
        cpf = data.get("cpf")
        cnpj = data.get("cnpj")
        area_total = data.get("area_total")
        area_agricultavel = data.get("area_agricultavel")
        area_vegetacao = data.get("area_vegetacao")

        if cpf and cnpj:
            raise serializers.ValidationError(
                "Não é permitido informar tanto CPF quanto CNPJ. Escolha apenas um."
            )

        if area_agricultavel + area_vegetacao > area_total:
            raise serializers.ValidationError(
                "A soma da área agricultável e da área de vegetação não pode ser maior que a área total da fazenda."
            )

        return data


class DashSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProdutorRural
        fields = [
            "id",
            "nome_produtor",
            "nome_fazenda",
            "cpf",
            "cnpj",
            "cidade",
            "estado",
            "area_total",
            "area_agricultavel",
            "area_vegetacao",
            "culturas_plantadas",
        ]
    def validate(self, data):
        """
        Valida se o CPF e o CNPJ são fornecidos ao mesmo tempo.
        """
        cpf = data.get("cpf")
        cnpj = data.get("cnpj")
        area_total = data.get("area_total")
        area_agricultavel = data.get("area_agricultavel")
        area_vegetacao = data.get("area_vegetacao")

        if cpf and cnpj:
            raise serializers.ValidationError(
                "Não é permitido informar tanto CPF quanto CNPJ. Escolha apenas um."
            )

        if area_agricultavel + area_vegetacao > area_total:
            raise serializers.ValidationError(
                "A soma da área agricultável e da área de vegetação não pode ser maior que a área total da fazenda."
            )

        return data