#Maior e menor índice do vetor

def maiorIndice(vetor):

    maior = vetor[0]

    for i in vetor:
        if i > maior:
            maior = i

    return maior

def menorIndice(vetor):

    menor = vetor[0]

    for i in vetor:
        if i < menor:
            menor = i

    return menor

vetor = [6, 10, 4, 21, 9]
assert maiorIndice(vetor) == 21
assert menorIndice(vetor) == 4
print("SUCCESS")