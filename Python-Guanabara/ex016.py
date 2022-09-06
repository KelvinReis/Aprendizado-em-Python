#Aula 08
#Ex016 Ler um número real qualquer e mostrar a porção inteira
import math
n = float(input('Digite o valor real:'))
print('A parte inteira de {} é {}'.format(n, math.trunc(n)))