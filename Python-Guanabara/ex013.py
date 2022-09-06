#Exercício da aula 07 do curso em vídeo
#Ler o salário da pessoa e mostrar novo salário com aumento de 15%
#Lendo o salário atual
atual = float(input('Informe o salário atual:\n'))
#Definindo a porcentagem de aumento
porcentagem = 15
#Calculando o novo salário
salarioNovo = atual*(1+porcentagem/100)
valorAumento = salarioNovo-atual
#Mostrando ao colaborador
print('Com aumento de {}%, seu salário agora é de R${:.2f}. Aumento de R${:.2f}.'.format(porcentagem, salarioNovo, valorAumento))