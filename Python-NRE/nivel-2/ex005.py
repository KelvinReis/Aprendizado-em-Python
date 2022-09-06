#Equação de 2 grau
#Calcula as raízes da equação do 2 grau conforme a fórmula de Bhaskara.
import math
#Função para descobrir o valor de delta
def delta(a, b, c):
    return (b**2 - (4 * a * c))
#Função para descobrir o valor da primeira raiz
def raiz1(a, b, c):
    return ((-b + math.sqrt(delta(a, b, c))) / 2 * a)
#Função para descobrir o valor da segunda raiz
def raiz2(a, b, c):
    return ((-b - math.sqrt(delta(a, b, c))) / 2 * a)

a = 1
b = 0
c = -16

assert 64 == delta(a, b , c)
assert 4 == raiz1(a, b, c)
assert -4 == raiz2(a, b, c)

print('SUCCESS')