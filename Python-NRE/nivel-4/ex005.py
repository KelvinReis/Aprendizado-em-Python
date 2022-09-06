#Valores repetidos. Descobrir se há valores repetidos no vetor.
def haDuplicados(vetor):
    tam = len(vetor)
    inicio = 0
    while tam!= inicio:
        tam = len(vetor)
        while tam != inicio:
            if vetor[tam-1] == vetor[inicio]:
                return True
            tam = tam - 1
        inicio = inicio + 1

assert haDuplicados([1, 2, 4, 3])
print("SUCCESS")