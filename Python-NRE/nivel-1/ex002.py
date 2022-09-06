#Custo de fabricação de um carro
'''O custo de um carro novo ao consumidor é obtido com a seguinte fórmula:
custo final = custo de fábrica +
              (custo de fábrica * percentual do distribuidor) +
              (custo de fábrica * percentual de impostos)
Considerando os valores abaixo, faça um programa para calcular o custo de fabricação.
Custo de fábrica = 10.000,00
Percentual do distribuidor = 28%
Percentual dos Impostos  = 45%
'''
#Criando a função para obter o preço do carro
def valorCarro(custoFabrica, percentualDistribuidor, percentualImpostos):
    custoFinal = custoFabrica + (percentualDistribuidor/100 * custoFabrica) + (percentualImpostos/100 * custoFabrica)
    return custoFinal
#Testando a função
assert valorCarro(10000, 28, 45) == 17300
#A mensagem abaixo indica que o programa passou no teste
print('SUCCESS')
