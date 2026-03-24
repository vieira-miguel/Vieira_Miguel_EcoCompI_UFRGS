"""
Programa adulto
Descrição: Esse programa pergunta a idade de uma pessoa. Se, idade > 18, printa adulto, se não. negativa
Autor: Miguel dos Santos Pinto Vieira
Data: 24/03/2026
Versão: 0.0.1
"""

# Alocação de Memória

idade = 0
texto = ""


# Entrada de Dados

idade = int(input("\nDigite sua idade: "))


# Processamento de Dados

if idade >= 18:
    texto = 'Oi! Você é um adulto.'


# Saída de Dados

print(texto)
