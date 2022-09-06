#MDC máximo divisor comum
def mdc(n1, n2):
    resto = None
    while resto != 0:
        resto = n1 % n2
        n1 = n2
        n2 = resto
    return n1

assert 6 == mdc(18, 60)
print(mdc(18, 60))