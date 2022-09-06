#MMC mínimo múltiplo comum
def mmc(n1, n2):
    a = n1
    b = n2

    resto = None
    while resto != 0:
        resto = a % b
        a = b
        b = resto

    return (n1 * n2) / a

assert 180 == mmc(18, 60)
print (mmc(18, 60))