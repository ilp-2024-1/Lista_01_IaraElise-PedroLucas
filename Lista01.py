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
# import math
# pi = math.pi
# raio_esfera = int(input("Insira o valor do raio da esfera: "))
# volume = (4/3)*pi*(raio_esfera**3)

# print ("O volume da esfera é de: ", volume, "L")

#Questão 6 - Calculadora de Média Airtmética
# nota1 = float(input("Insira sua primeira nota: "))
# nota2 = float(input("Insira sua segunda nota: "))
# nota3 = float(input("Insira sua terceira nota: "))
# media_aritmetica = round(float((nota1+nota2+nota3)/3))

# print ("Sua primeira nota foi: .", nota1, 
#        "\n Sua segunda nota foi: .", nota2, 
#        "\n Sua terceira nota foi: .", nota3, 
#        "\n Sua média é: ", media_aritmetica)

#Questão 7 - Média ponderada
# nota1 = float(input("Insira sua primeira nota: "))
# nota2 = float(input("Insira sua segunda nota: "))
# nota3 = float(input("Insira sua terceira nota: "))
# nota4 = float(input("Insira sua quarta nota: "))
# peso1 = 1
# peso2 = 2
# peso3 = 2
# peso4 = 3
# media_pond = round(float(((nota1*peso1) + (nota2*peso2) + (nota3*peso3) + (nota4*peso4)) / (peso1 + peso2 +peso3 +peso4)))

# print ("Suas notas são, respectivamente: ", nota1, nota2, nota3, nota4)
# print ("Sua média é: ", media_pond)

#Questão 8 - Equação do Segundo grau
# a = float(input("Insirao o valor de a: "))
# b = float(input("Insirao o valor de b: "))
# c = float(input("Insirao o valor de c: "))
# x = float(input("Insirao o valor de x: "))
# equacao_y = float(a*x + b*x + c)

# print ("O valor de y é: ", equacao_y)

#Questão 9 - Calculadora de IMC
# peso = float(input("Insira o peso: "))
# altura = float(input("Insira a altura: "))
# imc = round(peso/(altura**2))

# print ("O Índice de massa corporal é: ", imc, "kg/m2")

#Questão 10 - Tabuada
# numero = int(input("Insira um número: "))
# x1 = numero*1
# x2 = numero*2
# x3 = numero*3
# x4 = numero*4
# x5 = numero*5
# x6 = numero*6
# x7 = numero*7
# x8 = numero*8
# x9 = numero*9
# x10 = numero*10

# print (numero,"x 1 =", x1, ";", numero,"x 2 =", x2, ";", numero,"x 3 =", x3, ";", numero,"x 4 =", x4, ";", numero,"x 5 =", x5, ";"
#        , numero,"x 6 =", x6, ";", numero,"x 7 =", x7, ";", numero,"x 8 =", x8, ";", numero,"x 9 =", x9, ";", numero,"x 10 =", x10, ";")

#Questão 11 - Conversão de Segundos para o formato Hora:Minuto:Segundo
# segundos = int(input("Insira a quantidade de segundos: "))
# horas = round(segundos/3600)
# minutos = round((segundos%3600)/60, 2)
# segundos_2 = round(minutos*60)

# print ("A conversão ficou: Hora: ", horas, ", Minuto: ", minutos, ", Segundo: ", segundos_2, ".")