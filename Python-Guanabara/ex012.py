#Exercício da aula 07 do curso em vídeo
#Ler o preço do produto e informa o novo valor com 5% de desconto
#Lendo o valor do produto
n = float(input('Informe o valor do produto:\n'))
#Definindo o percentual de desconto
desconto = 5
#Aplicando o desconto
valor = n*(1-desconto/100)
economia = n-valor
#Mostrando o resultado
print('Aplicando o desconto de {}% no produto de valor R${}, o novo valor é R${}.'.format(desconto, n, valor),end=' ')
print(' Um desconto de R${}.'.format(economia))