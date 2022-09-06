#Exercício da aula 07 do curso em vídeo
#Ler a altura e largura de uma parede, medir a área, e dizer quanto de tinta é necessário, sabendo que 1l pinta 2m*2
#Lendo a altura e largura
altura = float(input('Digite a altura em metros:\n'))
largura = float(input('DIgite a largura em metros:\n'))
#Faz a conta da área
area = altura*largura
#Faz a atribuição do rendimento da tinta pra 2 metros quadrados
tinta = area/2
#Mostra ao usuário quantos litros de tinta ele precisa para a parede
print('É necessário {:.3f} litros de tinta para pintar essa parede'.format(tinta))
