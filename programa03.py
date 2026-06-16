# Calculadora python
from operator import add

num1 = int(input("Digite o primeiro numero:"))

num2 = int(input("Digite o segundo numero:"))

soma = num1+num2
print(f"A soma de {num1} e {num2} é igual a = {soma}")
subtracao = num1-num2
print(f"A subtracao de {num1} e {num2} é igual a = {subtracao}")
multiplicacao = num1*num2
print(f"A multiplicacao de {num1} e {num2} é igual a = {multiplicacao}")
divisao = num1/num2
print(f"A divisao de {num1} e {num2} é igual a = {divisao}")
Divisao_inteira = num1//num2
print(f"A divisao_inteira de {num1} e {num2} é igual a = {Divisao_inteira:.0f}")
resto_divisao = num1%num2
print(f"O resto_divisao de {num1} e {num2} é igual a = {resto_divisao}")
potenciacao = num1**num2
print(f"A potenciacao de {num1} e {num2} é igual a = {potenciacao}")
