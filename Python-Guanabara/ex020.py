#Aula 08
#Leia o nome dos quatro alunos e mostre a ordem sorteada.
#Lendo o nome dos alunos
from random import shuffle
n1 = str(input('Primeiro aluno\n'))
n2 = str(input('Segundo aluno\n'))
n3 = str(input('Terceiro aluno\n'))
n4 = str(input('Quarto aluno\n'))
#Colocando os alunos em uma lista
lista = [n1, n2, n3, n4]
#Embaralhando a lista
shuffle(lista)
#Mostrando a ordem dos alunos
print('A ordem  da apresentação será')
print(lista)