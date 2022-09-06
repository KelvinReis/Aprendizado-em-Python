#Copiar um vetor

def copiarVetor(vetor1):
    vetor2 = []
    for i in vetor1:
        vetor2.append(i)
        
    return vetor2

vetor1 = [10, 20, 30, 40]
assert vetor1 == copiarVetor(vetor1)
print("SUCCESS")