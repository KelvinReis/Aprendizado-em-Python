#Trocar valor de duas variáveis
a = 999
b = 555
print('VALOR ANTES DA ALTERAÇÃO \n A = {}, B = {}'.format(a, b))
#Usando uma varíavel auxiliar para trocar os valores
aux = a
a = b
b = aux
#Testando se os valores foram trocados
assert a == 555
assert b == 999
#Mostrando o resultado (caso o print abaixo não seja exibido, significa que o teste falhou)
print('DEPOIS DA ALTERAÇÃO \n A = {}, B = {}'.format(a, b))
