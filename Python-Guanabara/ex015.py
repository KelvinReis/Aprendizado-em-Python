#Ex015
"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""
#Lê a quantidade de km percorrido
km = float(input('Digite a quantidade de kilômetros percorrido: '))
#Lê a quantidade de dias que o carro foi usado
d = int(input('Digite a quantidade de dias que usou o carro:'))
#Faz a soma de quanto o usuário deve pagar pelo aluguel do carro
total = (km*0.15)+(d*60)
#Mostra ao usuário quanto ele deve pagar
print('O valor total do aluguel é de R${}.'.format(total))