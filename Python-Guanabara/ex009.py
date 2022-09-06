#Exercício da aula 07 do curso em vídeo
#Ler um número e fazer sua tabuada
#Lê o número
n1 = int(input('Digite o número: '))
#Fazendo a tabuada
print('A tabuada de {} é:'.format(n1))
#Criando um loop 
for i in range(1, 10):
    print('{} * {} = {}'.format(n1, i, n1*i))
else:
    print('Essa foi a tabuada de {}'.format(n1))