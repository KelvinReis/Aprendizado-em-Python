#Maior que 10
#Descobre se um valor é maior ou menor que 10.
#Criando a função mairQue10
def maiorQue10(num):
    if num > 10:
        return True
    else:
        return False
#Testando função
assert maiorQue10(11)
assert not maiorQue10(10)
assert not maiorQue10(8)
#Mensagem exibida somente se passar no teste
print('SUCCESS')