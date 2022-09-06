#Valor par ou ímpar
#Criando a função
def ehPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

#Testando a função
assert ehPar(8)
assert not ehPar(7)
assert ehPar(0)
