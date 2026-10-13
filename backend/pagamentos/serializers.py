from rest_framework import serializers
from .models import Pedido


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ["id", "descricao", "valor", "status", "link_pagamento", "criado_em", "atualizado_em"]
        read_only_fields = ["status", "link_pagamento", "criado_em", "atualizado_em"]
