#Juro simples
#Calcula o juros simples segundo a fórmula J = C.i.n
'''Onde: 
J = juros,
C = capital,
i = taxa de empréstimo
n = períodos'''
#Criando a função jurosSimples
def jurosSimples(c, i, n):
    j = c * (i/100) * n
    return j
#Testando a função
assert jurosSimples(16000, 4, 4) == 2560
#A mensagem abaixo só é mostrado em caso de sucesso do teste
print('SUCCESS')
