#Aula 08
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
#Lendo o cateto oposto
from math import hypot
oposto = float(input('Cateto oposto: '))
#Lendo o cateto adjacente
adjacente = float(input('Cateto adjacente: '))
#Fazendo o cálculo
hipotenusa = hypot(oposto, adjacente)
#Mostrando o resultado
print('A hipotenusa é igual a {:.2f}.'.format(hipotenusa))