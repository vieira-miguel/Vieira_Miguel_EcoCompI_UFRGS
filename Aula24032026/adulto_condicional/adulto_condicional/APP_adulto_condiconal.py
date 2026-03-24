"""
Programa adulto_condicional
Descrição: esse programa pergunta ao usuário sua idade e analisa se é maior de idade (>=18) ou menor:
Autor: Miguel dos Santos Pinto Vieira
Data: 24/03/2026
Versão: 0.0.2
Atualização da versão: transforma idade de string para input

"""


# Alocação de memória

idade = 0
texto = ""



# Entrada de Dados

idade = int(input("Digite sua idade: "))


# Processamento de Dados

if idade >= 18:
    texto = 'Oi! Você é um adulto!'
else:
    texto = 'Oi! Você é menor!'


# Saída de Dados
print(texto)
    