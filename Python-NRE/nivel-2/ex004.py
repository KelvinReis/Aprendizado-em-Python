#Conversor Celsius/Fahrenheit 
#Criar duas funções, uma de ºC para ºF, e outra de ºF para ºC
#Criando funcao de C para F

def toCelcius (f):
    return (f - 32) / 1.8
def toFahrenheit(c):
    return c * 1.8 + 32
c = 100
f = 212
assert c == toCelcius(f)
assert f == toFahrenheit(c)
print('SUCCESS')
