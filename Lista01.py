#Questão 1 - Calculadora

# val_1 = int(input("Insira um valor: "))
# val_2 = int(input("Insira outro valor: "))
# soma = val_1 + val_2
# multiplicacao = val_1 * val_2
# subtracao = val_1 - val_2
# divisao = val_1 / val_2
# print ("A soma desses números é: ", soma)
# print ("A subtração desses números é: ", subtracao)
# print ("A multiplicação desses números é: ", multiplicacao)
# print ("A divisão desses números é: ", divisao)
# print ("Fim.")

#Questão 2 - Conversão de temperatura
# val_celsius = int(input("Insira um valor de temperatura em Celsius: "))
# conversao = (val_celsius * 9/5) + 32
# print ("A temperatura", val_celsius,"ºC em Farenheint é de: ", conversao, "ºF")

#Questão 3 - Cálculo da área do círculo
# import math
# pi = math.pi
# raio = int(input("Insira o valor do raio de um cículo: "))
# area_circulo = pi * (raio**2)
# print ("A área do cículo é: ", area_circulo)

#Questão 4 - Cálculo da área do triângulo
# base = int(input("Insira um valor de base: "))
# altura = int(input("Insira um valor de altura: "))
# area_triangulo = (base*altura)/2

# print ("A área do triângulo é: ", area_triangulo)

#Questão 5 - Volume da esfera
import math
pi = math.pi
raio_esfera = int(input("Insira o valor do raio da esfera: "))
volume = (4/3)*pi*(raio_esfera**3)

print ("O volume da esfera é de: ", volume, "L")