#Aula 08 
#Reproduzir um áudio mp3
import pygame
#Primeiro é preciso inicializar o pygame
pygame.init()
#Usando a função mixer para localizar e reproduzir a música
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
#O PyGame sofreu algumas modificações. Na versão 3.9py, é necessário colocar o input()
input()
pygame.event.wait()