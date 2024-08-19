from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


# Validador para CPF e CNPJ
cpf_validator = RegexValidator(
    regex=r"^\d{11}$", message="O CPF deve ter 11 dígitos numéricos."
)

cnpj_validator = RegexValidator(
    regex=r"^\d{14}$", message="O CNPJ deve ter 14 dígitos numéricos."
)


class ProdutorRural(models.Model):

    AREA_CHOICES = [
        ("Soja", "Soja"),
        ("Milho", "Milho"),
        ("Algodão", "Algodão"),
        ("Café", "Café"),
        ("Cana de Açúcar", "Cana de Açúcar"),
    ]

    nome_produtor = models.CharField(max_length=100)
    nome_fazenda = models.CharField(max_length=100)
    cpf = models.CharField(
        max_length=11, validators=[cpf_validator], unique=True, blank=True, null=True
    )
    cnpj = models.CharField(
        max_length=14, validators=[cnpj_validator], unique=True, blank=True, null=True
    )
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, help_text="Exemplo: SP")
    area_total = models.FloatField(help_text="Área total da fazenda em hectares")
    area_agricultavel = models.FloatField(help_text="Área agricultável em hectares")
    area_vegetacao = models.FloatField(help_text="Área de vegetação em hectares")
    culturas_plantadas = models.CharField(
        max_length=100, choices=AREA_CHOICES, help_text="Culturas plantadas"
    )

    def clean(self):
        # Validação para garantir que apenas CPF ou CNPJ é fornecido, não ambos
        if self.area_agricultavel + self.area_vegetacao > self.area_total:
            raise ValidationError(
                "A soma da área agricultável e da área de vegetação não pode ser maior que a área total da fazenda."
            )

        if self.cpf and self.cnpj:
            raise ValidationError(
                "Não é permitido informar tanto CPF quanto CNPJ. Escolha apenas um."
            )

    def __str__(self):
        return self.nome
