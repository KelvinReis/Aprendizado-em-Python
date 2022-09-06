#Número positivo ou negativo
#Descobre se um valor é positivo ou negativo (considere o valor zero como positivo).
#Criando a função ehPositivo
def ehPositivo(num):
    if num >= 0:
        return True
    else:
        return False
#Testando a função
assert ehPositivo(5)
assert not ehPositivo(-5)
assert ehPositivo(0)
#A mensagem abaixo é exibida somente passando sem erros pelo teste
print('SUCCESS')