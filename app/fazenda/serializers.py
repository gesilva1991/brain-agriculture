from rest_framework import serializers
from .models import Fazenda, ProdutorRural

class FazendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fazenda
        fields = ['id', 'nome', 'cidade', 'estado', 'area_total', 'area_agricultavel', 'area_vegetacao', 'culturas_plantadas']
    
    def validate(self, data):
        """
        Verifica se a soma da área agricultável e da área de vegetação não é maior que a área total.
        """
        area_total = data.get('area_total')
        area_agricultavel = data.get('area_agricultavel')
        area_vegetacao = data.get('area_vegetacao')

        if area_agricultavel + area_vegetacao > area_total:
            raise serializers.ValidationError("A soma da área agricultável e da área de vegetação não pode ser maior que a área total da fazenda.")

        return (data)

class ProdutorRuralSerializer(serializers.ModelSerializer):
    
    fazendas = FazendaSerializer(read_only=True)

    class Meta:
        model = ProdutorRural
        fields = ['id', 'nome', 'cpf', 'cnpj', 'fazendas']

    def validate(self, data):
        """
        Valida se o CPF e o CNPJ são fornecidos ao mesmo tempo.
        """
        cpf = data.get('cpf')
        cnpj = data.get('cnpj')

        if cpf and cnpj:
            raise serializers.ValidationError("Não é permitido informar tanto CPF quanto CNPJ. Escolha apenas um.")
        
        return data
