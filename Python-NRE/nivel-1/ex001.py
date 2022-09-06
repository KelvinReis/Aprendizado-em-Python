#Funções para as 4 operações aritméticas
#Uma função para cada uma das quatro operações simples com 2 valores
#Criando a função de adição
def adicao(num1,num2):
    return num1 + num2
#Testando a adição
assert adicao(2, 2) == 4
#Criando a função de subtração
def subtracao(num1, num2):
    return num1 - num2
#Testando a função de subtração
assert subtracao(5, 2) == 3
#Criando a função de multiplicacao
def multiplicacao(num1, num2):
    return num1 * num2
#Testando a função de multiplicação
assert multiplicacao(3, 4) == 12
#Criando a função de divisão
def divisao(num1, num2):
    return num1 / num2
#Testando resultado da função de divisão
assert divisao(10, 2) == 5
#Se a mensagem abaixo for exibida, significa que os testes obtiveram sucesso
print('SUCESSO')
