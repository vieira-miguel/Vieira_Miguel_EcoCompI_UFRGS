# lista1_EstruturaControleSequencia
# descricao: o codigo abaixo refere-se as questoes da lista 1 sobre o topico de controle de sequencia
# autor: miguel dos santos pinto vieira
# data: 20/03/2026
# versao: 0.0.8
# notas da versao: correcao do delta

### ALM

#1.
frase1 = ''

#2.
nn1 = 2
nn2 = 3
soma1 = 0

#3.
numero1 = 0.0
numero2 = 0.0
soma2 = 0.0

#4.
username = ''

#5.
h_trab = 0.0
sal = 40      # salario por hora
d_percentual = 0.3
sal_bruto = 0.0
sal_liq = 0.0
d_total = 0.0

#6. 
N = 0
n1 = 0.0
r = 0.0
nN = 0.0       # n-esimo termo da PA

#7.
Ng = 0
n1g = 0.0
g = 0.0
nNg = 0.0     # n-esimo termo da PG

#8.
a = 0.0
b = 0.0
x_sol = 0.0

#9. equacao do segundo grau
a2 = 0.0
b2 = 0.0
c2 = 0.0
delta = 0.0
x_sol_1 = 0.0
x_sol_2 = 0.0

#10.
capital = 0.0
i = 0.0
prazo = 0.0
valor_final = 0.0

#11.
num1 = 0.0
num2 = 0.0
num3 = 0.0
num4 = 0.0
media = 0.0

#12.
raio = 0.0
pi = 3.14
areaC = 0.0

#13.
renda = 0.0
preco = 0.0
qtd = 0.0

#15.
val1 = 0.0
val2 = 0.0
val3 = 0.0
lista = [val1, val2, val3]

#16.
selic = 0.0
ibov = 0.0
beta = 0.0
retorno = 0.0



# Entrada de dados

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

username = input("Qual o seu nome? ")

h_trab = float(input("Quantas horas sao trabalhadas por dia?: "))

N = int(input("Digite o total de termos da PA: "))
n1 = float(input("Digite o primeiro termo da PA: "))
r = float(input("Digite a razao da PA: "))

Ng = int(input("Digite o total de termos da PG: "))
n1g = int(input("Digite o primeiro termo da PG: "))
g = float(input("Digite a razao da PG: "))

a = float(input("Digite um numero a diferente de 0: "))
b = float(input("Digite um numero b diferente de 0: "))

a2 = float(input("Digite um numero a<>0: "))
b2 = float(input("Digite um numero b: "))
c2 = float(input("Digite um numero c: "))

capital = float(input("Insira o capital inicial do investimento: "))
i = float(input("Insira a taxa de juros em porcentagem): "))
prazo = float(input("Insira o prazo do investimento: "))

num1 = float(input("Informe o primeiro termo: "))
num2 = float(input("Informe o segundo termo: "))
num3 = float(input("Informe o terceiro termo: "))
num4 = float(input("Informe o quarto termo: "))

raio = float(input("Diga o raio do circulo: "))

val1 = float(input("Digite um numero real para a lista de tres numeros: "))
val2 = float(input("Digite um numero real para a lista de tres numeros: "))
val3 = float(input("Digite um numero real para a lista de tres numeros: "))

renda = float(input("Qual a renda do consumidor: "))
preco = float(input("Qual o preco do bem: "))

selic = float(input("Qual a selic?: "))
ibov = float(input("Qual o retorno anual esperado do ibovespa?: "))
beta = float(input("Qual o beta da acao?: "))



# Processamento de Dados

frase1 = "Hello World!"

soma1 = nn1 + nn2
soma2 = numero1 + numero2

sal_bruto = sal * h_trab
sal_liq = sal_bruto*(1-d_percentual)
d_total = sal_bruto*d_percentual

nN = n1+r*(N-1)

#nNg = n1g*(g**(Ng-1))

#x_sol = b/a

#delta = b2**2 - 4*(a2*c2)
#x_sol_1 = (-b2 + (delta)**(1/2))/(2*a2)
#x_sol_2 = (-b2 - (delta)**(1/2))/(2*a2)

#i = i/100
#valor_final = round(capital*((1+i)**12), 2)

media = (num1 + num2 + num3 + num4)/4

areaC = 2*pi*raio

lista = [val1, val2, val3]
lista.sort()

qtd = round(renda/preco, 0)

retorno = selic + beta*(ibov-selic)



# Saida de dados
print(frase1)
print(soma1)
print(f"A soma e dada por {soma2}")
print(f"Oi, {username}, como vai? ")
print(f"O salario bruto e: R${sal_bruto}")
print(f"O salario liquido e: R${sal_liq}")
print(f"O salario burto e: R${d_total}")
print(f"O n-esimo termo da PA e: {nN}")
print(f"O n-esimo termo da PG e: {nNg}")
print(f"A solucao da equacao ax = b para x e: x = {x_sol}")
if delta < 0:
   print("As solucoes sao complexas.") 
elif delta == 0:
    print(f"A solucao dupla e: {x_sol_1}")
else:
   print(f"As solucoes sao: x1 = {x_sol_1} e x2 = {x_sol_2}")

print(f"O valor final do investimento e: R${valor_final}")
print(f"A media e: {media}")
print(f"A area do circulo e: {areaC}")
print(lista)
print(f"A quantidade demandada do bem e: {qtd}")
print(f"O retorno previsto da acao por CAPM e: {retorno} ")