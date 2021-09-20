from clientes.validators import cpf_valido
from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({"cpf": "CPF inválido"})
    
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({"celular": "O número de celular deve seguir esse padrão: XX XXXXX-XXXX"})
        
        return data


    