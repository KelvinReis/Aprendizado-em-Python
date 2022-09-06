#Aula 08
#Programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#Importando a biblioteca math para usar métodos mais ágeis
import math
from re import A
#Lendo o valor do ângulo
a = float(input('Digite o valor do ângulo: '))
#Realizando os cálculos
#Primeiro é preciso transformar o ângulo em radiano
rad = math.radians(a)
#Com o valor radiano é possível usar as operações para obter os valores desejados
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
#Mostrando ao usuário
print('Seno de {}º é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(a, sen, cos, tan))
print('ÂNGULO {} é igual a {} radianos.'.format(a, rad))