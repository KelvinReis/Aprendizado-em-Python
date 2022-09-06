#Reajustando salário
'''calcule o reajuste de um salário, utilize os seguintes dados:
salário  = 1.000,00
reajuste = 15%,
'''
#Criando a função reajuste
def reajuste(salario, reajuste):
    return salario * (reajuste / 100)
#Testando a função
assert reajuste(1000 , 15) == 150
#Mensagem abaixo é exibida em caso de sucesso no teste
print('SUCCESS')
