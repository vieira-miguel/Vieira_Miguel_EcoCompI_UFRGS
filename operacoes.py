# -*- coding: utf-8 -*-

#exercicio_operacoes
#O programa le dois numeros reais e faz as seguintes operacoes: soma, subtracao, multiplicacao, divisao, exponenciacao e radiciacao
#Autor: Miguel dos Santos Pinto Vieira
#Data: 17/03/2026
#Versao 0.1.0
#Obs: caso o resultado da operacao nao esteja no dominio dos reais, dara erro.
#Lembrar de remover a primeira linha caso o terminal seja bash


# ALM num

numero_1 = 0.0
numero_2 = 0.0

# ALM operacoes
soma = 0.0
sub = 0.0
mult = 0.0
div = 0.0
exp = 0.0
rad = 0.0


# Entrada de dados
numero_1 = float(input("Insira o primeiro valor: "))
numero_2 = float(input("Insira o segundo valor: "))


# Processamento de dados
soma = numero_1 + numero_2 
sub = numero_1 - numero_2
mult = numero_1 * numero_2
div = numero_1 / numero_2
exp = numero_1 ** numero_2
rad = numero_1 ** (1/numero_2)


# Saida de dados
print(f"A soma dos numeros e: {soma}")
print(f"A subtracao dos numeros e: {sub}")
print(f"A multiplicacao dos numeros e: {mult}")
print(f"A divisao dos numeros e: {div}")
print(f"A exponenciacao dos numeros e: {exp}")
print(f"A radiciacao dos numeros e: {rad}")