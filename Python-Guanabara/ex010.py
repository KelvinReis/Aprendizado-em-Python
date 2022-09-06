#Exercício da aula 07 do curso em vídeo
#Ler o dinheiro que a pessoa tem na carteira e mostra quatos dólares ela pode comprar
#Lendo o valor que a pessoa tem
reais = float(input('Digite o valor que possui em reais: '))
#Setar o valor do dólar
dolar = 5.37
#Faz o cálculo da conversão
valor = reais/dolar
#Mostra o resultado com três casas decimais após o ponto
print('Com valor de R${} vc pode comprar ${:.3f}'.format(reais, valor))
