#Número primo
#Identifica se o número é primo
def ehPrimo(num):
    if num < 2:
        return False
    else:
        for n in range(2, num):
            if num % n == 0:
                return False
            return True
#Funciona com os outros números primos, menos com o 2
assert ehPrimo(3)
print("SUCCESS")