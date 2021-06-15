from django.db import models

class Evento(models.Model):
    nome_evento = models.CharField(max_length=50)
    def __str__(self):
        return self.nome_evento
        
