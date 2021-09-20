import re
from validate_docbr import CPF

def cpf_valido(cpf):
    num_cpf = CPF()
    return num_cpf.validate(cpf) 

def celular_valido(celular):
    """
    Verifica se o celular é válido de acordo com regex (XX XXXXX-XXXX)
    """

    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)

    return resposta