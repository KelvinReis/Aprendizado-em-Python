#Ex014 da aula 08
#Escrever um programa que coneverte uma temperatura em ºC para ºF
#Lê o valor em ºC
c = float(input('Digite o valor em ºC: '))
#Faz a conversão
f = c * 1.8 + 32
#Exibe o cálculo ao usuário
print('A temperatura {}ºC é igual a {}ºF'.format(c, f))
