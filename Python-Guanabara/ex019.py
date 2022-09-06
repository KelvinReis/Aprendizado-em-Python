#Aula 08
#Ler o nome dos 4 alunos e escrever na tela o nome do escolhido.
#Importar a biblioteca random para poder sortear o nome
from random import choices
#Lendo os nomes dos alunos
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
#Colocando numa lista
lista = [n1, n2, n3, n4]
#Mostrando quem foi o escolhido
print('O aluno escolhido foi o {}'.format(choices(lista)))