#Somar dígitos
""" Faça um programa para somar os dígitos de um inteiro
Sem utilizar recursos de string, ou seja, trabalhe apenas com tipos numéricos.
Somar dígitos significa que dados um número qualquer, exemplo, 2015, devemos somar seus dígitos:
2  +  0 +  1 +  5 """
def somarDigitos(numero):
    soma = 0

    while numero != 0:
        soma   += numero % 10
        numero  = int(numero / 10) 
    return soma
print(somarDigitos(10))
assert 1 == somarDigitos(10)
assert 8 == somarDigitos(2015), "a soma dos dígitos de 2015 devem ser 8"
assert 15 == somarDigitos(456), "a soma dos dígitos de 456 devem ser 15"