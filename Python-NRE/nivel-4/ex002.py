#Somar vetor. Somar todos os valores do vetor.
def somarVetor(vetor):
    soma = 0

    for n in vetor:
        soma = soma + n
    return soma

vetor = [10, 20, 30, 0]
assert 60 == somarVetor(vetor)
print("SUCCESS")