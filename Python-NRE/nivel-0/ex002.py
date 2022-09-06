#O dobro de um número qualquer
#Função que retorna o dobro de um número qualquer
#Usuário informa o valor
num = int(input('Informe um número inteiro:\n'))
#A função dobro é criada o número informado pelo usuário é passado como parâmetro
def dobro(num):
    return num * 2 #A função retorna o dobro do valor
#Verifica se o que está sendo retornado pela função é o dobro do valor informado
assert (num * 2) == dobro(num)
print(f'O dobro de {num} é {dobro(num)}.')
