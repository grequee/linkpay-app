from django.db import models

# Create your models here.

from django.db import models


class Pedido(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("pago", "Pago"),
        ("cancelado", "Cancelado"),
    ]

    descricao = models.CharField("Descrição", max_length=255)
    valor = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default="pendente")
    link_pagamento = models.URLField("Link de Pagamento", blank=True)
    id_preferencia = models.CharField("ID da Preferência", max_length=100, blank=True)
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["-criado_em"]  # mais recentes primeiro

    def __str__(self):
        return f"#{self.id} - {self.descricao} - R$ {self.valor} ({self.get_status_display()})"
