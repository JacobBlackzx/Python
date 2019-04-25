# -*- coding: utf-8 -*-
"""
Calculadora
Autor: Vitor Hugo Romana da Silva

"""
# Iniciar Sistema

print("----- CALCULADORA V1.0 -----")

num1 = input("Digite o primeiro número: ")
num1 = int(num1)

operador = input("Digite o operador (+-/*): ")

num2 = input("Digite o segundo número: ")
num2 = int(num2)

# Operações do Sistema

# + Soma
if operador == "+":
    operacao = num1 + num2

# - Subtração
if operador == "-":
    operacao = num1 - num2

# / Divisão
if operador == "/":
    operacao = num1 / num2

# * Multiplicação
if operador == "*":
    operacao = num1 * num2

print("Resultado: ")
print(operacao)

# Encerrar Sistema

sair = False
while sair == False:

# Encerramento

    Encerrar = input("Deseja sair (N/S): ")
    if Encerrar == "S":
        sair = True