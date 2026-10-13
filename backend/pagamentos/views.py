from django.shortcuts import render

# Create your views here.
import os
import mercadopago
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Pedido
from .serializers import PedidoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def perform_create(self, serializer):
        # 1. Salva o pedido como "pendente"
        pedido = serializer.save(status="pendente")

        # 2. Chama a API do Mercado Pago (usando o token de teste do .env)
        sdk = mercadopago.SDK(os.getenv("MP_ACCESS_TOKEN"))
        dados_preferencia = {
            "items": [{
                "title": pedido.descricao,
                "quantity": 1,
                "unit_price": float(pedido.valor),
                "currency_id": "BRL",
            }],
            "external_reference": str(pedido.id),
        }
        resultado = sdk.preference().create(dados_preferencia)

        # 3. Salva o link e o ID retornados pelo Mercado Pago
        pedido.link_pagamento = resultado["response"]["init_point"]
        pedido.id_preferencia = resultado["response"]["id"]
        pedido.save()
