from django.db import models

class Financeiro(models.Model):
    identificacao_da_conta = models.CharField(max_length=30)
    valor_da_conta = models.DecimalField(decimal_places=2, max_digits=999999999)
    def __str__(self):
        return self.identificacao_da_conta